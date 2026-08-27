---
title: Broadcom BCM4311 en Ubuntu
date: 2009-10-26 16:38:14+00:00
slug: broadcom-bcm4311-en-ubuntu
categories:
- Cómos
- Gnu/Linux
tags:
- Cómos
- Ubuntu
aliases:
- /2009/10/26/broadcom-bcm4311-en-ubuntu/
- /comos/broadcom-bcm4311-en-ubuntu/
---

Resulta que [@avidal][1] me estuvo preguntando en varios correos que tenía una bronca con su wireless en su lap con Ubuntu. Así que finalmente nos vimos en el parque de la juventud el pasado jueves o viernes  
<!--more-->Finalmente y después de checar que esa instalación ya estaba más tocada que Niurka nos fuimos a mi casa para reinstalarle Ubuntu, porque además estaba usando una versión anterior.

Finalmente le instalamos Ubuntu 9.04 y algunos paquetes más. Pero efectivamente la che tarjeta wireless nomás no detectaba nada, algo por ahí estaba fallando.

Ahorita exactamente no recuerdo el modelo, espero que me mande por correo ese dato para colocarlo acá.

> $ sudo su  
> \# modprobe -r b43 b44 ssb wl  
> \# modprobe ieee80211\_crypt\_tkip  
> \# modprobe wl  
> \# modprobe b44  
> \# /etc/init.d/networking restart

Y con eso funcionó después de unos segundos de haber reiniciado el servicio de la red (networking), el problema es que esos pasos hay que hacerlos cada vez que se reinicie el equipo :S 🙁 así que retocando rc.local se pudo hacer que lo hiciera de forma automática.

> nano /etc/rc.local
> 
> modprobe -r b43 b44 ssb wl  
> modprobe ieee80211\_crypt\_tkip  
> modprobe wl  
> modprobe b44  
> /etc/init.d/networking restart

Y ya está, cada vez que inicie ubuntu quedará perverso.

  * **modprobe -r b43 b44 ssb wl**: Quita los módulos que causan problemas
  * **modprobe ieee80211\_crypt\_tkip**: Carga este módulo que es esencial
  * **modprobe wl y b44**: Son para cargar los modulos de la tarjeta Broadcom
  * **/etc/init.d/networking restart**: Reiniciamos la red

Espero que a alguien le pueda servir:

Enlaces de interés

  * <a title="Broadcom Ubuntu" href="http://bit.ly/bCwMU" target="_blank">http://bit.ly/bCwMU</a>
  * <a title="Broadcom Ubuntu" href="http://bit.ly/shv4W" target="_blank">http://bit.ly/shv4W</a>

 [1]: http://twitter.com/avidal
