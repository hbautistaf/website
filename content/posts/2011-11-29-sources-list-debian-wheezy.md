---
title: Sources.list Debian Wheezy
date: 2011-11-30 04:21:20+00:00
slug: sources-list-debian-wheezy
image: /images/2011/Pant_sources_wheezy-1.png
categories:
- Gnu/Linux
tags:
- Cómos
- Gnu/Linux
- Howto
- Howtos
- Sources.list
- Tips
- Wheezy
aliases:
- /2011/11/29/sources-list-debian-wheezy/
- /linux/sources-list-debian-wheezy/
---

Actualmente me encuentro usando Debian Wheezy (rama testing/pruebas) y este es mi actual sources.list

Sources.list Wheezy

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/11/Pant_sources_wheezy-1.png?fit=648%2C373&ssl=1" class="aligncenter size-medium wp-image-790" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/11/Pant_sources_wheezy-1.png?resize=300%2C173&ssl=1" alt="" width="300" height="173" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/11/Pant_sources_wheezy-1.png?resize=300%2C173&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/11/Pant_sources_wheezy-1.png?resize=768%2C443&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/11/Pant_sources_wheezy-1.png?resize=1024%2C590&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/11/Pant_sources_wheezy-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Ahora bien, vamos a editar nuestro sources.list

root@luke:/home/hbautista# nano /etc/apt/sources.list</pre>

Y escribimos el siguiente contenido:

```bash
deb http://ftp.us.debian.org/debian/ wheezy main contrib non-free
#deb-src http://ftp.us.debian.org/debian/ wheezy main

deb http://security.debian.org/ wheezy/updates main
#deb-src http://security.debian.org/ wheezy/updates main

deb http://mmc.geofisica.unam.mx/debian/ wheezy main contrib non-free
# deb-src http://mmc.geofisica.unam.mx/debian/ squeeze main

deb http://ftp.mx.debian.org/debian/ squeeze main
deb http://ftp.rediris.es/debian squeeze main contrib non-free
# deb-src http://ftp.mx.debian.org/debian/ squeeze main

# Google software repository
# deb http://dl.google.com/linux/deb/ stable non-free

#Debian Multimedia
deb http://www.debian-multimedia.org wheezy main non-free

# Google testing repository
#deb http://dl.google.com/linux/deb/ testing non-free
#deb http://dl.google.com/linux/deb/ stable non-free

#Opera for Debian Lenny
deb http://deb.opera.com/opera/ wheezy non-free

#### JDowloader http://jdownloader.org/ (Repositorio ubuntu)
deb http://ppa.launchpad.net/jd-team/jdownloader/ubuntu natty main
```

Antes de actualizar debemos realizar lo siguiente para obtener las firmas del repositorio de Opera:

```bash
root@luke:/home/hbautista# wget -O - http://deb.opera.com/archive.key | apt-key add -
```

Y también esto para la firma de Google Testing Repository:

```bash
root@luke:/home/hbautista# wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
```

Y bueno, queda instalar Debian Multimedia Keyring

```bash
root@luke:/home/hbautista# aptitude install debian-multimedia-keyring
```

Y también la llave de Launchpad para el JDownloader:

```bash
root@luke:/home/hbautista# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A68F637
```

Ahora si, actualizamos nuestro sources.list

```bash
root@luke:/home/hbautista# aptitude update
```

Y ya estaremos en posibilidades de tener los paquetes actualizados y poder instalar algunos que no se encuentran en Debian.
