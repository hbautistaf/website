---
title: Problema con canal negativo en Aircrack-ng
date: 2011-08-13 07:08:24+00:00
slug: problema-con-canal-negativo-en-aircrack-ng
image: /images/2011/aircrack-ng-1.gif
categories:
- Gnu/Linux
tags:
- aircrack
- aircrack-ng
- Broadcom
- Cómos
- Debian
- Howto
- Kernel
- Linux
- Wireless
aliases:
- /2011/08/13/problema-con-canal-negativo-en-aircrack-ng/
- /linux/problema-con-canal-negativo-en-aircrack-ng/
---

[Aircrack-ng

" data-image-caption="" data-large-file="/images/2011/aircrack-ng-new-logo-1.jpg" class="alignleft size-full wp-image-706" title="Aircrack-ng" src="/images/2011/aircrack-ng-new-logo-1.jpg" alt="Aircrack-ng" width="226" height="110" />][1]

Actualmente me encuentro usando <a title="Debian" href="http://debian.org" target="_blank" rel="noopener">Debian</a> **Gnu/Linux Wheezy de 64 bits**, y al momento de actualizarme desde **Squeeze**, también hubo una actualización del **kernel** teniendo en estos momentos:

```bash
hbautista@luke:~$ uname -a
Linux luke 2.6.39-2-amd64 #1 SMP Tue Jul 5 02:51:22 UTC 2011 x86_64 GNU/Linux
hbautista@luke:~$
```

Y pues varios paquetes fueron desinstalados y unos más fueron reemplazados por otros y básicamente hasta ahora me he topado con dos detalles que he logrado solucionar. El primero fue que <a title="Problema con Broadcom" href="http://blog.hbautista.com/linux/problema-con-broadcom-bcm4311-en-debian-wheezy-64-bits/" target="_blank" rel="noopener">no me funcionaba la tarjeta inalámbrica</a> que tengo:

```bash
hbautista@luke:~$ lspci -nn |grep Broadcom
0e:00.0 Network controller [0280]: Broadcom Corporation BCM4311 802.11b/g WLAN [14e4:4311] (rev 01)
hbautista@luke:~$
```

[Wireless Broadcom

" data-image-caption="" data-large-file="/images/2011/wireless-gPCI-Broadcom-1.jpg" class="aligncenter size-medium wp-image-707" title="Wireless Broadcom" src="/images/2011/wireless-gPCI-Broadcom-1.jpg" alt="Wireless Broadcom" width="300" height="225" srcset="/images/2011/wireless-gPCI-Broadcom-1.jpg 300w, /images/2011/wireless-gPCI-Broadcom-1.jpg 768w, /images/2011/wireless-gPCI-Broadcom-1.jpg 800w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2]

Ese punto ya lo he solucionado y ahora vengo por el segundo detalle, cuando hacemos una auditoría de una red inalámbrica, generalmente uno de los programas que se usan es el <a title="Aircrack" href="http://www.aircrack-ng.org/" target="_blank" rel="noopener">aircrack-ng</a>. Pues bien, me topé con el detalle de que en uno de los pasos donde especificas en que canal vas a trabajar, independientemente de cual le indiques, siempre te lo pondrá en el canal -1 y obviamente no podrás hacer la autenticación ni nada más.

Pues al parecer es un detalle en el kernel y aquí tenemos los pasos que en mi caso, si funcionaron:

Descargar el paquete **compat-wireless**:

```bash
root@luke:~# pwd
/root
root@luke:~# wget http://linuxwireless.org/download/compat-wireless-2.6/compat-wireless-2011-07-07.tar.bz2
```

Extraemos el contenido del paquete comprimido:

```bash
root@luke:~# tar jfxv compat-wireless-2011-07-07.tar.bz2
```

Accedemos a la carpeta extraida:

```bash
root@luke:~# cd compat-wireless-2011-07-07/
```

Descargamos el parche de nuestra tarjeta inalámbrica, en mi caso fue esta:

```bash
root@luke:~# wget http://patches.aircrack-ng.org/mac80211.compat08082009.wl_frag+ack_v1.patch
```

Aplicamos el parche:

```bash
root@luke:~# patch -p1 < mac80211.compat08082009.wl_frag+ack_v1.patch
```

Descargamos el parche para el canal negativo:

```bash
root@luke:~# wget http://patches.aircrack-ng.org/channel-negative-one-maxim.patch
```

Aplicamos ese parche

```bash
root@luke:~# patch ./net/wireless/chan.c channel-negative-one-maxim.patch
```

Compilamos el paquete, nótese que todos los pasos los estoy haciendo como root y en el directorio de root, pero hasta este paso se pueden hacer como un usuario normal en cualquier directorio de su home, sólo los pasos posteriores a estos se deben hacer con la cuenta root.

```bash
root@luke:~# make
```

Después de unos minutos y si todo salió bien, entonces instalamos:

```bash
root@luke:~# make install
```

Quitamos de memoria los controladores wireless:

```bash
root@luke:~# make unload
```

Ponemos otra vez nuestro driver de la tarjeta inalámbrica:

```bash
root@luke:~# modprobe b43
```

Actualizamos initramsf

```bash
root@luke:~# update-initramfs -u
```

Y con esto debería de funcionar todo correctamente, en mi caso y por las lecturas que consulté indican que se debe reiniciar el equipo, cosa que yo hice y cuando volví a ejecutar aircrack-ng ya no me mandó al canal negativo.

aircrack-ng

" data-image-caption="" data-large-file="/images/2011/aircrack-ng-1.gif" class="aligncenter size-medium wp-image-708" src="/images/2011/aircrack-ng-1.gif" alt="" width="300" height="198" /> 

Enlaces:

<http://free4universe.wordpress.com/2010/12/29/problema-con-canal-negativo-en-aircrack-ng/>

http://www.portalhacker.net/index.php?topic=140639.0

 

 [1]: /images/2011/aircrack-ng-new-logo-1.jpg
 [2]: /images/2011/wireless-gPCI-Broadcom-1.jpg
