---
title: Formatear NTFS en Debian
date: 2010-10-07 14:59:06+00:00
slug: formatear-ntfs-en-debian
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Debian
- Gnu
- GParted
- Linux
- Ntfs
- Squeeze
- TestDisk
- Tips
aliases:
- /2010/10/07/formatear-ntfs-en-debian/
- /comos/formatear-ntfs-en-debian/
---

Resulta que este inicio de semana, tengo un disco duro externo que me dieron en el trabajo y se usa principalmente para hacer respaldos y esas cosas.

Pues bien, algo pasó que simplemente se perdió una partición conteniendo información importante y valiosa que debía ser rescatada, <a title="TestDisk" href="http://www.cgsecurity.org/wiki/TestDisk" target="_blank">TestDisk</a> finalmente me ayudó a resolver parte del problema.[TestDisk

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2010/10/Testdisklogo_clear_100-1.png?fit=100%2C100&ssl=1" class="alignright size-full wp-image-350" title="TestDisk" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2010/10/Testdisklogo_clear_100-1.png?resize=100%2C100&ssl=1" alt="TestDisk" width="100" height="100" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2010/10/Testdisklogo_clear_100-1.png?w=100&ssl=1 100w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2010/10/Testdisklogo_clear_100-1.png?resize=60%2C60&ssl=1 60w" sizes="auto, (max-width: 100px) 100vw, 100px" />][1]

El caso es que finalmente tuve perdida de información debido a un error mío y pues ni modos. No sé exactamente que se perdió ni si era importante o no. La cuestión es que necesitamos usar ese disco duro externo que es de 250GB.

<!--more-->Entonces lo que hice fue eliminar las particiones usando GParted y volverlas a crear en el siguiente orden: 50% en una partición primaria del tipo NTFS y 50% de una partición lógica en Fat32.

Pero me topé con el pequeño detalle que no podía crear la partición en NTFS porque no tenía soporte completo, en mi caso instalé los siguientes paquetes y asunto resuelto:

```bash
root@luke:/home/hbautista# aptitude install ntfs-config ntfsprogs fuse-utils
```

Basta con volver a entrar en GParted y crear las particiones tal y como mencioné antes y listo.

En el trabajo necesitamos de ese disco duro con ese tipo de particiones.

 [1]: /images/2010/Testdisklogo_clear_100-1.png
