---
title: Eliminar paquetes huerfanos con Deborphan
date: 2012-01-03 04:11:51+00:00
slug: eliminar-paquetes-huerfanos-con-deborphan
image: /images/2012/Pant_Synaptic-1.png
categories:
- Cómos
- Gnu/Linux
tags:
- Cómos
- Debian
- Deborphan
- Howto
- Linux
aliases:
- /2012/01/02/eliminar-paquetes-huerfanos-con-deborphan/
- /comos/eliminar-paquetes-huerfanos-con-deborphan/
---

Cuando instalas un paquete en **Debian**/**Ubuntu** éste suele tener dependencias, las cuales se instalan automáticamente. Si desinstalas ese paquete padre, las dependencias se quedarán en el disco ocupando un espacio inútil. A estos paquetes se les llama **huérfanos** (no tienen padre). **Deborphan** encuentra paquetes "huérfanos" en el sistema. Determina qué paquetes no tienen a otros que dependan de su instalación, y le muestra una lista de estos paquetes. Su mayor utilidad es buscar bibliotecas, pero se puede usar con paquetes de todas las secciones.

  Este paquete también incluye **orphaner**, una interfaz de menú de texto para **deborphan**. Instale los paquetes recomendados **dialog**, **gettext-base** y **apt** si desea un orphaner plenamente funcional, con todas sus características.

Ahora bien, lo primero que debemos hacer es instalarlo

```bash
root@luke:/home/hbautista# aptitude install deborphan
```

Y después de instalado, se puede ejecutar tal cual:

```bash
root@luke:/home/hbautista# deborphan 
libgnomekbd4
kdepimlibs-kio-plugins
librpcsecgss3
libchamplain-gtk-0.8-1
libcryptui0a
libslab0a
libkdcraw9
libgweather1
libkexiv2-9
libxcb-render-util0
ttf-sil-gentium
libgnome-window-settings1
libmicroblog4
libakonadi-kcal4
libevent-1.4-2
libswscale0
libcvaux2.1
ttf-droid
libksane0
libakonadi-kabc4
libabiword-2.8
pnm2ppa
liboobs-1-4
libkcalutils4
libmailtransport4
libtracker-client-0.10-0
libgck0
libedataserverui1.2-11
ttf-larabie-straight
libpolkit-gtk-1-0
libgucharmap7
libavformat52
chromium-browser-l10n
libkipi8
libkdb5-5
kerneloops
libboost-iostreams1.42.0
libgnome-bluetooth7
ttf-prociono
root@luke:/home/hbautista#
```

O podemos usar algunos argumentos:

```bash
root@luke:/home/hbautista# deborphan --guess-all
digikam-doc
libgnomekbd4
kdepimlibs-kio-plugins
librpcsecgss3
libchamplain-gtk-0.8-1
python-coherence
libcryptui0a
libslab0a
libkdcraw9
libcurl4-openssl-dev
libgweather1
libkexiv2-9
digikam-data
libxcb-render-util0
ttf-sil-gentium
libgnome-window-settings1
libgnome2-perl
gnome-desktop-environment
libmicroblog4
python-gdbm
conky
python-statgrab
libakonadi-kcal4
python-gdata
libevent-1.4-2
libswscale0
libcvaux2.1
ttf-droid
libksane0
libakonadi-kabc4
libabiword-2.8
python-gtksourceview2
pnm2ppa
kipi-plugins-common
liboobs-1-4
libkcalutils4
libmailtransport4
libtracker-client-0.10-0
python-gtkglext1
libgck0
libedataserverui1.2-11
ttf-larabie-straight
libpolkit-gtk-1-0
python-rdflib
libgucharmap7
libavformat52
chromium-browser-l10n
libkipi8
libkdb5-5
kerneloops
icedove-quotecolors
python-bugbuddy
libboost-iostreams1.42.0
libgnome-bluetooth7
ttf-prociono
root@luke:/home/hbautista#
```

Que como podrán darse cuenta, los paquetes también cambian. Hay varias formas de obtener listados de los paquetes huerfános, por ejemplo:

```bash
root@luke:/home/hbautista# dpkg -l $(deborphan --find-config)
Deseado=Desconocido/Instalar/Eliminar/Purgar/Retener
| Estado=No/Instalado/Config-files/Desempaquetado/Medio-conf/Medio-inst/espera-disparo/pendiente-disparo
|/ Err?=(ninguno)/Requiere-reinst (Estado,Err: mayúsc.=malo)
||/ Nombre                       Versión                     Descripción
+++-============================-============================-========================================================================
rc  capplets-data                1:2.30.1-3                   configuration applets for GNOME - data files
rc  checkgmail                   1.13+svn43-2                 alternative Gmail Notifier for Linux via Atom feeds
rc  gnome-netstatus-applet       2.28.1-1                     Network status applet for GNOME
rc  gwibber                      3.0.0.1-2                    Open source social networking client for GNOME (client)
rc  libbrasero-media0            2.30.3-3                     CD/DVD burning library for GNOME - runtime
rc  libechonest1.1               1.1.9-2                      Qt library for communicating with The Echo Nest platform
rc  libedata-book-1.2-9          3.0.3-2                      Backend library for evolution address books
rc  libedata-cal-1.2-11          3.0.3-2                      Backend library for evolution calendars
rc  libegroupwise1.2-13          3.0.3-2                      Client library for accessing groupwise POA through SOAP interface
rc  libepc-ui-1.0-2              0.3.11-1                     Easy Publish and Consume library - shared widget libraries
rc  libevince3                   2.32.0-1                     Document (PostScript, PDF) rendering library
rc  libgadu3                     1:1.11.0+r1184-2             Gadu-Gadu protocol library - runtime files
rc  libgcr-3-0                   3.0.3-2                      Library for Crypto UI related task - runtime
rc  libgdata11                   0.8.1-2                      Library for accessing GData webservices - shared libraries
rc  libgnome-desktop-3-0         3.0.2-2                      Utility library for loading .desktop files - runtime files
rc  libgnome-media0              2.30.0-1                     runtime libraries for the GNOME media utilities
rc  libgps19                     2.95-13.1                    Global Positioning System - library
rc  libgupnp-igd-1.0-3           0.1.11-1                     library to handle UPnP IGD port mapping
rc  libhunspell-1.2-0            1.2.14-4                     spell checker and morphological analyzer (shared library)
rc  libicu44                     4.4.2-2                      International Components for Unicode
rc  libimobiledevice1            1.0.6-3                      Library for communicating with the iPhone and iPod Touch
rc  libindicate-gtk2             0.5.0-3                      library for raising indicators via DBus - GTK+ bindings
rc  libmarblewidget11            4:4.6.5-1+b1                 Marble globe widget library
rc  libmatroska4                 1.2.0-1                      extensible open standard audio/video container format (shared library)
rc  libmetacity-private0         1:2.30.1-3                   library for the Metacity window manager
rc  libmozjs5d                   5.0-6                        Mozilla SpiderMonkey JavaScript library
rc  libmozjs6d                   6.0.2-1                      Mozilla SpiderMonkey JavaScript library
rc  libmozjs7d                   7.0.1-4                      Mozilla SpiderMonkey JavaScript library
rc  libnautilus-extension1       2.30.1-3                     libraries for nautilus components - runtime version
rc  libnm-glib2                  0.8.4.0-2                    network management framework (GLib shared library)
rc  libpostproc52                4:0.7.1-5                    Libav video postprocessing library
rc  libv8-3.4.14.21              3.4.14.21-5                  v8 JavaScript engine - runtime library
rc  libwebp0                     0.1.2-1                      Lossy compression of digital photographic images.
rc  libxalan2-java-gcj           2.7.1-5                      XSL Transformations (XSLT) processor in Java (native code)
rc  libxml-sax-perl              0.99+dfsg-1                  Perl module for using and building Perl SAX2 XML processors
rc  nvidia-kernel-3.0.0-1-686-pa 280.13.really.275.28-1+3.0.0 NVIDIA binary kernel module for Linux 3.0.0-1-686-pae
rc  tucan                        0.3.10-2                     Download and upload manager for 1-Click Hosters
root@luke:/home/hbautista#
```

El cual es un listado de los paquetes que no se están ocupando y de esta forma han quedado inservibles, si quisieramos desintalar ocuparíamos el siguiente comando:

```bash
root@luke:/home/hbautista# dpkg --purge $(deborphan)
(Leyendo la base de datos ... 202977 ficheros o directorios instalados actualmente.)
Desinstalando libgnomekbd4 ...
Purgando ficheros de configuración de libgnomekbd4 ...
Desinstalando kdepimlibs-kio-plugins ...
Desinstalando librpcsecgss3 ...
Purgando ficheros de configuración de librpcsecgss3 ...
Desinstalando libchamplain-gtk-0.8-1 ...
Purgando ficheros de configuración de libchamplain-gtk-0.8-1 ...
Desinstalando libcryptui0a ...
...
root@luke:/home/hbautista#
```

Ese comando sin preguntas ni nada, empieza la desinstalación de los paquetes, ahora bien si queremos que antes de desinstalar nos informe de que paquetes lo harán, podemos usar aptitude de la siguiente forma:

```bash
root@luke:/home/hbautista# aptitude purge `deborphan`
Se ELIMINARÁN los siguientes paquetes:            
  chromium-browser-l10n{p} fonts-droid{u} fonts-larabie-straight{u} fonts-prociono{u} kerneloops{p} kerneloops-applet{u} 
  kerneloops-daemon{u} libabiword-2.8{p} libakonadi-kabc4{p} libakonadi-kcal4{p} libavformat52{p} libboost-iostreams1.42.0{p} 
  libchamplain-0.8-1{p} libclutter-gtk-0.10-0{p} libcvaux2.1{p} libedataserverui1.2-11{p} libevent-1.4-2{p} libgck0{p} 
  libgnome-bluetooth7{p} libgnome-desktop-2-17{u} libgnome-window-settings1{p} libgucharmap7{p} libkcalutils4{p} libkdb5-5{p} 
  libkimap4{p} libkipi8{p} libksane0{p} libmailtransport4{p} libmicroblog4{p} liboobs-1-4{p} libpolkit-gtk-1-0{p} libswscale0{p} 
  libtracker-client-0.10-0{p} libtracker-sparql-0.10-0{u} pnm2ppa{p} printer-driver-pnm2ppa{u} seahorse-daemon{u} ttf-droid{p} 
  ttf-larabie-straight{p} ttf-prociono{p} 
0 paquetes actualizados, 0 nuevos instalados, 40 para eliminar y 0 sin actualizar.
Necesito descargar 0 B de ficheros. Después de desempaquetar se liberarán 45.0 MB.
¿Quiere continuar? [Y/n/?]
```

En resumen, si queremos ver los paquetes huérfanos:

```bash
root@luke:/home/hbautista# deborphan
```

o

```bash
root@luke:/home/hbautista# deborphan --guess-all
```

Si queremos eliminarlos:

```bash
root@luke:/home/hbautista# dpkg --purge $(deborphan)
```

Y si tenemos instalado **Synaptic** (instalador de paquetes en modo gráfico) podemos eliminar los paquetes huerfános de forma sencilla, para empezar ejecutamos synaptic:

[Synaptic

" data-image-caption="" data-large-file="/images/2012/Pant_Synaptic-1.png" class="aligncenter size-medium wp-image-821" title="Synaptic" src="/images/2012/Pant_Synaptic-1.png" alt="Synaptic" width="300" height="173" srcset="/images/2012/Pant_Synaptic-1.png 300w, /images/2012/Pant_Synaptic-1.png 768w, /images/2012/Pant_Synaptic-1.png 1024w, /images/2012/Pant_Synaptic-1.png 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" />][1]

Crearemos un nuevo filtro, así que hacemos clic en el menú Configuración -> Filtros

Synaptic Filtro 1

" data-image-caption="" data-large-file="/images/2012/Pant_Synaptic_Filtro1-1.png" class="aligncenter size-medium wp-image-822" src="/images/2012/Pant_Synaptic_Filtro1-1.png" alt="" width="300" height="171" srcset="/images/2012/Pant_Synaptic_Filtro1-1.png 300w, /images/2012/Pant_Synaptic_Filtro1-1.png 768w, /images/2012/Pant_Synaptic_Filtro1-1.png 841w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Clic en Nuevo, le asignamos un nombre (en mi caso Huérfanos) y de la lista de opciones, quitar todos y dejar solamente el que dice precisamente Huérfanos:

 

En la pantalla de Synaptic, clic en Filtros -> Huerfános

[Synaptic Filtro 3

" data-image-caption="" data-large-file="/images/2012/Pant_SynapticFiltros3-1.png" class="aligncenter size-medium wp-image-824" title="Synaptic Filtro 3" src="/images/2012/Pant_SynapticFiltros3-1.png" alt="Synaptic Filtro 3" width="300" height="173" srcset="/images/2012/Pant_SynapticFiltros3-1.png 300w, /images/2012/Pant_SynapticFiltros3-1.png 768w, /images/2012/Pant_SynapticFiltros3-1.png 1024w, /images/2012/Pant_SynapticFiltros3-1.png 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2]

Y es cuestión de seleccionar o marcar todos los que aparezcan para luego indicar que los elimine.

Synaptic Filtro 2

" data-image-caption="" data-large-file="/images/2012/Pant_SynapticFiltros2-1.png" class="aligncenter size-medium wp-image-823" src="/images/2012/Pant_SynapticFiltros2-1.png" alt="" width="300" height="171" srcset="/images/2012/Pant_SynapticFiltros2-1.png 300w, /images/2012/Pant_SynapticFiltros2-1.png 768w, /images/2012/Pant_SynapticFiltros2-1.png 841w" sizes="auto, (max-width: 300px) 100vw, 300px" />

 [1]: /images/2012/Pant_Synaptic-1.png
 [2]: /images/2012/Pant_SynapticFiltros3-1.png
