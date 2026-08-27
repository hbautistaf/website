---
title: Recuperando Grub2
date: 2010-03-06 19:07:47+00:00
slug: recuperando-grub2
categories:
- Gnu/Linux
tags:
- Cómos
- Gnu/Linux
- Tips
- Ubuntu
aliases:
- /2010/03/06/recuperando-grub2/
- /linux/recuperando-grub2/
---

Ya tengo un <a title="Recuperando Grub" href="http://blog.hbautista.com/linux/recuperando-grub/" target="_blank">artículo para poder recuperar GRUB</a> en este blog, pero está orientado al Grub 1.x y hoy tuve una laptop con una instalación de Ubuntu 9.10 y que al reinstalar el Hasefroch nomás se perdió y pues aunque la persona estuvo tratando de poder recuperar Grub, la mayoría de los enlaces que consultó y aplicó nomás no le funcionaron porque estaban enfocados a esa versión 1.x, pero Ubuntu 9.10, Debian Squeeze y probablemente más distribuciones están usando actualmente GRUB 2.x y obviamente la forma de funcionar cambió. 🙂

<!--more-->Así que vamos a ver la forma rápida de cómo hacer para recuperar Grub2 😀

Al igual que en el <a title="Recuperando Grub" href="http://blog.hbautista.com/linux/recuperando-grub/" target="_blank">artículo anterior</a>, precisaremos de una distribución Live, como Ubuntu o la que ustedes prefieran e iniciar desde ahí.

Como menciono lo que se hizo fue iniciar con el cd de Ubuntu, escoger el idioma español y la opción de “Probar sin instalar” (o algo así)

Una vez dentro e iniciado ubuntu hacemos clic en “Lugares – Equipo”

Esto abrirá una ventana de Nautilus que nos indica todas las particiones que encuentra SIN montarlas. En el caso de la pc en cuestión encontró 2 (dos) partciones y las etiquetó como disk y disk2. Cuando se instaló se crearon dos particiones raíz (/) y home (/home). Al darle clic sobre el ícono de disk, éste se monta y nos muestra el contenido que es típico de la partición raíz (/).

Ahora abrimos una terminal haciendo clic en “Aplicaciones – Accesorios – Terminal”

Nos aseguramos en donde está montada la partición y cúal es:

df -h

/dev/sda1 43G 2.0G 8G 2% /media/disk

Ok, veremos primero la talacha y luego explico que hicimos :-p

Como vemos la partición ya está montada en /media/disk lo que necesitamos es que los dispositivos también sean cargados ya que usaremos un entorno <a title="Guia Ubuntu" href="http://doc.ubuntu-es.org/Restaurar_Grub" target="_blank">chroot</a>. 🙂

> sudo su

> mount –bind /dev /mnt/dev

Y ejecuta el comando chroot de forma que accedemos como root al sistema de archivos de nuestro Ubuntu:

chroot /media/disk

Por último cargamos el Grub en el MBR ejecutando el siguiente comando:

> grub-install –recheck /dev/sda

(sda lo debemos substituir por el disco duro que utilizamos para arrancar los sistemas operativos, casi siempre es sda. Ojo!! no poner el número de partición, solo sda)

Reiniciamos y cuando vuelva a arrancar ubuntu (no el del live-cd), podemos ajustar en el menú del grub manualmente para que aparezca en el menú de arranque el nuevo sistema operativo que nos borró el MBR, o dejar que lo haga el automáticamente con el siguiente comando:

> $ sudo update-grub2

Y eso es todo 😀
