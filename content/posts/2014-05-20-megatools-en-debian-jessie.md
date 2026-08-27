---
title: Megatools en Debian Jessie
date: 2014-05-20 14:00:36+00:00
slug: megatools-en-debian-jessie
image: /images/2018/Logo-Mega.png
categories:
- Cómos
- Gnu/Linux
tags:
- Bash
- Cómos
- Debian
- Gnu/Linux
- Howto
- Howtos
- Linux
- Scripts
- Tips
aliases:
- /2014/05/20/megatools-en-debian-jessie/
- /comos/megatools-en-debian-jessie/
---

![Megatools](/images/2014/Megatools-300x55.png)

Después de un buen rato de no publicar nada por acá, volvemos a las andadas u.u

  Pues creo que todos conocen o al menos alguna vez han descargado algún archivo desde <a title="Mega" href="http://mega.co.nz/" target="_blank" rel="noopener">Mega</a>. Si te creas una cuenta te permite almacenar hasta 50GiB de tu información.

  

![Mega Signup](/images/2014/Mega-Sigup-300x121.png)

  

![Logo Mega](/images/2014/Logo-Mega-300x223.png)

Tiene una aplicación para iOS, Android y un cliente para escritorio que por el momento nada más hay para Hasefroch.

  Es una buena opción para subir o compartir archivos que no puedas enviar por correo electrónico, como el vídeo que grabaste de tu sobrino dónde está cantando, el vídeo que grabaste de tu primo al que le jugaron una broma, etc.

  Si te pusiste a escanear esas fotos de cuando eras niño(a) y en ese tiempo, pues no existían las cámaras digitales (ROFL). En fin, pueden ser muchos motivos y muchos tipos de archivo o de información que quieras compartir con tu familia, trabajo, etc.

  Imagina que grabaste la graduación de tu hermano(a) de la prepa o universidad, más parte del convivio familiar y a eso le agregas fotos del evento y decides crear un DVD de autoría propia de dicho evento. Una vez terminado te queda un bonito DVD de 4.7GiB como máximo de tal acontecimiento.

  Ahora resulta que se lo quieres mandar a alguien, para que tenga una copia de dicho recuerdo, creas una imágen ISO de dicho archivo y por obvias razones no se la puedes mandar en un correo.

  Algunos servicios de almacenamiento tampoco te permiten tener un archivo tan grande, entonces te surge la necesidad de "partirlo" en varios pedacitos que se puedan manejar con mayor comodidad.

  Generalmente a este proceso se le denomina "comprimir en varias partes" que es lo más común que se hace en estos casos.

  Y bueno, después de muchos días y esfuerzo invertido logras por fin tener tus "pedacitos" que quieres enviar, pero aún son archivos muy "grandes y pesados" como para enviarlos por correo electrónico. Así que no queda de otra que usar un servicio como el que ofrece Mega.

  Pues bien, igual después de batallarle un poco logras subir dichos archivos al servicio y te genera los enlaces para la descarga que es lo que le enviarás a la persona o personas que quieras que descarguen dicho contenido.

Si fueran unos 4 o 5 enlaces, no hay tanto problema, el servicio Mega te permite descargar varios archivos simultáneamente sin problemas. Las cosas se complican cuando son 20, 30 o hasta 45 enlaces.

Para estos casos se hace necesario el usar algún tipo de gestor de descargas, hay uno para sistemas Hasefroch y encontré algunos esfuerzos para Linux, hasta que dí con Megatools.

![](/images/2018/Mega-Sync.png)

![](/images/2018/Mega-Mobile-Apps.png)

![](/images/2018/Mega.png)

 

  <a title="Megatools" href="http://megatools.megous.com/" target="_blank" rel="noopener">Megatools</a> es un proyecto hecho en Python que consiste en una colección de programas para acceder al servicio de Mega desde la línea de comandos.

  Aunque ahorita el proyecto está detenido y hay un anuncio de que ya no van a continuar con el desarrollo, es funcional y puede ser usado sin problemas aparentes.

  En mi caso estoy usando Debian Jessie (Testing) y aquí vemos la forma de cómo hacer para compilar dicho proyecto.

Lo que se necesita es descargar el código fuente del proyecto:

