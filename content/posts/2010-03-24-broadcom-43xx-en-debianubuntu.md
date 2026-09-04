---
title: Broadcom 43xx en Debian/Ubuntu
date: 2010-03-24 21:04:27+00:00
slug: broadcom-43xx-en-debianubuntu
categories:
- Cómos
- Debian
- Gnu/Linux
- Ubuntu
tags:
- Cómos
- Debian
- Gnu/Linux
- Luke
- Tips
- Ubuntu
aliases:
- /2010/03/24/broadcom-43xx-en-debianubuntu/
- /comos/broadcom-43xx-en-debianubuntu/
---

Pues para aquellos que cuenten con una tarjeta inalámbrica **Broadcom** **4311** o **4312** y usen <a title="Debian" href="http://debian.org" target="_blank">Debian</a> o <a title="Ubuntu" href="http://ubuntu.com" target="_blank">Ubuntu</a>, pues aquí está la forma de echarlos andar sin problemas 😀

En mi caso ya que tengo una tarjeta broadcom 4311 como podemos ver acá y uso Debian (^_^)

[lspci Broadcom 43xx

" data-image-caption="" data-large-file="/images/2011/Pant_lspci.png" class="aligncenter size-medium wp-image-771" title="lspci Broadcom 43xx" src="/images/2011/Pant_lspci.png" alt="lspci Broadcom 43xx" width="300" height="174" srcset="/images/2011/Pant_lspci.png 300w, /images/2011/Pant_lspci.png 768w, /images/2011/Pant_lspci.png 1024w, /images/2011/Pant_lspci.png 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" />][1]

```bash
hbautista@luke:~$  lspci |grep Network
0e:00.0 Network controller: Broadcom Corporation BCM4311 802.11b/g WLAN (rev 01)
hbautista@luke:~$
```

Luego entonces, hay que instalar b43-fwcutter para hacerla funcionar sin problemas

```bash
root@luke:/home/hbautista# aptitude install b43-fwcutter
```

Basta reiniciar la laptop y con eso ya tengo funcionando mi tarjeta **Broadcom** con todo y el modo **monitor** (**mon0**) ñ_ñ

Ahora bien, si usas **Ubuntu 9.10** y tienes la **Broadcom 4312** como acá:

```bash
:~$ lspci |grep Network
06:00 Network controller: Broadcom Corporation BCM4312 802.11b/g (rev 01)
```

El procedimiento sería hacer lo siguiente:

```bash
aptitude install bcmwl-kernel-source
```

Igualmente, reinicias y ya tendrás tu tarjera inalámbrica funcionando al 100% ñ_ñ lo que si no puedo decirles es si funciona el modo **monitor** (**mon0**)

Es cuestión de que avisen si con eso queda funcionando el modo monitor 😉

Referencias:

> <a title="Broadcom Ubuntu" href="http://bit.ly/b8k7q3" target="_blank">http://bit.ly/b8k7q3</a>

 [1]: /images/2011/Pant_lspci.png
