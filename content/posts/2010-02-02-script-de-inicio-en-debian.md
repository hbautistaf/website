---
title: Script de inicio en Debian
date: 2010-02-02 20:08:53+00:00
slug: script-de-inicio-en-debian
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Debian
- Tips
aliases:
- /2010/02/02/script-de-inicio-en-debian/
- /comos/script-de-inicio-en-debian/
---

Resulta que tení­a en mi instalación anterior en la pc de **soporte** algunos scripts que hací­an actividades especí­ficas y en su momento las agregue manualmente para que cada vez que iniciara el sistema, dichos scripts se ejecutaran.

Resulta que en su momento comenté como le hice, pero pues ya tendrá su tiempecito de eso y pues no recordaba exactamente cómo le habí­a hecho.

<!--more-->Sucede que tengo un script con reglas para montar un firewall, además de hacer bloqueo de puertos tanto de entrada como de salida. Cuando por fin quedó funcionando tal y como se necesitaba copie dicho script (llamado local) a 

**/etc/init.d/** y le habí­a dado permisos de ejecución así­.. cada que querí­a ejecutarlo hací­a:

> <div>
>   root_at_soporte:/etc/init_dot_d# /etc/init.d/local
> </div>

Y listo.. se ejecutaba el script. Pero debí­a de ponerlo para que se ejecutara cada vez que esta pc se reiniciara (raramente). Entonces lo conseguí­ gracias a [este artí­culo][1] de [JavoAxian][2].

Así­ que lo que hice fue lo siguiente, entrar al directorio:

> <div>
>   root_at_soporte:/home/hbautista# cd /etc/init.d/
> </div>

Luego fue cuestión de ejecutar **rc-update**

> <div>
>   root_at_soporte:/etc/init_dot_d# update-rc.d local defaults<br /> update-rc.d: warning: /etc/init.d/local missing LSB information<br /> update-rc.d: see<br /> Adding system startup for /etc/init.d/local …<br /> /etc/rc0.d/K20local -> ../init.d/local<br /> /etc/rc1.d/K20local -> ../init.d/local<br /> /etc/rc6.d/K20local -> ../init.d/local<br /> /etc/rc2.d/S20local -> ../init.d/local<br /> /etc/rc3.d/S20local -> ../init.d/local<br /> /etc/rc4.d/S20local -> ../init.d/local<br /> /etc/rc5.d/S20local -> ../init.d/local<br /> root_at_soporte:/etc/init_dot_d#
> </div>

Listo!!, con eso se agrega un script al inicio.

Abur.. 😛

 [1]: http://javoaxian.blogspot.com/2008/03/ejecutar-procesos-al-arrancar-debian-o.html
 [2]: http://javoaxian.blogspot.com/