<a title="http://megatools.megous.com/builds/megatools-1.9.91.tar.gz" href="http://megatools.megous.com/builds/megatools-1.9.91.tar.gz" target="_blank" rel="noopener">http://megatools.megous.com/builds/megatools-1.9.91.tar.gz</a>

  Una vez que lo hayas descargado, extrae el contenido en alguna carpeta, después quedará abrir la terminal y accesar a dicha carpeta.

  Para prevenir que a la hora de compilar el paquete descargado tengamos problemas, instalemos lo necesario (como root):

root@kenobi:/home/hbautista# aptitude install libglib2.0-dev libcurl4-openssl-dev libssl-dev</pre>

   Ahora procederemos a la instalación, como típico paquete de Linux, se ejecuta Configure (como usuario normal):

hbautista@kenobi:~/Descargas/megatools-1.9.91$ ./configure</pre>

Luego make

hbautista@kenobi:~/Descargas/megatools-1.9.91$ make</pre>

Y por último con privilegios de root, make install

hbautista@kenobi:~/Descargas/megatools-1.9.91$ sudo make install</pre>

   Una vez hecho eso veremos que tenemos varios comandos disponiblles

hbautista@kenobi:~$ mega
megadf     megadl     megaget    megals     megamkdir  megamv     megaput    megareg    megarm     megasync
hbautista@kenobi:~$ mega</pre>

   Como en mi caso no necesito configurar una cuenta mega, sino simplemente descargar archivos usando la url "completa", omito dicho paso y solamente hago uso de megadl que es precisamente el que voy a necesitar:

hbautista@kenobi:~/Descargas$ megadl 'https://mega.co.nz/#!1c1WQIZI!25fGpiBF4W1O6phNFo2A1oxVob46009m0cLuSKcfVrk'
megadl: error while loading shared libraries: libmega.so.0: cannot open shared object file: No such file or directory
hbautista@kenobi:~/Descargas$</pre>

   Si les pasa como a mi que les sale ese error de "error while loading shared libraries:…" se debe principalmente a que las librerías recién instaladas aún no están "actualizadas". Para hacerlo, basta ejecutar como root lo siguiente:

root@kenobi:/home/hbautista# ldconfig</pre>

Y si después de eso no funcionara:

root@kenobi:/home/hbautista# ldconfig.real</pre>

Y entonces sí, volver a intentar la descarga:

hbautista@kenobi:~/Descargas$ megadl 'https://mega.co.nz/#!tFVFwTYT!7qkLNQHk45J5gAnn-YkOOWBVjq5xn_nAefeklwl8jCk'
Downloaded Vaughan System.part087.rar
hbautista@kenobi:~/Descargas$</pre>

   Ahora bien, no tiene para hacer descargas simultaneas, pero podemos abrir varias terminales y ejecutar varias veces el comando, tantas como ustedes (y su conexión a internet) se lo permitan. Pero también me pregunté si podemos pasarle varios enlaces en una misma orden:

hbautista@kenobi:~/Descargas$ megadl 'https://mega.co.nz/#!ZcUjzApI!MnJALBLkS9FQptNDi6Ob3OAgIs_xJBuKWaIFXkFocU0' 'https://mega.co.nz/#!MYVSwQhA!ExJ0d2_t2mtZwm8bDQlnBG1F8CaQRdU39OFyZLgtT_M' 'https://mega.co.nz/#!wRdWEBqR!02Zmwza6LJDMLdFOn9R_ZYyHfcYKIxGfMvTegCB9MAI' 'https://mega.co.nz/#!xV9U2TrL!JDo5UQwbNk6kEw96_j_R5bZa2SpE7fHE-y9hQDxy9n8'
Downloaded Vaughan System.part064.rar
Downloaded Vaughan System.part065.rar
Downloaded Vaughan System.part066.rar
Downloaded Vaughan System.part067.rar
hbautista@kenobi:~/Descargas$</pre>

   Y pues si, aunque se va descargando de uno en uno, al menos dejas "encolados" varios archivos a la vez.

  En fin, si quieren ver que más cosas se pueden hacer con Megatools, les dejo el siguiente video:

Espero publicar más seguido 😀
