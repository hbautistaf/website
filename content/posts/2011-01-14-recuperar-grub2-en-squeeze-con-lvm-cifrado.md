---
title: Recuperar Grub2 en Squeeze con LVM cifrado
date: 2011-01-14 18:17:30+00:00
slug: recuperar-grub2-en-squeeze-con-lvm-cifrado
image: /images/2011/grub2.jpg
categories:
- Gnu/Linux
tags:
- Cifrado
- Cómos
- Debian
- Documentación
- Gnu/Linux
- Grub2
- Howto
- Luks
- LVM
- Squeeze
- Tips
aliases:
- /2011/01/14/recuperar-grub2-en-squeeze-con-lvm-cifrado/
- /linux/recuperar-grub2-en-squeeze-con-lvm-cifrado/
---

Ayer estaba viendo arreglar un pequeño detalle con **Grub2**, el grub.cfg de otra laptop y reinicié.. grave error :-/

Resulta que no me cargaba la imágen de fondo de **Grub2** y tampoco entraba a <a title="Debian Releases" href="http://debian.org/releases/" target="_blank" rel="noopener">Squeeze</a>, debido a que no correspondían los valores (obvio) con los de la Laptop Dell Vostro 1320 (_**Luke**_) que tengo.

No tiene mucho que reinstalé **Squeeze** en esa laptop, dejándolo con la versión de 64 bits y **LVM cifrado**, intenté con un live-cd de **Ubuntu** hacer la recuperación de grub sin resultado, pues no cargaba el volumen cifrado donde se encuentra el ejecutable de grub, solamente podía accesar a la partición de **/boot** donde se encuentra el kernel, initrd y la propia configuración de grub (**/boot/grub/grub.cfg**)

<!--more-->

Ya después de un buen rato de estar modificando manualmente grub.cfg y reiniciando varias veces el equipo y viendo que probablemente tendría que reinstalar (pensando lo peor) dí con la <a title="Rescatar sistema Debian" href="http://www.esdebian.org/foro/39018/rescatar-sistema-debian-lenny-eliminacion-etcinitd-error" target="_blank" rel="noopener">respuesta</a> en el foro de <a title="EsDebian.org" href="http://www.esdebian.org" target="_blank" rel="noopener">EsDebian</a>.

Básicamente indican que iniciando con el netinstall (es el que usé para instalar Debian Squeeze de 64 bits) usar el modo "rescue" para poder montar la partición cifrada y así poder hacer la recuperación.

Los pasos que finalmente me dieron la solución fueron:

Iniciar con el cd de **netinstall** en modo rescate (**rescue mode**)

Contestar las preguntas que se nos presentan hasta donde se nos pide la clave de encriptación del disco, escribirla y nos pide que escojamos la partición raíz del volumen LVM Indicamos que nos deje en la terminal

  * No monta la partición /boot por lo que habrá que hacerlo manualmente
  * 
```bash
mount /dev/sda1 /boot
```

  * Actualizar la configuración de grub
  * 
```bash
update-grub2
```

  * Se genera de nuevo el archivo grub.cfg en **/boot/grub/grub.cfg**

En mi caso y para evitar sorpresas ví el contenido de dicho archivo

** **

```bash
less /boot/grub/grub.cfg
```

 

Reiniciar el equipo Y con eso finalmente pude recuperar grub e iniciar normalmente el equipo.

Espero les sirva
