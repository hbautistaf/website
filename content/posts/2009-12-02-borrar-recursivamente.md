---
title: Borrar recursivamente
date: 2009-12-02 22:35:35+00:00
slug: borrar-recursivamente
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Tips
aliases:
- /2009/12/02/borrar-recursivamente/
- /comos/borrar-recursivamente/
---

Resulta que esto ya van varias veces que lo he llegado a necesitar y hoy también 😛 y pues nada, que después de batallar un poco volví a encontrar el comando correcto para poder eliminar de forma recursiva archivos en Gnu/Linux 🙂

Básicamente es usar el comando **find** 🙂

<!--more-->Si quisieramos encontrar todos los archivos .odt de forma recursiva dentro de un directorio la orden sería la siguiente:

> hbautista@soporte:~$ find documentos/2009/ -type f -name "*.odt"  
> documentos/2009/Servicios/Solicitud\_de\_Servicio.odt  
> documentos/2009/Justificantes/Faltas_19Feb09.odt  
> documentos/2009/Informe\_Comision\_Selva.odt  
> hbautista@soporte:~$

Como ven dentro de ese directorio no hay muchos archivos, pero imaginen que por alguna extraña razón se encuentran con un disco duro externo en donde se crean un monton de archivos **Thumbs.db**

> hbautista@soporte:~$ find /media/Mastodonte/ -type f -name "*.db"  
> /media/Mastodonte/dad/Users/CHILO/AppData/Local/IconCache.db  
> /media/Mastodonte/dad/Users/CHILO/AppData/Local/Microsoft/Windows/Explorer/thumbcache_1024.db  
> /media/Mastodonte/dad/Users/CHILO/AppData/Local/Microsoft/Windows/Explorer/thumbcache_256.db  
> .  
> .  
> .  
> /media/Mastodonte/info/Imagenes/Thumbs.db  
> /media/Mastodonte/info/Imagenes/Wallpaper/Thumbs.db  
> /media/Mastodonte/info/Imagenes/Wolverine/Thumbs.db  
> /media/Mastodonte/info/Imagenes/x-men/Thumbs.db  
> hbautista@soporte:~$

Y pues la verdad en mi caso me desespera que se creen tantos archivos ocupando espacio que puede ser valioso 😉

La forma correcta de eliminar de forma segura y recursiva TODOS esos archivos sería añadir un parámetro más a la orden anterior, quedando de la siguiente manera:

> hbautista@soporte:~$ find /media/Mastodonte/ -type f -name "Thumbs.db" -exec rm {} \;

Aunque igual y se puede resumir a lo siguiente:

> hbautista@soporte:~$ find /media/Mastodonte/ -name "Thumbs.db" -exec rm {} \;

Y con eso logramos nuestro objetivo 🙂
