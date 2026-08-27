---
title: Desinstalar Skimmer
date: 2011-12-27 23:25:31+00:00
slug: desinstalar-skimmer
image: /wp-content/uploads/2011/12/skimmer-1.jpg
categories:
- Cómos
- Gnu/Linux
tags:
- AdobeAIR
- Ayuda
- Cómos
- Debian
- Dpkg
- Skimmer
- Tips
aliases:
- /2011/12/27/desinstalar-skimmer/
- /comos/desinstalar-skimmer/
---

skimmer

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/12/skimmer-1.jpg?fit=648%2C362&ssl=1" class="aligncenter size-medium wp-image-815" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/12/skimmer-1.jpg?resize=300%2C168&ssl=1" alt="" width="300" height="168" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/12/skimmer-1.jpg?resize=300%2C168&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/12/skimmer-1.jpg?resize=768%2C429&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/12/skimmer-1.jpg?w=950&ssl=1 950w" sizes="auto, (max-width: 300px) 100vw, 300px" />

  Pues hace un tiempo instalé Skimmer (http://www.fallon.com/skimmer/) para compartir fotos de flickr (principalmente) en un entorno de microblogging, como Twitter. Al menos recuerdo que por esa razón instalé tal aplicación, aunque al parecer de acuerdo al sitio oficial, se puede leer lo siguiente:

> 

>   Skimmer℠ is an Adobe® AIR™ desktop application designed to streamline, beautify, and enhance the experience of participating in your most frequently used social networking activities. It improves upon your day-to-day interaction with multiple social networks, removing distractions and providing a rich experience that is particularly suited to multimedia content.
> 

> 
> Las aplicaciones con Adobe Air, no tienen (en su mayoría) un botón para desinstalar alguna aplicación que hemos ya instalado.

Pues bien, en Debian (y distribuciones basadas en ella) se usa aptitude o apt-get para instalar o desinstalar paquetes, que finalmente no son otra cosa, más que un front-end para una aplicación llamada dpkg (rpm en distribuciones como RedHat), así que usaremos este comando para obtener un listado de los paquetes instalados, aplicando un filtro del paquete que requerimos, y no, no se llama Skimmer, sino Fallon 😉

```bash
root@luke:/home/hbautista# dpkg --list |grep -i fallon
ii fallon.957283bd7ae99c519b762f3e2f85073ed97331f2.1 1.1.73 <>
```

Como podrán darse cuenta, aparece la información de la aplicación Skimmer con su número de identificación "957283bd7ae99c519b762f3e2f85073ed97331f2.1" y la versión instalada 1.1.73, así que usando el mismo comando, vamos a desinstalarlo:

```bash
root@luke:/home/hbautista# dpkg -r fallon.957283bd7ae99c519b762f3e2f85073ed97331f2.1
(Leyendo la base de datos ... 200502 ficheros o directorios instalados actualmente.)
Desinstalando fallon.957283bd7ae99c519b762f3e2f85073ed97331f2.1 ...
Procesando disparadores para packagekit-backend-aptcc ...
Procesando disparadores para software-center ...
Procesando disparadores para python-central ...
root@luke:/home/hbautista#
```

Y con eso quitamos ese paquete que al menos a mi, me estorbaba puesto que nunca funcionó como se supone debería de hacerlo.
