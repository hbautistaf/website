#!/usr/bin/env python3
import os
import re
import html
import yaml
import glob
import shutil
from pathlib import Path

SOURCE_POSTS_DIR = Path("hugo-export/posts")
TARGET_POSTS_DIR = Path("content/posts")
SOURCE_ABOUT = Path("hugo-export/sobre-mi/index.md")
TARGET_ABOUT = Path("content/page/about/index.md")
SOURCE_UPLOADS = Path("hugo-export/wp-content/uploads")
TARGET_IMAGES = Path("static/images")

def clean_html_entities(text) -> str:
    if text is None:
        return ""
    text = str(text)
    replacements = {
        '&#8211;': '–',
        '&#8212;': '—',
        '&#8216;': "'",
        '&#8217;': "'",
        '&#8220;': '"',
        '&#8221;': '"',
        '&#8230;': '…',
        '&#038;': '&',
        '&#039;': "'",
        '&amp;': '&',
        '&quot;': '"',
        '&nbsp;': ' ',
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return html.unescape(text)

def clean_image_url(url: str) -> str:
    if not url:
        return ""
    url = str(url).strip()
    # Strip photon CDN prefixes
    url = re.sub(r'https?://i[0-9]\.wp\.com/(?:https?://)?(?:blog\.)?hbautista\.com', '', url)
    url = re.sub(r'https?://(?:blog\.)?hbautista\.com', '', url)
    # Strip query params like ?fit=... or ?resize=... or ?ssl=1
    url = re.sub(r'\?(?:fit|resize|ssl|w|h|strip)=[^ \)\"\'>]+', '', url)
    
    # Transform /wp-content/uploads/YYYY/MM/file.ext -> /images/YYYY/file.ext
    # or /wp-content/uploads/YYYY/file.ext -> /images/YYYY/file.ext
    match_year_month = re.search(r'wp-content/uploads/(\d{4})/(?:\d{2}/)?([^/\"\'>\s\)]+)', url)
    if match_year_month:
        year = match_year_month.group(1)
        filename = match_year_month.group(2)
        return f"/images/{year}/{filename}"
    
    # Generic wp-content/uploads/filename -> /images/filename
    match_root = re.search(r'wp-content/uploads/([^/\"\'>\s\)]+)', url)
    if match_root:
        filename = match_root.group(1)
        return f"/images/{filename}"

    # If already /images/...
    if url.startswith("/images/"):
        return url

    return url

def clean_body_content(body: str) -> str:
    # Normalize unicode quotes and dashes before processing
    body = body.replace('»', '"').replace('«', '"').replace('&#8220;', '"').replace('&#8221;', '"')
    body = body.replace('&#8216;', "'").replace('&#8217;', "'").replace('&#8211;', '–').replace('&#8212;', '—')
    body = body.replace('&#038;', '&').replace('&amp;', '&').replace('&nbsp;', ' ')

    # 1. SyntaxHighlighter [cc lang="bash"] ... [/cc] or [cc lang=bash] or [cc]
    def replace_cc_lang(match):
        lang = (match.group(1) or '').lower().strip().replace('"', '').replace("'", "")
        code = match.group(2)
        lang_map = {'bash': 'bash', 'sh': 'bash', 'shell': 'bash', 'php': 'php', 'python': 'python', 'sql': 'sql', 'xml': 'xml', 'css': 'css', 'js': 'javascript', 'html': 'html'}
        lang = lang_map.get(lang, lang or '')
        code = clean_html_entities(code)
        return f"\n```{lang}\n{code.strip()}\n```\n"

    body = re.sub(r'\[cc(?:\s+lang=["\']?([a-zA-Z0-9_-]+)["\']?)?[^\]]*\](.*?)\[/cc\]', replace_cc_lang, body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'\[code(?:\s+lang=["\']?([a-zA-Z0-9_-]+)["\']?)?[^\]]*\](.*?)\[/code\]', replace_cc_lang, body, flags=re.DOTALL | re.IGNORECASE)

    # 2. Clean <pre class="brush:bash"> ... </pre>
    def replace_pre_brush(match):
        lang = match.group(1).lower().strip()
        code = match.group(2)
        lang_map = {'bash': 'bash', 'sh': 'bash', 'shell': 'bash', 'php': 'php', 'python': 'python', 'sql': 'sql', 'xml': 'xml', 'css': 'css', 'js': 'javascript'}
        lang = lang_map.get(lang, lang)
        code = clean_html_entities(code)
        return f"\n```{lang}\n{code.strip()}\n```\n"

    body = re.sub(r'<pre\s+class=["\']brush:\s*([a-zA-Z0-9_-]+)[^"\']*["\']\s*>(.*?)</pre>', replace_pre_brush, body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<pre\s+class=["\']wp-block-code["\']\s*><code>(.*?)</code></pre>', lambda m: f"\n```\n{clean_html_entities(m.group(1)).strip()}\n```\n", body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'```wp-block-code\s*<code>(.*?)</code>\s*```', lambda m: f"\n```\n{clean_html_entities(m.group(1)).strip()}\n```\n", body, flags=re.DOTALL | re.IGNORECASE)
    body = re.sub(r'<pre><code>(.*?)</code></pre>', lambda m: f"\n```\n{clean_html_entities(m.group(1)).strip()}\n```\n", body, flags=re.DOTALL | re.IGNORECASE)

    # 3. Clean WordPress Gutenberg Image blocks
    def replace_wp_figure(match):
        block = match.group(0)
        img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\'][^>]*>', block, flags=re.DOTALL)
        alt_match = re.search(r'alt=["\']([^"\']*)["\']', block)
        caption_match = re.search(r'<figcaption[^>]*>(.*?)</figcaption>', block, flags=re.DOTALL)
        
        src = clean_image_url(img_match.group(1)) if img_match else ""
        alt = alt_match.group(1) if alt_match else ""
        caption = caption_match.group(1).strip() if caption_match else ""
        caption = re.sub(r'<[^>]+>', '', caption)
        
        alt_text = caption or alt or "Imagen"
        return f"\n\n![{alt_text}]({src})\n\n"

    body = re.sub(r'<div class="wp-block-image".*?</div>', replace_wp_figure, body, flags=re.DOTALL)
    body = re.sub(r'<figure class="[^"]*wp-block-image[^"]*".*?</figure>', replace_wp_figure, body, flags=re.DOTALL)

    # 4. Clean messy WP markdown reference links: [![" data-image-... src="..."][N]]
    def clean_messy_ref_img(match):
        inner = match.group(0)
        src_m = re.search(r'src=["\']([^"\']+)["\']', inner)
        title_m = re.search(r'title=["\']([^"\']*)["\']', inner)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', inner)
        src = clean_image_url(src_m.group(1)) if src_m else ""
        alt = (title_m.group(1) if title_m else "") or (alt_m.group(1) if alt_m else "Imagen")
        return f"\n\n![{alt}]({src})\n\n"

    body = re.sub(r'\[!\[[^\]]*src=["\'][^"\']+["\'][^\]]*\]\[\d+\]\]?', clean_messy_ref_img, body)

    # 5. Clean linked images: <a href="..."><img ...></a>
    def replace_linked_img(match):
        href = clean_image_url(match.group(1))
        inner = match.group(2)
        src_m = re.search(r'src=["\']([^"\']+)["\']', inner)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', inner)
        if not src_m:
            return match.group(0)
        src = clean_image_url(src_m.group(1))
        alt = alt_m.group(1) if alt_m else ""
        return f"\n\n![{alt}]({src})\n\n"

    body = re.sub(r'<a\s+[^>]*href=["\']([^"\']+)["\'][^>]*>(\s*<img[^>]+>.*?)</a>', replace_linked_img, body, flags=re.DOTALL | re.IGNORECASE)

    # 6. Clean stand-alone <img ...> tags
    def replace_img_tag(match):
        img_str = match.group(0)
        src_m = re.search(r'src=["\']([^"\']+)["\']', img_str)
        alt_m = re.search(r'alt=["\']([^"\']*)["\']', img_str)
        if not src_m:
            return ""
        src = clean_image_url(src_m.group(1))
        alt = alt_m.group(1) if alt_m else ""
        return f"\n\n![{alt}]({src})\n\n"

    body = re.sub(r'<img[^>]+>', replace_img_tag, body, flags=re.DOTALL | re.IGNORECASE)

    # 7. Clean reference links at bottom of post: [1]: https://.../wp-content/...
    def clean_ref_link(match):
        ref_num = match.group(1)
        ref_url = clean_image_url(match.group(2))
        return f"[{ref_num}]: {ref_url}"
    body = re.sub(r'\[(\d+)\]:\s*(https?://[^\s]+)', clean_ref_link, body)

    # 8. Clean paragraph tags
    body = re.sub(r'<p[^>]*>', '\n\n', body)
    body = re.sub(r'</p>', '\n\n', body)

    # 9. Clean span tags and residual embeds
    body = re.sub(r'<span class="embed-youtube"[^>]*>.*?</span>', '', body)

    # 10. Clean residual headings attributes and separators
    body = re.sub(r'\{#?[a-zA-Z0-9_.-]*\.wp-block-[^}]*\}', '', body)
    body = re.sub(r'<hr class="wp-block-separator[^"]*"[^>]*/>', '\n---\n', body)

    # 11. Clean simple inline HTML tags: <strong>, <b>, <em>, <i>, <del>, <strike>
    body = re.sub(r'<(?:strong|b)>(.*?)</(?:strong|b)>', r'**\1**', body, flags=re.DOTALL)
    body = re.sub(r'<(?:em|i)>(.*?)</(?:em|i)>', r'*\1*', body, flags=re.DOTALL)
    body = re.sub(r'<(?:del|strike)>(.*?)</(?:del|strike)>', r'~~\1~~', body, flags=re.DOTALL)

    # 12. Clean entities
    body = clean_html_entities(body)

    # 13. Clean excessive blank lines (more than 2)
    body = re.sub(r'\n{3,}', '\n\n', body)

    return body.strip()

def process_posts():
    os.makedirs(TARGET_POSTS_DIR, exist_ok=True)
    post_files = sorted(glob.glob(str(SOURCE_POSTS_DIR / "*.md")))
    print(f"Found {len(post_files)} posts to process.")

    migrated_count = 0
    for file_path in post_files:
        basename = os.path.basename(file_path)
        if basename == "2021-01-05-.md":
            continue

        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            raw_content = f.read()

        if not raw_content.startswith("---"):
            continue

        parts = raw_content.split("---", 2)
        if len(parts) < 3:
            continue

        fm_text = parts[1]
        body = parts[2]

        try:
            fm = yaml.safe_load(fm_text) or {}
        except Exception as e:
            print(f"YAML load error in {file_path}: {e}")
            continue

        date_match = re.match(r'^(\d{4}-\d{2}-\d{2})-(.*)\.md$', basename)
        if date_match:
            date_prefix = date_match.group(1)
            slug_from_name = date_match.group(2)
        else:
            slug_from_name = os.path.splitext(basename)[0]

        title = clean_html_entities(str(fm.get("title", slug_from_name)))
        orig_url = fm.get("url", "")
        
        # Build aliases list
        aliases = []
        if orig_url:
            cleaned_orig_url = str(orig_url).strip()
            if cleaned_orig_url and cleaned_orig_url != f"/p/{slug_from_name}/":
                aliases.append(cleaned_orig_url)
                if not cleaned_orig_url.endswith("/"):
                    aliases.append(cleaned_orig_url + "/")
        
        # Add historical date-based aliases if different
        if date_match:
            year, month, day = date_prefix.split("-")
            date_alias = f"/{year}/{month}/{day}/{slug_from_name}/"
            if date_alias not in aliases:
                aliases.append(date_alias)

        # Clean featured image to /images/YYYY/filename
        image = fm.get("featured_image") or fm.get("image") or ""
        if image:
            image = clean_image_url(str(image))

        categories = fm.get("categories", [])
        if isinstance(categories, (str, int, float)):
            categories = [categories]
        categories = [clean_html_entities(str(c)) for c in categories if c is not None]

        tags = fm.get("tags", [])
        if isinstance(tags, (str, int, float)):
            tags = [tags]
        tags = [clean_html_entities(str(t)) for t in tags if t is not None]

        clean_fm = {
            "title": title,
            "date": fm.get("date"),
            "slug": slug_from_name,
        }

        if image:
            clean_fm["image"] = image
        if categories:
            clean_fm["categories"] = categories
        if tags:
            clean_fm["tags"] = tags
        if aliases:
            clean_fm["aliases"] = sorted(list(set(aliases)))
        if fm.get("draft"):
            clean_fm["draft"] = True

        clean_body = clean_body_content(body)

        target_path = TARGET_POSTS_DIR / basename
        output_content = "---\n" + yaml.dump(clean_fm, allow_unicode=True, sort_keys=False) + "---\n\n" + clean_body + "\n"

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(output_content)

        migrated_count += 1

    print(f"Successfully migrated {migrated_count} posts to {TARGET_POSTS_DIR}")

def process_about_page():
    if not SOURCE_ABOUT.exists():
        print(f"About source {SOURCE_ABOUT} not found.")
        return
    
    os.makedirs(TARGET_ABOUT.parent, exist_ok=True)
    with open(SOURCE_ABOUT, "r", encoding="utf-8", errors="ignore") as f:
        raw_content = f.read()

    parts = raw_content.split("---", 2)
    body = parts[2] if len(parts) >= 3 else raw_content
    clean_body = clean_body_content(body)

    clean_fm = {
        "title": "Sobre mí",
        "slug": "about",
        "menu": {
            "main": {
                "weight": -80,
                "params": {
                    "icon": "user"
                }
            }
        },
        "comments": False
    }

    output_content = "---\n" + yaml.dump(clean_fm, allow_unicode=True, sort_keys=False) + "---\n\n" + clean_body + "\n"
    with open(TARGET_ABOUT, "w", encoding="utf-8") as f:
        f.write(output_content)
    print(f"Successfully migrated About page to {TARGET_ABOUT}")

def organize_images_by_year():
    print(f"Organizing images from {SOURCE_UPLOADS} into {TARGET_IMAGES}/YYYY/...")
    os.makedirs(TARGET_IMAGES, exist_ok=True)

    # 1. Process YYYY/MM/* files
    for year_dir in SOURCE_UPLOADS.glob("*"):
        if year_dir.is_dir() and year_dir.name.isdigit() and len(year_dir.name) == 4:
            year = year_dir.name
            target_year_dir = TARGET_IMAGES / year
            os.makedirs(target_year_dir, exist_ok=True)

            for item in year_dir.rglob("*"):
                if item.is_file():
                    target_file = target_year_dir / item.name
                    if not target_file.exists():
                        shutil.copy2(item, target_file)

    # 2. Process root files in uploads (e.g. logo_hbautista.png)
    for root_file in SOURCE_UPLOADS.glob("*.*"):
        if root_file.is_file():
            target_file = TARGET_IMAGES / root_file.name
            if not target_file.exists():
                shutil.copy2(root_file, target_file)

    print("Images organized by year successfully!")

if __name__ == "__main__":
    organize_images_by_year()
    process_posts()
    process_about_page()
