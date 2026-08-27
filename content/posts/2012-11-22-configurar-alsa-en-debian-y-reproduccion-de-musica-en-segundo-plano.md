---
title: Configurar ALSA en Debian y reproducción de música en segundo plano
date: 2012-11-22 23:00:11+00:00
slug: configurar-alsa-en-debian-y-reproduccion-de-musica-en-segundo-plano
image: /images/2012/alsaequal-1.png
categories:
- Cómos
- Gnu/Linux
tags:
- ALSA
- Alsamixer
- Bash
- Cómos
- Debian
- Howtos
- Linux
- mplayer
- nohup
- Scripts
- Servidor
- Sonido
- Squeeze
aliases:
- /2012/11/22/configurar-alsa-en-debian-y-reproduccion-de-musica-en-segundo-plano/
- /comos/configurar-alsa-en-debian-y-reproduccion-de-musica-en-segundo-plano/
---

He instalado un servidor casero con Debian Squeeze, y como tal, sólo se ha instalado lo necesario para que funcione como tal, servir como servidor Web para manejar control de inventario de bienes informáticos y poco más.

  Resulta que después de dicha instalación (aproximadamente 1 mes después) me surge la necesidad de tener una fuente de audio "permanente" para el conmutador de la empresa, es decir, el clásico sonido de música en espera cambiarlo por un archivo de audio cualquiera.

 [Alsamixer

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/alsaequal-1.png?fit=648%2C450&ssl=1" class="aligncenter size-medium wp-image-930" title="Alsamixer" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/alsaequal-1.png?resize=300%2C208&ssl=1" alt="Alsamixer" width="300" height="208" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/alsaequal-1.png?resize=300%2C208&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/alsaequal-1.png?resize=768%2C533&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/alsaequal-1.png?w=1014&ssl=1 1014w" sizes="auto, (max-width: 300px) 100vw, 300px" />][1]

  En ese sentido, hay dos equipos que actuán de servidores en el site donde se encuentra el conmutador, pero sólo el equipo con Debian tiene tarjeta de audio, así que el otro quedó descartado.

## Manos a la obra

  Ese pequeño servidor con Debian no tiene ambiente gráfico, se instaló (como mencioné al inicio) sólo la base y de ahí a instalar los paquetes que hicieron falta para dejarlo funcionando. Pues bien, al no instalar el ambiente gráfico no se instalaron los paquetes necesarios para que se pueda oir desde consola.

Checamos que estén cargados los módulos (en mi caso, sí lo estaba)

```bash
~# cat /proc/asound/modules
0 snd_via82xx
```

Y checar qué módulos se están cargando

```bash
# lsmod |grep snd
snd_via82xx 15256 2
gameport 6061 1 snd_via82xx
snd_ac97_codec 79136 1 snd_via82xx
ac97_bus 710 1 snd_ac97_codec
snd_pcm 47226 3 snd_via82xx,snd_ac97_codec
snd_page_alloc 5045 2 snd_via82xx,snd_pcm
snd_mpu401_uart 4067 1 snd_via82xx
snd_seq_midi 3576 0
snd_seq_midi_event 3684 1 snd_seq_midi
snd_rawmidi 12513 2 snd_mpu401_uart,snd_seq_midi
snd_seq 35463 2 snd_seq_midi,snd_seq_midi_event
snd_timer 12270 2 snd_pcm,snd_seq
snd_seq_device 3673 3 snd_seq_midi,snd_rawmidi,snd_seq
snd 34423 11 snd_via82xx,snd_ac97_codec,snd_pcm,snd_mpu401_uart,snd_rawmidi,snd_seq,snd_timer,snd_seq_device
```

En caso de que no estén instalados los paquetes necesarios, los instalamos

```bash
# aptitude install alsa-utils alsa-oss alsa-tools
```

Bastaría realizar el paso siguiente para ya dejar funcionando la tarjeta, y no dar tantas vueltas como lo hice yo

```bash
# alsaconf
```

Sonido en Debian

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/debian211-1.png?fit=648%2C477&ssl=1" class="size-medium wp-image-931 aligncenter" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/debian211-1.png?resize=300%2C221&ssl=1" alt="" width="300" height="221" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/debian211-1.png?resize=300%2C221&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/debian211-1.png?resize=768%2C565&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2012/11/debian211-1.png?w=800&ssl=1 800w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

El problema viene cuando vemos en la <a title="Wiki Alsa Debian" href="http://wiki.debian.org/ALSA" target="_blank" rel="noopener">Wiki de ALSA en Debian </a>lo siguiente:

> 

>   For release Squeeze or any later release, alsaconf is no longer available in package <a title="alsa-utils" href="http://packages.debian.org/alsa-utils" target="_blank" rel="noopener">alsa-utils</a>. So try to configure alsa by running the command '**alsactl init**' as root. Just ignore the error message like 'Unknown hardware' (this issue said to be fixed in alsa-utils .20), then reboot and try to test your sound. For more details please see this <a title="Forums Debian" href="http://forums.debian.net/viewtopic.php?f=6&t=39116" target="_blank" rel="noopener">thread</a>.
> 

Así que tendremos que ejecutar lo siguiente como root:

```bash
# alsactl init
```

Y con eso ya tenemos resuelto el problema de sonido, bastaría hacer una prueba colocando bocinas o auriculares y reproducir algún archivo de audio para corroborar que todo funciona bien.

  Ahora bien, una vez que ya tengo solucionado el problema de sonido viene ver el segundo punto, dejar audio (o música) reproduciendo en dicho servidor de forma continua, es decir, que esté reproduciendo el o los archivos de audio (mp3) de forma aleatoria y sin parar.

  Para esto usaremos dos programas, el primero es el viejo conocido mplayer(http://www.mplayerhq.hu) que me servirá para reproducir archivos de audio.

```bash
$ mplayer "01 Diablo.mp3"
```

Con esto hacemos una prueba simple de reproducción.

Si tenemos varios archivos, el comando sería el siguiente:

```bash
$ mplayer *.mp3
```

Si queremos que la reproducción se repita como en un bucle, usamos la opción -loop indicando con un número las veces que queremos que se repita:

```bash
$ mplayer "03 Elysium.mp3" -loop 5
```

Con eso logramos que se repita 5 veces, pero si queremos que sea indefinido, es decir, hasta que nosotros lo cancelemos, sería:

```bash
$ mplayer "03 Elysium.mp3" -loop 0
```

  Ya avanzamos, ahora la idea es tener varios archivos que se reproduzcan de forma indefinida pero también de forma aleatoria, para lograr esto último, usamos la opción -shuffle:

```bash
$ mplayer -shuffle -loop 0 *.mp3
```

  En este caso, tengo un directorio llamado "bond" con unos 15 archivos mp3 que quiero que se reproduzcan de forma aleatoria y que se repitan indefinidamente, pero además que si cierro sesión via tty1, putty o ssh, el comando se siga ejecutando en segundo plano. En este caso nohup(http://rm-rf.es/nohup-mantiene-ejecucion-comando-pese-salir-terminal/) es nuestro amigo ñ_ñ

Quedando el comando final de la siguiente forma:

```bash
hbautista@war-machine:~$ nohup mplayer -shuffle -loop 0 bond/*.mp3 &
```

  Y con esto logramos el cometido: Reproducir de forma aleatoria y de forma indefinida los archivos .mp3 que se encuentren en el directorio bond dentro de la carpeta del usuario, lo haga en segundo plano aún si dicho usuario cierra sesión.

 [1]: /images/2012/alsaequal-1.png
