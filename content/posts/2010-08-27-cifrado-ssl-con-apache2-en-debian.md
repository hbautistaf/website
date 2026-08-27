---
title: Cifrado SSL con Apache2 en Debian
date: 2010-08-27 20:43:17+00:00
slug: cifrado-ssl-con-apache2-en-debian
image: /images/2010/apache.png
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Apache
- CACert
- Cómos
- Debian
- Howto
- https
- SSL
- Tips
aliases:
- /2010/08/27/cifrado-ssl-con-apache2-en-debian/
- /comos/cifrado-ssl-con-apache2-en-debian/
---

Instalar el servidor <a title="Apache" href="http://www.apache.org/" target="_blank" rel="noopener">Apache2</a> en <a title="Debian" href="http://www.debian.org/" target="_blank" rel="noopener">Debian</a> no es una tarea complicada sin duda, pero el ir puliendo algunos detalles para tener un mejor performance, seguridad y estabilidad en general, a veces lo es.

Supongamos que deseamos agregar un nuevo sitio pero que la comunicación entre el cliente y el servidor sea cifrada mediante el uso de https. Para esto necesitamos activar el cifrado ssl en apache, lo hacemos mediante la utilidad a2enmod ejecutando:

```bash
# a2enmod ssl
```

También debemos decir a apache que debe aceptar solicitudes en el puerto 443 que es el puerto estándar de https por lo que editamos el archivo **/etc/apache2/ports.conf** y agregamos la línea **Listen 443**, he aquí la configuración que tiene mi **Apache2**:

<!--more-->

```bash
# If you just change the port or add more ports here, you will likely also
# have to change the VirtualHost statement in
# /etc/apache2/sites-enabled/000-default
# This is also true if you have upgraded from before 2.2.9-3 (i.e. from
# Debian etch). See /usr/share/doc/apache2.2-common/NEWS.Debian.gz and
# README.Debian.gz

NameVirtualHost *:80
Listen 80

<IfModule mod_ssl.c>
 # If you add NameVirtualHost *:443 here, you will also have to change
 # the VirtualHost statement in /etc/apache2/sites-available/default-ssl
 # to <VirtualHost *:443>
 # Server Name Indication for SSL named virtual hosts is currently not
 # supported by MSIE on Windows XP.
 Listen 443
</IfModule>

<IfModule mod_gnutls.c>
 Listen 443
</IfModule>
```

Es importante aclarar que al menos tanto el módulo **SSL** como el puerto **443** ya se encontraban 'activados' cuando instalé Apache2.

Ahora necesitamos crear los certificados que utilizaremos para el cifrado, para ello utilizaremos **OpenSSL**, deberemos instalarlo ejecutando:

```bash
# aptitude install openssl
```

Por si no lo tenemos instalado, una vez que lo tengamos, se crean dos certificados, el público y el privado:

```bash
# openssl req -new -newkey rsa:2048 -nodes -out /etc/ssl/certs/publico.pem -keyout /etc/ssl/private/privado.pem

Country Name (2 letter code) [AU]: MX
State or Province Name (full name) [Some-State]: Chiapas
Locality Name (eg, city) []: Tuxtla Gutierrez
Organization Name (eg, company) [Internet Widgits Pty Ltd]: Mi Organización
Organizational Unit Name (eg, section) []: Posh Inc
Common Name (eg, YOUR name) []: www.dominiocifrado.com
Email Address []: muajajaja@diablito.com

Please enter the following 'extra' attributes
to be sent with your certificate request
A challenge password []:
An optional company name []:
```

Los archivos generados serían:

La petición de nuevo certificado, que una autoridad certificadora (CA) tendrá que firmar, en **/etc/ssl/certs/publico.pem**.

La clave privada del certificado en /etc/ssl/private/privado.pem.

Podemos usar <a title="CaCert" href="http://www.cacert.org/" target="_blank" rel="noopener">CAcert.org</a> para firmar la petición de certificado. Debido a que CAcert.org tan sólo puede verificar la información contenida en el Common Name, da igual lo que introduzcamos en los otros campos (el resto lo descarta).

