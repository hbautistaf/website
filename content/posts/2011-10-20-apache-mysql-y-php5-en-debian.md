---
title: Apache, Mysql y Php5 en Debian
date: 2011-10-20 06:05:10+00:00
slug: apache-mysql-y-php5-en-debian
image: /images/2011/apache_php_mysql_logo-1.jpg
categories:
- Cómos
- Gnu/Linux
tags:
- Apache2
- Cómos
- Debian
- Gnu/Linux
- Linux
- Mysql
- Php
aliases:
- /2011/10/20/apache-mysql-y-php5-en-debian/
- /comos/apache-mysql-y-php5-en-debian/
---

Logo Apache, Mysql y Php

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/apache_php_mysql_logo-1.jpg?fit=325%2C287&ssl=1" class="size-medium wp-image-742 alignleft" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/apache_php_mysql_logo-1.jpg?resize=300%2C265&ssl=1" alt="" width="300" height="265" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/apache_php_mysql_logo-1.jpg?resize=300%2C265&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/apache_php_mysql_logo-1.jpg?w=325&ssl=1 325w" sizes="auto, (max-width: 300px) 100vw, 300px" />Debido a que tengo que hacer algunas pruebas con plantillas y demás, me vi en la necesidad de instalar un entorno para hacer las pruebas correspondientes. En este caso necesitamos de tener instalado el servidor web **Apache**, **Mysql** y **Php5**.

Una vez que hayamos terminado, tendremos un servidor web + php + mysql.

Así que comenzaremos por instalar lo necesario, podemos instalar primeramente el servidor web y luego los demás componentes, o como en mi caso. Instalar lo que voy a necesitar de una buena vez:

```bash
root@luke:/home/hbautista# aptitude install apache2-mpm-prefork mysql-server mysql-admin php5 php5-mysql php5-gd php5-mcrypt php5-imagick
Se instalarán los siguiente paquetes NUEVOS:
  apache2-mpm-prefork apache2-utils{a} apache2.2-common{a} libapache2-mod-php5{a}
  libdbd-mysql-perl{a} libdbi-perl{a} libgd2-xpm{ab} libgtkhtml3.14-19{a}
  libhtml-template-perl{a} libmcrypt4{a} libnet-daemon-perl{a} libonig2{a} libplrpc-perl{a}
  libqdbm14{a} mysql-admin mysql-client-5.1{a} mysql-gui-tools-common{a}
  mysql-query-browser{a} mysql-server mysql-server-5.1{a} php5 php5-cli{a} php5-common{a}
  php5-gd php5-imagick php5-mcrypt php5-mysql php5-suhosin{a}
0 paquetes actualizados, 28 nuevos instalados, 0 para eliminar y 7 sin actualizar.
Necesito descargar 30.3 MB de ficheros. Después de desempaquetar se usarán 77.1 MB.
No se satisfacen las dependencias de los siguientes paquetes:
  libgd2-noxpm: Entra en conflicto: libgd2 que es un paquete virtual.
                Entra en conflicto: libgd2-xpm pero se va a instalar 2.0.36~rc1~dfsg-5.1+b1.
  libgd2-xpm: Entra en conflicto: libgd2 que es un paquete virtual.
              Entra en conflicto: libgd2-noxpm pero está instalado 2.0.36~rc1~dfsg-5.1+b1.
Las acciones siguientes resolverán estas dependencias

     Eliminar los paquetes siguientes:
1)     libgd2-noxpm                   

¿Acepta esta solución? [Y/n/q/?]y
Se instalarán los siguiente paquetes NUEVOS:
  apache2-mpm-prefork apache2-utils{a} apache2.2-common{a} libapache2-mod-php5{a}
  libdbd-mysql-perl{a} libdbi-perl{a} libgd2-xpm{a} libgtkhtml3.14-19{a}
  libhtml-template-perl{a} libmcrypt4{a} libnet-daemon-perl{a} libonig2{a} libplrpc-perl{a}
  libqdbm14{a} mysql-admin mysql-client-5.1{a} mysql-gui-tools-common{a}
  mysql-query-browser{a} mysql-server mysql-server-5.1{a} php5 php5-cli{a} php5-common{a}
  php5-gd php5-imagick php5-mcrypt php5-mysql php5-suhosin{a}
Se ELIMINARÁN los siguientes paquetes:
  libgd2-noxpm{a}
0 paquetes actualizados, 28 nuevos instalados, 1 para eliminar y 7 sin actualizar.
Necesito descargar 30.3 MB de ficheros. Después de desempaquetar se usarán 76.5 MB.
¿Quiere continuar? [Y/n/?]
```

  Como habrán notado, estoy instalando el paquete **apache2-mpm-prefork**, ya que si instalan el paquete **apache2**, instala **apache2-mpm-worker** que entra en conflicto con **php5**.

  

