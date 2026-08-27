---
title: Broadcom en Saori
date: 2009-11-17 18:21:31+00:00
slug: broadcom-en-saori
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Broadcom
- Debian
- Saori
aliases:
- /2009/11/17/broadcom-en-saori/
- /comos/broadcom-en-saori/
---

Pues resulta que la semana pasada y viendo que le voy a poner Debian Squeeze (Amd64) a Saori, decidí verificar que todo va a funcionar como espero que lo haga, así que debido a falta de tiempo, agarré un live-cd de Ubuntu 9.10 para corrobar el hardware que tiene 🙂

El detalle vino cuando vi que trae una tarjeta de red inalámbrica Broadcom :S y pues he leído que dan algo de lata en linux y así 🙁

<!--more-->

<a title="Randy" href="http://www.apuralemijo.com" target="_blank">Randy</a> me pasó un enlace debido a que él también tiene esa tarjeta en su lap para verficar si podría poner o no en modo monitor dicha tarjeta (con fines didácticos :P)

Y se reduce a lo siguiente, en la terminal escribir el siguiente comando

> lspci -nn

Y si aparece en el ID del chipset de su tarjeta lo siguiente, básicamente ya se la pellizcaron 🙁 (como es mi caso y el de Randy 🙁 )

> PCI ID 14e4:4315

Sip, en <a title="Aircrack Broadcom" href="http://www.aircrack-ng.org/doku.php?id=broadcom" target="_blank">ésta página</a> dice textualmente lo siguiente "Most broadcom cards are supported EXCEPT the following:", oséase que ya nos fregaron, porque el modo monitor NO se puede con ese chipset específico 🙁

¿Que opciones quedan? sinceramente no muchas, más que esperar que en un futuro sea corregido, intentar aplicar un par de parches que se mencionan ahí. También queda la posibilidad de adquirir una tarjeta inalámbrica usb, pcmcia card externa o lo que intentaré (espero que hoy) hacer XD.

Tengo otra lap (que no es mía :P) que trae una tarjeta inalámbrica Atheros (que sí soporta el modo monitor) y ya le quité dicha tarjeta (solamente desmontar una tapa y quitar dos tornillos) y que tiene por S.O. hasefroch y que no se le va a poner Gnu/Linux. Ahora bien, destaparé a Saori, y le quitaré (si se puede de forma fácil) la tarjeta de red inalámbrica hija de puta broadcom que tiene ¬¬ y la sustituiré por la maravillosamente chingona Atheros 😛

Espero que sean de entradas parecidas, porque la lap del chip Atheros es una Compaq :P, si funciona lo publicaré en la noche o mañana 🙂

Si no funcionara 🙁 ¬¬ creo que tendrá Saori sus días contados :@

Ahi luego escribo como me fue 😉
