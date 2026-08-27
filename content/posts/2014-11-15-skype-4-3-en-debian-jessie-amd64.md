---
title: Skype 4.3 en Debian Jessie AMD64
date: 2014-11-16 04:39:42+00:00
slug: skype-4-3-en-debian-jessie-amd64
image: /images/2018/skype-linux-08.png
categories:
- Cómos
- Gnu/Linux
tags:
- AMD64
- Cómos
- Debian
- Gnu/Linux
- Howto
- Howtos
- Linux
- Skype
- Tips
aliases:
- /2014/11/15/skype-4-3-en-debian-jessie-amd64/
- /comos/skype-4-3-en-debian-jessie-amd64/
---

Resulta que en alguna de las actualizaciones de mi escritorio, la versión de skype que estaba usando dejó de funcionar. Como no recordaba como lo había hecho funcionar en un inicio, y recordando que al menos en Redhat, el rpm proporcionado por el sitio oficial, me dio un poco de lata, así que tienen una versión "dinámica".

  Luego entonces, fui a la web de Skype y me descargué la versión dinámica, como se muestra en las siguientes imágenes:

[

![Skype Linux 01](/images/2014/skype-linux-01-300x145.png)

][1]{.lightbox}[

![Skype Linux 02](/images/2014/skype-linux-02-300x119.png)

][2]{.lightbox}

  

![Skype Linux 03](/images/2014/skype-linux-03-300x100.png)

![Skype Linux 04](/images/2014/skype-linux-04-300x161.png)

  Una vez terminada la descarga, procedí a descomprimir el archivo, y ejecuté el binario:

 

hbautista@kenobi:~/Descargas/skype$ ./skype
./skype: error while loading shared libraries: libQtWebKit.so.4: cannot open shared object file: No such file or directory
hbautista@kenobi:~/Descargas/skype$</pre>

 

Y me encontré con ese error, el detalle es que el paquete que se necesita es: libqtwebkit4 y no se encuentra en los repositorios de la arquitectura de 64 bits, pero sí en la arquitectura i386. Por si no tienen habilitada la opción de multi-arquitectura en Debian, estos son los pasos a seguir:

root@kenobi:~# dpkg --add-architecture i386
root@kenobi:~# aptitude update</pre>

Una vez que se hayan actualizado los paquetes, procederemos a instalar el paquete requerido de la siguiente forma, lo cuál también nos mostrará todas las dependencias:

root@kenobi:~# aptitude install libqtwebkit4:i386
Se instalarán los siguiente paquetes NUEVOS:
gstreamer1.0-plugins-base:i386{a} libaudio2:i386{a} libavahi-client3:i386{a} libavahi-common-data:i386{a} libavahi-common3:i386{a} libcdparanoia0:i386{a}
libcups2:i386{a} libfontconfig1:i386{a} libgssapi-krb5-2:i386{a} libgstreamer-plugins-base1.0-0:i386{a} libgstreamer1.0-0:i386{a} libk5crypto3:i386{a}
libkeyutils1:i386{a} libkrb5-3:i386{a} libkrb5support0:i386{a} libmng1:i386{a} libqt4-opengl:i386{a} libqt4-xmlpatterns:i386{a} libqtgui4:i386{a}
libqtwebkit4:i386 libsqlite3-0:i386{a} libxt6:i386{a}
0 paquetes actualizados, 22 nuevos instalados, 0 para eliminar y 29 sin actualizar.
Necesito descargar 22.5 MB de ficheros. Después de desempaquetar se usarán 72.9 MB.
¿Quiere continuar? [Y/n/?] y</pre>

  

![Skype Linux 05](/images/2014/skype-linux-05-300x154.png)

En mi caso, también me descargué el <a title="Descargar Skype" href="http://download.skype.com/linux/skype-debian_4.3.0.37-1_i386.deb" target="_blank" rel="noopener">paquete deb</a>, así que procedí a instalarlo con dpkg:

root@kenobi:~# dpkg -i /home/hbautista/Descargas/skype
skype/                            skype-debian_4.3.0.37-1_i386.deb
root@kenobi:~# dpkg -i /home/hbautista/Descargas/skype-debian_4.3.0.37-1_i386.deb
Seleccionando el paquete skype previamente no seleccionado.
(Leyendo la base de datos ... 252325 ficheros o directorios instalados actualmente.)
Preparing to unpack .../skype-debian_4.3.0.37-1_i386.deb ...
Unpacking skype (4.3.0.37-1) ...
Configurando skype (4.3.0.37-1) ...
Processing triggers for dbus (1.8.8-2) ...
Processing triggers for mime-support (3.57) ...
Processing triggers for desktop-file-utils (0.22-1) ...
Processing triggers for hicolor-icon-theme (0.13-1) ...
root@kenobi:~#</pre>

[

![Skype Linux 06](/images/2014/skype-linux-06-300x93.png)

][3]{.lightbox}Ya nada más nos queda ejecutarlo como un usuario normal

  

![Skype Linux 09](/images/2014/skype-linux-09-300x205.png)

 

![](/images/2018/skype-linux-10.png)

  Y con eso se resuelve dicho problema

  Fuente: <a title="Linux Questions" href="http://www.linuxquestions.org/questions/debian-26/installing-skype-4-1-0-on-amd64-architecture-4175437925/" target="_blank" rel="noopener">LinuxQuestions</a>

 [1]: /images/2014/skype-linux-01.png
 [2]: /images/2014/skype-linux-02.png
 [3]: /images/2014/skype-linux-06.png
