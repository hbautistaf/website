---
title: Recuperar contraseña
date: 2009-11-04 16:41:03+00:00
slug: recuperar-contrasena
categories:
- Cómos
- Gnu/Linux
tags:
- Cómos
- Gnu/Linux
- Ubuntu
aliases:
- /2009/11/04/recuperar-contrasena/
- /comos/recuperar-contrasena/
---

Resulta que ayer me trajeron una laptop que tiene Ubuntu instalado (pero se puede aplicar básicamente a cualquier gnu/linux) pero que no recordaban ni la cuenta de usuario ni mucho menos la contraseña 😛

Primero averigüe cual era el nombre de usuario (**chencho**) y ya luego me dispuse a usar un entorno **chroot** para asignar una nueva contraseña 🙂

<!--more-->Así que hace unos minutos me dí a la tarea de recuperar dicha contraseña y he aquí la forma de hacerlo 🙂

  * Iniciar desde un live cd (en mi caso lo hice con el de Karmic Koala) 😛
  * Montar la partición (Lugares -> Disco de XXGB) y te muestra el iconito en el escritorio 😉
  * Abrir la terminal y escribir **sudo su** para tener acceso a root (livecd no te pide contraseña)
  * Teclear **chroot /media/tudisco /bin/bash**
  * Cambiar la contraseña en cuestión con: **passwd root** o **passwd tuusuario** 😀
  * Reiniciar el equipo y listo!! 😀

En resumen lo que yo hice fue

> _**chroot /media/ubuntu /bin/bash**_
> 
> _**passwd chencho**_
> 
> _**exit**_

Reinicié el equipo y escribí la contraseña que le asigne (pepenador) y así con un excelente tiempo de 10 minutos (entre lo que metía el cd, iniciaba y reiniciaba) recuperamos ese equipo 😀
