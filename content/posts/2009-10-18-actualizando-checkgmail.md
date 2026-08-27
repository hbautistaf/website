---
title: Actualizando CheckGmail
date: 2009-10-18 19:41:04+00:00
slug: actualizando-checkgmail
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Tips
aliases:
- /2009/10/18/actualizando-checkgmail/
- /comos/actualizando-checkgmail/
---

Resulta que <a title="Bucio" href="http://bucio.com.mx/" target="_blank">Bucio</a> me recomendó <a title="CheckGmail" href="http://checkgmail.sourceforge.net/index-es.html" target="_blank">CheckGmail</a>:

> **Acerca de Checkgmail**  
> CheckGmail es una Gmail Notifier alternativo para Linux y otros sitemas *nix. Es rápido, seguro y usa un mínimo de bandwidth vía atom feeds.

<!--more-->

  
Y resulta que nomás se quedaba pasmado en tratando de loguearse :S y nomás me sacaba que volviera a escribir mi usuario y contraseña 🙁 y vaya que le puse de varias formas y nomás no funcionaba >_<  
<br>  
Finalmente dí con la solución y <a title="Otra solución" href="http://bit.ly/47L87a" target="_blank">acá también</a>.

Consiste en lo siguiente:

> root@soporte:~# wget http://checkgmail.svn.sourceforge.net/viewvc/checkgmail/checkgmail  
> –2009-10-14 15:06:23–  http://checkgmail.svn.sourceforge.net/viewvc/checkgmail/checkgmail  
> Resolviendo checkgmail.svn.sourceforge.net… 216.34.181.65  
> Connecting to checkgmail.svn.sourceforge.net|216.34.181.65|:80… conectado.  
> Petición HTTP enviada, esperando respuesta… 200 OK  
> Longitud: no especificado [text/plain]  
> Saving to: \`checkgmail'
> 
> [ <=>                                                                                                                ] 197,161     –.-K/s   in 0.04s
> 
> 2009-10-14 15:06:28 (5.35 MB/s) – \`checkgmail' saved [197161]
> 
> root@soporte:~# mv checkgmail /usr/bin/  
> root@soporte:~# chmod +x /usr/bin/checkgmail  
> root@soporte:~#

O también como mencionan en el segundo enlace:

> wget http://checkgmail.svn.sourceforge.net/viewvc/\*checkout\*/checkgmail/checkgmail  
> mv checkgmail /usr/bin/  
> chmod +x /usr/bin/checkgmail

Y ahora solo resta ejecutarlo como un usuario y ya deja conectarse 🙂
