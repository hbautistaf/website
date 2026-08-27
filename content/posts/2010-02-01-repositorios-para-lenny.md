---
title: Repositorios para Lenny
date: 2010-02-01 17:58:46+00:00
slug: repositorios-para-lenny
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Gnu/Linux
- Tips
aliases:
- /2010/02/01/repositorios-para-lenny/
- /comos/repositorios-para-lenny/
---

Sucede que después de usar <a title="Debian" href="http://debian.org" target="_blank">Debian</a>, <a title="Ubuntu" href="http://ubuntu.com" target="_blank">Ubuntu </a>y <a title="OpenSuse" href="http://es.opensuse.org/Bienvenidos_a_openSUSE.org" target="_blank">OpenSuse</a> no cabe duda que uno es de hábitos y costumbres y finalmente he regresado con Debian Gnu/Linux

Usé en esta portátil (<a title="HP Pavilion" href="http://picasaweb.google.com/lh/photo/a7xnUS36VmcZkeCdXzSbzg?feat=embedwebsite" target="_blank">Bombadil</a>) los 3 sabores y por diversas razones cada uno estuvo bien aunque con algunos detalles, así­ que finalmente decidí­ quedarme en Lenny, al menos hasta que Squeeze esté más depurada

Así­ que las razones de peso por las que finalmente estoy con <a title="Debian" href="http://www.debian.org/releases/stable/" target="_blank">Debian Gnu/Linux Lenny</a> son a grandes rasgos los siguientes:

  1. TODO funciona bien recién instalado, a excepción de la red inalámbrica
  2. Hay suficientes programas para lo que necesito
  3. No hay cuelgues en programas
  4. Hay repositorios no oficiales para programas que no estén en los oficiales
  5. La inalámbrica tiene solución, ya sea usando madwifi o bien actualizando a una versión del kernel más nueva

Por lo mismo, debido a que estuve del tingo al tango pues ahora que está funcionando todo como debiera a excepción de gwibber, dejo los repositorios que actualmente tengo en uso y que me proporciona (hasta ahorita) todo lo que necesito.

```bash
#Repositorios oficiales de Debian
deb http://mmc.geofisica.unam.mx/debian/ lenny main
#deb-src http://mmc.geofisica.unam.mx/debian/ lenny main
deb http://ftp.mx.debian.org/debian/ lenny main
deb http://ftp.rediris.es/debian lenny main contrib non-free
#deb-src http://ftp.mx.debian.org/debian/ lenny main
deb http://security.debian.org/ lenny/updates main
#deb-src http://security.debian.org/ lenny/updates main
#Otros repositorios adicionales
#Debian Multimedia
#deb http://www.debian-multimedia.org lenny main
deb http://www.debian-multimedia.org lenny main
# Google testing repository
#deb http://dl.google.com/linux/deb/ testing non-free
#Opera for Debian Lenny
deb http://deb.opera.com/opera/ lenny non-free
#deb http://deb.opera.com/opera/ lenny non-free
# Skype
deb http://download.skype.com/linux/repos/debian/ stable non-free
## Thí¨mes du projet bisigi
deb http://ppa.launchpad.net/bisigi/ppa/ubuntu jaunty main
```

Espero que sea entendible y los que tengan el **#** al inicio de la lí­nea, pues no serán tomados en cuenta.