![Pant_lamp](/images/2011/Pant_lamp-1.png)

  Como nota, indicar que de preferencia NO desinstalen **libgd2-noxpm** que aparece ahí, ya que es necesario para varios paquetes de entorno gráfico que en mi caso los uso. Pero no se preocupen, se sustituye por **libgd2-xpm** y los programas mencionados siguen funcionando de igual forma.

Voy a mencionar cuales son los paquetes que corresponden a cada cosa:

  Esos paquetes instalarán el servidor web, por defecto, la carpeta donde se almacenaran los archivos es en **/var/www**

```bash
apache2-mpm-prefork apache2-utils apache2.2-common
```

Ahora viene la parte de Php5 y sus librerías:

```bash
php5 php5-cli php5-common php5-gd php5-imagick php5-mcrypt php5-mysql php5-suhosin
```

Ahora el módulo de Apache para Php5 para que nuestro servidor web pueda interpretar las páginas con código Php

```bash
libapache2-mod-php5
```

Ahora toca el turno para el servidor de base de datos Mysql, el cliente y un programa para administrarlo de forma gráfica (mysql-admin).

Pant_lamp2

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp2-1.png?fit=648%2C380&ssl=1" class="aligncenter size-medium wp-image-745" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp2-1.png?resize=300%2C176&ssl=1" alt="" width="300" height="176" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp2-1.png?resize=300%2C176&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp2-1.png?resize=768%2C450&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp2-1.png?resize=1024%2C600&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp2-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

```bash
mysql-admin mysql-client-5.1 mysql-gui-tools-common mysql-query-browser{a} mysql-server mysql-server-5.1
```

Una vez que se instale el paquete mysql-server, nos pedirá una contraseña para el usuario root de Mysql, la librería php5-mysql nos permitirá enlazar Mysql con Php y con eso tendremos ya listo lo necesario para comenzar a trabajar.

Pant_lamp3

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp3-1.png?fit=648%2C380&ssl=1" class="alignnone size-medium wp-image-747" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp3-1.png?resize=300%2C176&ssl=1" alt="" width="300" height="176" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp3-1.png?resize=300%2C176&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp3-1.png?resize=768%2C450&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp3-1.png?resize=1024%2C600&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp3-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" />Mysql-admin

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp6-1.png?fit=428%2C356&ssl=1" class="alignnone size-medium wp-image-748" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp6-1.png?resize=300%2C250&ssl=1" alt="" width="300" height="250" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp6-1.png?resize=300%2C250&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_lamp6-1.png?w=428&ssl=1 428w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Para verificar que la configuración básica y por defecto está funcionando bien, podemos crear un archivo llamado info.php o prueba.php que tenga por único contenido lo siguiente:

```bash
<?php phpinfo();?>
```

Y lo podemos ver si accedemos desde nuestro navegador en la siguiente dirección:

```bash
http://localhost/prueba.php
```

Deberíamos ver nuestro navegador un resumen con toda la información de PHP en nuestro sistema.

Ahora bien si queremos afinar más detalles, tendremos que configurar los archivos de configuración de cada uno de los servicios:

```bash
Apache: /etc/apache2/apache2.conf
PHP: /etc/php5/apache2/php.ini
MySQL: /etc/mysql/my.cnf
```

Una vez modificados los ficheros de configuración, recuerda que debes de reiniciar los servicios, para que los cambios se vean reflejados.

```bash
# /etc/apache2 restart
# /etc/mysql restart
```

Y eso es todo..
