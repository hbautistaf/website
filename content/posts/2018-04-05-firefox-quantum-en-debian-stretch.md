---
title: Firefox Quantum en Debian Stretch
date: 2018-04-05 13:30:28+00:00
slug: firefox-quantum-en-debian-stretch
image: /images/2018/Pant_FirefoxAcercade.png
categories:
- Gnu/Linux
tags:
- Cómos
- Firefox
- Linux
aliases:
- /2018/04/05/firefox-quantum-en-debian-stretch/
- /linux/firefox-quantum-en-debian-stretch/
---

[

![New Tab](/images/2018/new-tab.png)

][1]

<a href="https://www.mozilla.org/es-MX/firefox/" target="_blank" rel="noopener">**Firefox Quantum**</a> es la nueva versión de **Firefox** que viene completamente renovada. Desafortunadamente no lo encontramos en los repositorios de <a href="https://wiki.debian.org/Firefox" target="_blank" rel="noopener">**Debian Stretch**</a> ni en <a href="https://backports.debian.org/" target="_blank" rel="noopener">Backports</a>. Aunque si esta en Sid, lo podríamos instalar usando APT Pinning, lo cual no es muy recomendable, y en lo personal me causaba muchos conflictos.

[

![Firefox Quantum](/images/2018/Pant_FirefoxAcercade.png)

][2]Lo primero que hay que hacer es descargar el archivo comprimido desde el sitio oficial de Mozilla, y una vez descargado realizamos los siguientes pasos como root:

```bash
root@elrond:~# tar xjfv /home/hbautista/Descargas/firefox-59.0.1.tar.bz2 -C /opt/
```

En mi caso y dado que no necesito Mozilla Firefox ESR, que al momento de escribir esto es la versión 52.7.2esr-1~deb9u1, decidí quitar.

```bash
root@elrond:~# apt remove firefox-esr
```

Necesitamos es crear su acceso directo, que es un archivo .desktop y se puede crear con tu editor de texto favorito, en mi caso estoy usando nano:

```bash
root@elrond:~# nano /usr/share/applications/firefox-quantum.desktop
```

Debe contener lo siguiente:

```xml
[Desktop Entry]  
Name=Firefox Quantum  
Comment=Web Browser  
GenericName=Web Browser  
X-GNOME-FullName=Firefox Quantum Web Browser  
Exec=/opt/firefox/firefox %u  
Terminal=false  
X-MultipleArgs=false  
Type=Application  
Icon=/opt/firefox/browser/chrome/icons/default/default128.png  
Categories=Network;WebBrowser;  
MimeType=text/html;text/xml;application/xhtml+xml;application/xml;application/vnd.mozilla.xul+xml;application/rss+xml;application/rdf+xml;image/gif;image/jpeg;image/png;x-scheme-handler/http;x-scheme-handler/ht$  
StartupWMClass=Firefox  
StartupNotify=true
```

Para guardar y cerrar presiona CTRL + O y para salir CTRL + X

Le damos permiso de ejecución al acceso directo:

```bash
root@elrond:~# chmod +x /usr/share/applications/firefox-quantum.desktop
```

Creamos un enlace simbólico para que cualquier usuario pueda ejecutarlo:

```bash
root@elrond:~# ln -s /opt/firefox/firefox /usr/lib/
```

[

![Firefox & Mate en Debian Stretch](/images/2018/Pant_Firefox01.png)

][3]  
Actualización manual de Mozilla Firefox

Si por alguna razón, no se actualiza de forma automática, siempre se puede hacer manualmente. Descargar el archivo .bz2 desde el sitio de <a href="https://www.mozilla.org/es-MX/" target="_blank" rel="noopener">Mozilla Firefox</a> y hacer lo siguiente:

Eliminamos todo el contenido en /opt:

```bash
root@elrond:~# rm -Rf /opt/firefox/
```

Y volvemos a descomprimir:

```bash
root@elrond:~# tar xjfv /home/hbautista/Descargas/firefox-59.0.2.tar.bz2 -C /opt/
```

 [1]: /images/2018/new-tab.png
 [2]: /images/2018/Pant_FirefoxAcercade.png
 [3]: /images/2018/Pant_Firefox01.png
