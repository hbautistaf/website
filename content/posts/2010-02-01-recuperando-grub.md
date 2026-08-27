---
title: Recuperando Grub
date: 2010-02-01 16:30:52+00:00
slug: recuperando-grub
categories:
- Cómos
- Gnu/Linux
tags:
- Cómos
- Gnu/Linux
- Ubuntu
aliases:
- /2010/02/01/recuperando-grub/
- /comos/recuperando-grub/
---

Resulta que un compañero de trabajo tenía arranque dual en su computadora, pero me parece que tuvo que reinstalar por un problema que tuvo y pues como se podrán imaginar, Grub se perdió en los 0 y 1. 🙁

Así que intentó por varios medios y consejos que vió en la web para recuperarlo, pero por alguna razón no conseguía lograrlo. Incluso yo le dije que se <a href="http://bit.ly/wwy0R" target="_blank">descargara </a>el <a title="SPD" href="http://www.supergrubdisk.org/" target="_blank">Super Grub Disk</a>, lo cual hizo y hasta una guía se consiguió pero una vez más no hubo suerte 🙁

<!--more-->Ya desmoralizado y viendo que realmente quería de regreso su flamante 

<a href="http://www.ubuntu.org/" target="_blank">Ubuntu</a> 9.04 decidí iniciar con el mismo cd con el que instalamos, pero en la opción Live ;-). Googleé un poco y finalmente di con una solución que me permitió recuperar Grub de una forma fácil, rápida y sencilla.

El nivel de esta entrada es: _Básico-Medio_.

Como menciono lo que se hizo fue iniciar con el cd de **Ubuntu**, escoger el idioma español y la opción de "Probar sin instalar" (o algo así)

Una vez dentro e iniciado ubuntu hacemos clic en "**Lugares – Equipo**"

Esto abrirá una ventana de Nautilus que nos indica todas las particiones que encuentra SIN montarlas. En el caso de la pc en cuestión encontró 2 (dos) partciones y las etiquetó como **disk** y **disk2**. Cuando se instaló se crearon dos particiones **raíz** (**/**) y **home** (**/home**). Al darle clic sobre el ícono de **disk**, éste se monta y nos muestra el contenido que es típico de la partición **raíz** (**/**).

Ahora abrimos una terminal haciendo clic en "**Aplicaciones – Accesorios – Terminal**"

Nos aseguramos en donde está montada la partición y cúal es:

> df -h

> /dev/sda2 10G 2.0G 8G 2% /media/disk

Ok, veremos primero la talacha y luego explico que hicimos :-p

> sudo grub
> 
> GNU GRUB version 0.97 (640K lower / 3072K upper memory)  
> [ Minimal BASH-like line editing is supported. For  
> the first word, TAB lists possible command  
> completions. Anywhere else TAB lists the possible  
> completions of a device/filename. ]  
> grub> root (hd0,1)  
> grub> setup (hd0)  
> grub> quit

Ahora veremos que se hizo:

  * **root (hd0,1)**: Con esto indicamos en donde se encuentra /boot o lo que es lo mismo donde se encuentra grub (en resumidas cuentas)
  * setup (hd0) : Esta instrucción es la que instala Grub en el disco duro
  * **quit**: Salimos de Grub.

Ahora bien para entender un poquito veamos como se ven en grub los discos duros y las particiones:  
Discos duros completos (en esta pc soporta 4 SATA)

  1. Primero (sda) – Grub – hd0
  2. Segundo (sdb) – Grub – hd1
  3. Tercero (sdc) – Grub – hd2
  4. Cuarto (sdd) – Grub – hd3

Ahora es fácil entender que **/dev/sda** es el primer disco duro, por lo tanto sería en grub **hd0**

Las particiones por cada disco duro completo se verían así:

Tomando el primer disco duro:

  1. Primera (sda1) – Grub – hd0,0
  2. Segunda (sda2) – Grub – hd0,1
  3. Tercera (sda3) – Grub – hd0,2
  4. Cuarta (sda4) – Grub – hd0,3

Ahora es fácil entender que **/dev/sda2** es la segunda partición del primer disco duro, por lo tanto en grub sería **hd0,1**  
No queda más que reiniciar el equipo para que Grub haga la función de siempre 😀

Ojalá y alguno le sirva esto 😀