Después de modificar tus **sources.list** (que se encuentra el archivo en **/etc/apt/**) tendrás que hacer lo siguiente:

Descargar –> **http://www.debian-multimedia.org/pool/main/d/debian-multimedia-keyring/debian-multimedia-keyring\_2008.10.16\_all.deb**  
Y luego lo instalamos:

```bash
dpkg -i debian-multimedia-keyring_2008.10.16_all.deb
```

Luego añadimos las claves de los demás repositorios:

```bash
gpg --keyserver hkp://keyserver.ubuntu.com:11371 --recv-key 881574DE && gpg -a --export 881574DE | apt-key add -
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
gpg --keyserver subkeys.pgp.net --recv-key 6A423791 && gpg --fingerprint 6A423791 && gpg --armor --export  6A423791| apt-key add -
```

Ahora paso a explicar un poco:

El primero es para el repositorio <a title="Debian Multimedia" href="http://debian-multimedia.org/" target="_blank">debian-multimedia</a>, el segundo es para el repositorio de <a title="Bisigi project" href="http://www.bisigi-project.org/?lang=en" target="_blank">launchpad</a> y el tercero es el de <a title="Opera" href="http://www.opera.com/" target="_blank">Opera</a>. Lo anterior es para que no tengamos problemas a la hora de actualizar la lista de paquetes de Debian 🙂

En **Debian-Multimedia** se encontrarán con los codecs para ver cualquier tipo de videos, poder leer dvd's, además del MPlayer, Flash y demás.

El de **Launchpad** es porque en ese repositorio nada más hay unos temas muy bueno y que me gustaron (<http://www.bisigi-project.org/>)

El tercero es para **Google Picasa**

Y finalmente el de **Opera** es para poder instalar el navegador Opera en nuestro Debian

Una vez hecho los cambios en nuestro **sources.list** y añadidos las claves de los repositorios, nos queda actualizar la lista de paquetes que podemos instalar y eso lo hacemos con:

```bash
aptitude update
```

Bueno lo que resta es instalar aquellos paquetes que nos interesen. En mi caso este es lo que yo he instalado una vez hecho los cambios anteriores

```bash
aptitude install iceweasel-downloadstatusbar iceweasel-downthemall iceweasel-greasemonkey wallpaper-tray gftp xchat phatch conky startupmanager aircrack-ng nmap sun-java6-jre flashplayer-mozilla w32codecs mplayer libdvdcss2 grub-splashimages gnome-art ntfs-3g mesa-utils k3b-i18n liferea opera glabels p7zip unrar gnome-extra-icons nautilus-actions nautilus-gksu nautilus-open-terminal nautilus-image-converter apache2 mysql-server mysql-admin php5 php5-mysql chameleon-cursor-theme comixcursors crystalcursors xcursor-themes amarok amarok-utils phpmyadmin ttf-bitstream-vera ttf-dejavu ttf-marvosym ttf-mscorefonts-installer skype metacity-themes murrine-themes pidgin-themes pidgin-plugin-pack tropical-theme dfo mc
```

Se va a tardar un buen rato para instalar todo aquello, pero una vez que hayamos terminado hay que remover el paquete **swfdec-mozilla** para poder usar el **flashplayer**

```bash
aptitude remove swfdec-mozilla
```

El detalle es que me pide desinstalar el paquete **gnome** que desinstala otras cosas, apunté los paquetes que desinstaló y los vuelvo a instalar

```bash
apitude install bluez-gnome gnome-spell gnome-themes-extras gnome-vfs-obexftp libgda3-3 libgda3-common libgdl-1-0 libgdl-1-common libgksu1.2-0 libgksuui1.0-1 libopenobex1 python-4suite-xml python-eggtrayicon python-gnome2-extras python-notify rhythmbox serpentine system-config-printer transmission-common transmission-gtk
```

Finalmente queda definir que usaremos **Sun-Java** en lugar de **GCJ**

```bash
root_at_bombadil:/home/hbautista# update-alternatives --config java
Hay 3 alternativas que proveen `java'.
Selección     Alternativa
<hr noshade="noshade" size="1" />
1    /usr/bin/gij-4.3
+        2    /usr/lib/jvm/java-gcj/jre/bin/java
*         3    /usr/lib/jvm/java-6-sun/jre/bin/java
Pulse <Intro> para mantener el valor por omisión [*] o pulse un número de selección: 3
Utilizando `/usr/lib/jvm/java-6-sun/jre/bin/java' para proveer `java'.
root_at_bombadil:/home/hbautista#
```

Ahhh…. como mencioné al principio del artí­culo hay que actualizar el <a title="Debian Kernel" href="http://wiki.debian.org/DebianKernel" target="_blank">kernel</a> y hay dos formas:

La primera consiste en añadir otra clave de repositorio

```bash
wget -q -O - http://kernel-archive.buildserver.net/key-2009 | apt-key add -
```

Descomentar lo de las últimas lí­neas del sources.list quedando así­

```bash
#para el kernel
deb http://kernel-archive.buildserver.net/debian-kernel lenny main
#deb http://ftp.de.debian.org/debian squeeze main
```

Actualizar la lista de paquetes:

```bash
# aptitude update
```

Y finalmente instalar el kernel

```bash
root_at_bombadil:~# aptitude install linux-image-2.6.30-1-686
```

El detalle es que el servidor _kernel-archive.buildserver.net_ **NO** está disponible, caí­do o que se yo ton's nos vamos a hacerlo de la segunda forma:

Descomentar lo de las últimas lí­neas del sources.list quedando así­

```bash
#para el kernel
#deb http://kernel-archive.buildserver.net/debian-kernel lenny main
deb http://ftp.de.debian.org/debian squeeze main
```

Con esto indicamos que usaremos un repositorio de **Squeeze**, ahí­ ya tienen el <a title="Debian Kernel" href="http://packages.qa.debian.org/l/linux-2.6/news/20100122T163921Z.html" target="_blank">kernel actualizado</a>. Igualmente hay que actualizar la lista de paquetes.

```bash
aptitude update
```

Y finalmente instalar el kernel

```bash
root_at_bombadil:~# aptitude install linux-image-2.6.32-5-686
```

Con esto habremos de tener instalado el kernel 2.6.30-1, pero hay que volver a comentar para que quedemos con Lenny en lugar de Squeeze:

```bash
#para el kernel
#deb http://kernel-archive.buildserver.net/debian-kernel lenny main
#deb http://ftp.de.debian.org/debian squeeze main
```

Solamente queda reiniciar y tendremos funcionando nuestro Chip Atheros muy bien

Si se preguntan porqué escogí­ actualizar el kernel, es porque con madwifi no tengo modo monitor en el chip y no puedo hacer cosas como esta:

```bash
root_at_bombadil:~# aircrack-ng infi733-06.cap
KEY FOUND! [ 96:15:79:32:76 ]
```

Si tienen comentarios o sugerencias, pues serán bienvenidas 😀
