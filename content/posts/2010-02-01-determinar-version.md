---
title: Determinar versión
date: 2010-02-02 05:32:13+00:00
slug: determinar-version
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Gnu/Linux
- Tips
aliases:
- /2010/02/01/determinar-version/
- /comos/determinar-version/
---

Esta nota ya la había puesto en mi blog anterior, pero lo vuelvo a repetir para aquellos que les pueda interesar.

Si queremos saber la versión del Sistema Operativo Gnu/Linux que tenemos podemos hacer lo siguiente:

<!--more-->

> hbautista\_at\_soporte:~$ cat /etc/issue  
> Debian GNU/Linux lenny/sid \n \l  
> hbautista\_at\_soporte:~$ cat /etc/debian_version  
> lenny/sid  
> hbautista\_at\_soporte:~$ lsb_release -a  
> No LSB modules are available.  
> Distributor ID: Debian  
> Description: Debian GNU/Linux testing (lenny)  
> Release: testing  
> Codename: lenny  
> hbautista\_at\_soporte:~$

Esos comandos son los que generalmente uso para saber que versión de la distribución usas, ¿Cuáles usan ustedes?

> hbautista\_at\_soporte:~$ uname -a  
> Linux soporte 2.6.26-1-686 #1 SMP Thu Oct 9 15:18:09 UTC 2008 i686 GNU/Linux  
> hbautista\_at\_soporte:~$

A veces uno se topa en situaciones cómo la que me tocó a mi ayer y algunos pues no saben exactamente la existencia de este tipo de comandos.

Saludos.. 😀
