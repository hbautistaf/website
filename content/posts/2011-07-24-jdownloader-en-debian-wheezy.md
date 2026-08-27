---
title: JDownloader en Debian Wheezy
date: 2011-07-24 06:36:17+00:00
slug: jdownloader-en-debian-wheezy
image: /images/2011/Pant_jdownloader3-1.png
categories:
- Cómos
- Gnu/Linux
tags:
- Cómos
- Debian
- Gnu/Linux
- Howto
- JDownloader
- Wheezy
aliases:
- /2011/07/24/jdownloader-en-debian-wheezy/
- /comos/jdownloader-en-debian-wheezy/
---

[Logo JDownloader

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/jdownloader-1.png?fit=150%2C150&ssl=1" class="alignleft size-full wp-image-671" title="Logo JDownloader" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/jdownloader-1.png?resize=150%2C150&ssl=1" alt="Logo JDownloader" width="150" height="150" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/jdownloader-1.png?w=150&ssl=1 150w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/jdownloader-1.png?resize=60%2C60&ssl=1 60w" sizes="auto, (max-width: 150px) 100vw, 150px" />][1]

Resulta que durante mi estancia en Campus Party México 2011 actualicé mi Debian Squeeze a la versión de pruebas Debian Wheezy y aunque aún me falta ver si la tarjeta inalámbrica está funcionando de forma normal y correcta, me acabo de percatar que <a title="JDownloader" href="http://jdownloader.org/" target="_blank" rel="noopener">JDownloader</a> simplemente dejó de funcionar.

 

Había instalado **JDownloader** bajando el .deb de la página oficial y cuando lo ejecutaba se quedaba "cargando" la aplicación pero simplemente no terminaba de hacerlo, así que decidí borrar los archivos de configuración que se habían creado y eliminé el paquete.

 

Para que se actualizara de forma periódica añadí un repositorio <a title="Launchpad JDownloader" href="https://launchpad.net/~jd-team/+archive/jdownloader" target="_blank" rel="noopener">PPA de Launchpad</a> ya que no se encuentra en los repositorios de Wheezy y lo hice de forma manual, añadí en mi **/etc/apt/sources.list** lo siguiente:

```bash
#### JDowloader http://jdownloader.org/ (Repositorio ubuntu)
deb http://ppa.launchpad.net/jd-team/jdownloader/ubuntu natty main
```

Y luego de eso hay que añadir la firma del repositorio con el siguiente comando en una terminal:

```bash
root@luke:/home/hbautista# apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 6A68F637
Executing: gpg --ignore-time-conflict --no-options --no-default-keyring --secret-keyring /etc/apt/secring.gpg --trustdb-name /etc/apt/trustdb.gpg --keyring /etc/apt/trusted.gpg --primary-keyring /etc/apt/trusted.gpg --keyserver keyserver.ubuntu.com --recv-keys 6A68F637
gpg: solicitando clave 6A68F637 de hkp servidor keyserver.ubuntu.com
gpg: clave 6A68F637: clave pública "Launchpad JDownloader PPA" importada
gpg: no se encuentran claves absolutamente fiables
gpg: Cantidad total procesada: 1
gpg: importadas: 1 (RSA: 1)
root@luke:/home/hbautista#
```

Actualizamos los repositorios:

```bash
root@luke:/home/hbautista# aptitude update
Obj http://ftp.us.debian.org testing InRelease
...
...
Descargados 46.0 kB en 39seg. (1169 B/s).
Estado actual: 6259 nuevos [+1].
root@luke:/home/hbautista#
```

Y finalmente instalamos la aplicación:

```bash
root@luke:/home/hbautista# aptitude install jdownloader
Se instalarán los siguiente paquetes NUEVOS:
jdownloader
0 paquetes actualizados, 1 nuevos instalados, 0 para eliminar y 103 sin actualizar.
...
...
Configurando jdownloader (0.2-0jd1~natty) ...
root@luke:/home/hbautista#
```

Pero cuando lo ejecuté me encontré con un error :-/

> Caused by: java.io.FileNotFoundException: /usr/lib/libnss3.so  
> at sun.security.pkcs11.Secmod.initialize(Secmod.java:186)  
> at sun.security.pkcs11.SunPKCS11.<init>(SunPKCS11.java:197)  
> … 18 more  
> ERROR Could not initialize NSS

Y buscando me encontré con la respuesta gracias a <a title="Unnaki.com" href="http://www.unnaki.com/libnss3-so-error-on-debian-wheezy/" target="_blank" rel="noopener">este genial post</a> y que básicamente hay que hacer lo siguiente:

Editar **/etc/java-6-openjdk/security/nss.cfg** que contiene lo siguiente:

```bash
name = NSS
#nssLibraryDirectory = /usr/lib
nssDbMode = noDb
attributes = compatibility
```

```bash
root@luke:/home/hbautista# nano /etc/java-6-openjdk/security/nss.cfg
```

Y debemos dejarlo así si tenemos Debian Wheezy de 32 bits

```bash
name = NSS
#nssLibraryDirectory = /usr/lib
nssLibraryDirectory = /usr/lib/i386-linux-gnu
nssDbMode = noDb
attributes = compatibility
```

Y así si tenemos Debian Wheezy de 64 bits como es mi caso:

```bash
name = NSS
#nssLibraryDirectory = /usr/lib
nssLibraryDirectory = /usr/lib/x86_64-linux-gnu
nssDbMode = noDb
attributes = compatibility
```

Y después de eso ejecutamos JDownloader y empieza a actualizarse y después de eso nos muestra que debemos configurar el idioma y el directorio de descargas:

[Configurando JDownloader

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader-1.png?fit=557%2C400&ssl=1" class="aligncenter size-medium wp-image-672" title="Configurando JDownloader" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader-1.png?resize=300%2C215&ssl=1" alt="Configurando JDownloader" width="300" height="215" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader-1.png?resize=300%2C215&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader-1.png?w=557&ssl=1 557w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2]

Y luego nos pregunta si queremos instalar la extensión para Firefox, en mi caso le puse que no

[Configurando JDownloader 2

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader2-1.png?fit=557%2C400&ssl=1" class="aligncenter size-medium wp-image-673" title="Configurando JDownloader 2" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader2-1.png?resize=300%2C215&ssl=1" alt="Configurando JDownloader 2" width="300" height="215" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader2-1.png?resize=300%2C215&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader2-1.png?w=557&ssl=1 557w" sizes="auto, (max-width: 300px) 100vw, 300px" />][3]

Finalmente nos deja ya con la aplicación funcionando

[Configurando JDownloader 3

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader3-1.png?fit=648%2C485&ssl=1" class="aligncenter size-medium wp-image-674" title="Configurando JDownloader 3" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader3-1.png?resize=300%2C224&ssl=1" alt="Configurando JDownloader 3" width="300" height="224" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader3-1.png?resize=300%2C224&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader3-1.png?resize=768%2C574&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/07/Pant_jdownloader3-1.png?w=797&ssl=1 797w" sizes="auto, (max-width: 300px) 100vw, 300px" />][4]

Si alguien tiene un problema similar, espero que esto les sirva

 [1]: /images/2011/jdownloader-1.png
 [2]: /images/2011/Pant_jdownloader-1.png
 [3]: /images/2011/Pant_jdownloader2-1.png
 [4]: /images/2011/Pant_jdownloader3-1.png
