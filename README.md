# hbautista.com — Sitio Web Personal y Blog

Sitio web personal y blog técnico de **Héctor Bautista Flores** ([@hbautista](https://hbautista.com/)).

Construido como generador de sitios estáticos utilizando **[Hugo](https://gohugo.io/)** (Extended) y el tema **[Hugo Theme Stack](https://github.com/CaiJimmy/hugo-theme-stack)**, con una landing page interactiva personalizada y soporte multilingüe (Español / Inglés).

---

## 🛠️ Tecnologías

- **Generador Estático:** Hugo Extended
- **Tema del Blog:** [Hugo Theme Stack](https://github.com/CaiJimmy/hugo-theme-stack)
- **Landing Page:** Diseño custom con estética terminal y enlaces profesionales
- **Comentarios:** [Giscus](https://giscus.app/) (respaldado en GitHub Discussions)
- **Despliegue:** Scripts automatizados vía SSH / rsync y FTPS / lftp

---

## 🚀 Desarrollo Local

1. Clonar el repositorio con sus submódulos:
   ```bash
   git clone --recurse-submodules git@github.com:hbautistaf/website.git
   cd website
   ```
2. Iniciar el servidor local de Hugo:
   ```bash
   hugo server -D
   ```
3. Abrir en el navegador `http://localhost:1313/`.

---

## 📄 Licencia

- **Código:** [MIT License](LICENSE.md#1-código-fuente--source-code-mit-license)
- **Contenido y Artículos:** [Creative Commons CC BY-NC 4.0](LICENSE.md#2-contenido-y-artículos--content--articles-cc-by-nc-40)