El certificado resultante después de la firma de <a title="CaCert" href="http://www.cacert.org/" target="_blank" rel="noopener">CACert.org</a> lo dejaremos en el archivo **/etc/ssl/certs/publico.pem** con permisos **644** para el usuario y grupo **root**. La clave privada ya se encuentra en **/etc/ssl/private/privado.pem** con permisos **640** para el usuario **root**, pero debemos cambiarle el grupo a **ssl-cert**:

```bash
chgrp ssl-cert /etc/ssl/private/privado.pem
```

Para utilizar los servicios de <a title="CaCert" href="http://www.cacert.org/" target="_blank" rel="noopener">CACert.org</a> debemos realizar los siguientes pasos:

<ol>
<li>Darnos de <a title="CaCert" href="https://www.cacert.org/index.php?id=1" target="_blank" rel="noopener">alta</a> en su web.</li>
<li>Una vez validados en su sistema, <a title="CaCert" href="https://www.cacert.org/account.php?id=7" target="_blank" rel="noopener">dar de alta nuestro dominio</a> **dominiocifrado.com**</li>
<li>Una vez verificado nuestro dominio, procederemos a <a title="CaCert" href="https://www.cacert.org/account.php?id=10" target="_blank" rel="noopener">realizar la solicitud del certificado</a> usando el contenido del fichero **/etc/ssl/certs/publico.pem**.</li>
</ol>

En el caso de que no querramos firmar el certificado por CACert.org, podemos hacerlo nosotros mismos:

```bash
openssl x509 -req -days 3650 -signkey privado.pem -out publico.pem
```

***Nota***: Es altamente recomendable hacerlo con CACert.org ya que es un ente reconocido y el servicio es gratuito. Si requieren algo más profesional, pueden checar con <a title="VeriSign" href="http://www.verisign.com/" target="_blank" rel="noopener">VeriSign</a>.

***Nota2***: Cuando ya se encuentre firmado nuestro certificado nos llegará un correo electrónico indicándonos el contenido de la firma, el contenido de dicha firma debemos ponerla en lugar del contenido del archivo que se encuentra en **/etc/ssl/certs/publico.pem**

Ahora nada más queda tener nuestro archivo de configuración dentro de **/etc/apache2/sites-available/dominiocifrado.conf**

Aquí la configuración del archivo dominiocifrado.conf

```bash
<VirtualHost *:443>
 ServerAdmin webmaster@dominiocifrado.com
 ServerName dominiocifrado.com
 ServerAlias www.dominiocifrado.com
 DocumentRoot /home/web/cifrada

 #Aquí indicamos que será un canal cifrado y los certificados que antes creamos, aquí los ubicamos
 SSLEngine on
 SSLCertificateFile "/etc/ssl/certs/publico.pem"
 SSLCertificateKeyFile "/etc/ssl/private/privado.pem"
 ErrorLog /var/log/apache2/dominiocifrado.eror.log
 CustomLog /var/log/apache2/dominiocifrado.access.log combined

 <Directory />
 Options FollowSymLinks
 AllowOverride None
 </Directory>
 <Directory /home/web/cifrada>
 Options Indexes FollowSymLinks MultiViews
 AllowOverride None
 Order allow,deny
 allow from all
 </Directory>
</VirtualHost>
```

Después procederemos a reiniciar nuestro servidor Apache con el siguiente comando:

```bash
# /etc/init.d/apache2 restart
```

Y entrar a nuestro nuevo sitio web cifrado:

```bash
https://dominiocifrado.com
```

Veremos nuestro certificado más o menos como esto:

![Cifrado](/images/2010/Pant_cifrado-1.png)

![](/images/2010/Pant_cifrado2-1.png)

Eso es todo, espero a alguien pueda parecerle útil esta información

Fuentes:

<a title="LinuxSilo" href="http://linuxsilo.net/articles/postfix-mysql.html" target="_blank" rel="noopener">LinuxSilo.org</a>

<a title="esDebian" href="http://www.esdebian.org/wiki/apache-2-eaccelerator-mod-security-cifrado-ssl-instalacion-configuracion-gnulinux-debian" target="_blank" rel="noopener">esDebian.org</a>
