---
title: Compartir internet
date: 2011-05-27 20:05:36+00:00
slug: compartir-internet
image: /images/2011/firewall_esquema-1.gif
categories:
- Debian
- Gnu/Linux
tags:
- Cómos
- Compartir_Internet
- Debian
- firewall
- Gnu/Linux
- Howto
- iptables
- Linux
- Scripts
- Ubuntu
aliases:
- /2011/05/27/compartir-internet/
- /debian/compartir-internet/
---

Recientemente una persona me preguntó la forma de compartir internet usando **Gnu/Linux**, y pues se me ha ocurrido comentar la forma más simple de hacerlo mediante **iptables**.

Cabe aclarar que existen mejores formas y también de hacer cosas con restricciones, de este tema no trata este pequeño documento.

[Firewall

" data-image-caption="" data-large-file="/images/2011/firewall_esquema-1.gif" class="alignleft size-medium wp-image-572" title="Firewall" src="/images/2011/firewall_esquema-1.gif" alt="Firewall" width="300" height="155" />][1]  
Si usan un sistema como **Redhat** y derivados, lo siguiente puede ir dentro del archivo **/etc/rc.local** para que sea ejecutado al iniciar la computadora, o bien crear un archivo que se llame **/etc/init.d/firewall** en otros sistemas operativos como **Debian** y sus derivados.

#Vaciamos el contenido de iptables
iptables -F
iptables -Z
iptables -t nat -F

#Hacemos un masquerading
iptables -t nat -A POSTROUTING -s 192.168.1.0/24 -j MASQUERADE

#Aceptamos las conexiones
iptables -A INPUT -p TCP -m state --state RELATED -j ACCEPT

# habilitar el ip forwarding
echo 1 > /proc/sys/net/ipv4/ip_forward</pre>

Con ese sencillo script tienen salida a internet los que estén en tu red interna del tipo **192.168.1.x**, máscara de subred **255.255.255.0**, tu puerta de enlace puede ser **192.168.1.1** siempre y cuando sea la de tu servidor y los dns que más te acomoden (**200.33.126.201**, **200.33.146.193** son los de Telmex).

Saludos y espero que a alguien le sirva.

 [1]: /images/2011/firewall_esquema-1.gif
