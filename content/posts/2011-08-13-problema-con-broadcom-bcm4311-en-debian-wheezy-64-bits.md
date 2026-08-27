---
title: Problema con Broadcom BCM4311 en Debian Wheezy 64 bits
date: 2011-08-13 05:50:21+00:00
slug: problema-con-broadcom-bcm4311-en-debian-wheezy-64-bits
image: /images/2011/Broadcom-1.jpg
categories:
- Gnu/Linux
tags:
- Broadcom
- Debian
- Howto
- Kernel
- Linux
- Ubuntu
- Wirreless
aliases:
- /2011/08/13/problema-con-broadcom-bcm4311-en-debian-wheezy-64-bits/
- /linux/problema-con-broadcom-bcm4311-en-debian-wheezy-64-bits/
---

Broadcom

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/08/Broadcom-1.jpg?fit=480%2C257&ssl=1" class="size-medium wp-image-701 alignleft" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/08/Broadcom-1.jpg?resize=300%2C161&ssl=1" alt="" width="300" height="161" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/08/Broadcom-1.jpg?resize=300%2C161&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/08/Broadcom-1.jpg?w=480&ssl=1 480w" sizes="auto, (max-width: 300px) 100vw, 300px" />

  En el mes de julio se celebró el Campus Party México 2011 y aprovechando la velocidad de internet con la que se cuenta allá, me decidí a actualizar mi <a title="Debian" href="http://www.debian.org/index.es.html" target="_blank" rel="noopener">Debian</a> <a title="Debian Squeeze" href="http://www.debian.org/releases/stable/" target="_blank" rel="noopener">Squeeze</a> a <a title="Debian Wheezy" href="http://www.debian.org/releases/testing/" target="_blank" rel="noopener">Wheezy</a> (de Estable a Testing).

  

![Linux Broadcom](/images/2011/linux-broadcom-0-1.jpg)

Pero resulta que me actualizó el kernel y con ello se fue el driver de mi tarjeta inalámbrica que es una Broadcom:

```bash
hbautista@luke:~$ uname -a
Linux luke 2.6.39-2-amd64 #1 SMP Tue Jul 5 02:51:22 UTC 2011 x86_64 GNU/Linux
hbautista@luke:~$ lspci -nn |grep Broadcom
0e:00.0 Network controller [0280]: Broadcom Corporation BCM4311 802.11b/g WLAN [14e4:4311] (rev 01)
hbautista@luke:~$
```

  Así que veremos como solucionar este detalle, primeramente hay que remover los módulos al kernel y actualizar **initramfs**

```bash
root@luke:~# rmmod -f b44 b43 b43legacy ssb brcm80211 wl
root@luke:~# update-initramfs -u -k $(uname -r)
```

Y si no lo tienen instalado, el paquete **Wireless-tools**:

```bash
root@luke:~# aptitude install wireless-tools
```

Luego instalar el firmware de nuestra **Broadcom**:

```bash
root@luke:~# aptitude install firmware-b43-installer
```

Añadimos el módulo

```bash
root@luke:~# modprobe b43
```

En mi caso cuando hice el upgrade de **Squeeze** a **Wheezy**, me desinstaló el paquete para administrar la red cableada e inalámbrica en gnome, así que tuve que instalarla de nuevo:

```bash
root@luke:~# aptitude install network-manager-gnome
```

[Network Manager

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/08/network-manager-1.png?fit=264%2C207&ssl=1" class="aligncenter size-full wp-image-700" title="Network Manager" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/08/network-manager-1.png?resize=264%2C207&ssl=1" alt="Network Manager" width="264" height="207" />][1]

Y reinicié el equipo quedando nuevamente todo funcionando bien y bonito ñ_ñ

En caso de que te encontraras de que no cargue el módulo cada vez que reinicias el equipo, puedes añadirlo manualmente de la siguiente forma, abrir /etc/modules con un editor de texto, nano en mi caso:

```bash
root@luke:~# nano /etc/modules
```

Y como verán, al último se añade el módulo:

```bash
# /etc/modules: kernel modules to load at boot time.
#
# This file contains the names of kernel modules that should be loaded
# at boot time, one per line. Lines beginning with "#" are ignored.
# Parameters can be specified after the module name.
firewire-sbp2
loop
vboxdrv
b43
```

Espero que les sirva esta pequeña información.

Enlaces:

<a title="http://bit.ly/pQJoYQ" href="http://bit.ly/pQJoYQ" target="_blank" rel="noopener">http://bit.ly/pQJoYQ</a>

<a title="http://bit.ly/p8MrCo" href="http://bit.ly/p8MrCo" target="_blank" rel="noopener">http://bit.ly/p8MrCo</a>

<http://wireless.kernel.org/en/users/Drivers/b43>

 [1]: /images/2011/network-manager-1.png
