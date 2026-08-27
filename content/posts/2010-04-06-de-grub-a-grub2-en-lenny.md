---
title: De Grub a  Grub2 en Lenny
date: 2010-04-06 16:43:48+00:00
slug: de-grub-a-grub2-en-lenny
image: /images/2011/grub2.jpg
categories:
- Gnu/Linux
aliases:
- /2010/04/06/de-grub-a-grub2-en-lenny/
- /linux/de-grub-a-grub2-en-lenny/
---

Debido a que **Grub 1** ha sido "descontinuada" aunque muchas distribuciones (incluída Debian) lo siguen usando:

Tomado de "<a title="Bit Negro" href="http://bitnegro.blogspot.com/2008/03/migrando-grub-2.html" target="_blank" rel="noopener">El Bit Negro</a>"

> Para el que no lo conoce, GRUB es el mnemónico de [GRand Unified Bootloader][1]. Un boot loader, o cargador de arranque, es el primer programa que se ejecuta cuando la computadora arranca (salvando la secuencia de arranque en ROM). El boot loader es responsable de cargar y transferir el control al núcleo, o kernel, del sistema operativo. El kernel, luego, incializa el resto del sistema operativo.
> 
> GRUB es, para aquellos que tenemos Linux, el "menú que aparece en la pantalla" y que nos permite seleccionar el sistema operativo, o la versión de kernel, que vamos a iniciar. Otro gestor conocido y que muchos hemos utilizado alguna vez, es [LILO][2].
> 
> La versión 1 de GRUB, ahora denominada GRUB Legacy, es la que utiliza la mayoría de las distribuciones de GNU/Linux actuales y ya no está siendo desarrollada activamente por la comunidad; no se están añadiendo nuevas funcionalidades y sólo se están aplicando los parches necesarios para mantenerlo al día mientras la versión 2 se estabiliza. De ahí la solicitud de Otavio en la lista de mails.

<!--more-->

  
Ok, pasemos a la acción 😉 primeramente instalamos lo necesario

```bash
root@luke:/home/hbautista# aptitude install grub2 grub2-splashimages os-prober
```

Reiniciamos como en este video y veremos los cambios:

Si podemos ver y entrar usando **Grub2** sin ningún mensaje de error, entonces procedemos a ejecutar lo siguiente para finalizar:

```bash
root@luke:/home/hbautista# upgrade-from-grub-legacy 

Installing GRUB to Master Boot Record of your first hard drive ...

Installation finished. No error reported.
This is the contents of the device map /boot/grub/device.map.
Check if this is correct or not. If any of the lines is incorrect,
fix it and re-run the script `grub-install'.

(hd0)   /dev/sda

GRUB Legacy has been removed, but its configuration files have been preserved,
since this script cannot determine if they contain valuable information.  If
you would like to remove the configuration files as well, use the following
command:

  rm -f /boot/grub/menu.lst*

root@luke:/home/hbautista#
```

 

Y eso es todo, faltaría reiniciar y **Grub1** habrá desaparecido 😉

 [1]: http://es.wikipedia.org/wiki/GRUB
 [2]: http://en.wikipedia.org/wiki/LILO_%28boot_loader%29
