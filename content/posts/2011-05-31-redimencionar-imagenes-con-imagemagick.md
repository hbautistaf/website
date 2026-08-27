---
title: Redimensionar imágenes con Imagemagick
date: 2011-05-31 20:29:17+00:00
slug: redimencionar-imagenes-con-imagemagick
image: /images/2011/Imagemagick-logo.png
categories:
- Cómos
- Gnu/Linux
tags:
- Bash
- Cómos
- Consola
- Debian
- Fotografía
- Fotos
- Howtos
- ImageMagick
- Imágenes
- Scripts
- Terminal
- Tips
aliases:
- /2011/05/31/redimencionar-imagenes-con-imagemagick/
- /comos/redimencionar-imagenes-con-imagemagick/
---

Hace ya un buen tiempo en mi blog anterior había hecho algunos scripts para reducir de tamaño las imágenes que subía en Flickr o en ese blog.

Como ese blog pasó a la historia junto con los artículos que tenía, las dos entradas relacionadas con lo mismo desaparecieron. Hace como una semana me preguntaron el porqué no escribo tan seguido y comenté que principalmente porque a veces no encuentro sobre qué escribir.

Y de ahí surgió el comentario sobre este tema y le mencioné que ya había resuelto ese detalle, aunque ahora mismo ya no use dichos scripts.

Pues bien y después de rebuscar entre las cosas que tenía almacenadas por fin encontré no uno, sino varios scripts sobre el tema. Pondré los primeros que usaba y finalmente el que para mi gusto fue el que finalmente usé masivamente debido a que estaba más completo.

## Primeros scripts

 

El primero le puse el nombre de "achicar" y es:

```bash
#!/bin/bash
#
# Pequeño script que cambia la resolución de la imagenes (con extension PNG) al 27% del tamaño original.
# Realizado por: Hbautista, hbautista@usoli.org

for file in $( ls *.JPG ); do
convert $file -resize 27% foto_$file
done
echo “Listo!
```

Como verán es simple y tiene la limitante que sólo funciona con fotos que tengan la extensión jpg en mayúsculas, debido a que cuando pasaba las fotos de mi cámara a la computadora las tenía así.

Las fotos resultantes quedaban en el mismo directorio al igual que las originales, quedando las "nuevas" con "foto_" al inicio del nombre de cada archivo.

En el caso de pantallazos y otros archivos o fotos que tenían la extensión .png lo modifiqué resultando el script llamado "reducir":

```bash
#!/bin/bash
#
# Pequeño script que cambia la resolución de la imagenes (con extension PNG) al 50% del tamaño original.
# Realizado por: Hbautista, hbautista@usoli.org

for file in $( ls *.png ); do
convert $file -resize 50% foto_$file
done
echo “Listo!
```

Luego de eso y buscando un poco más usé durante un tiempo este otro que lo llamé "quitar-calidad":

```bash
#/usr/bin
mkdir pt
for N in *; do
convert -compress jpeg -quality 44 -enhance -font Bookman-DemiItalic  -fill white -pointsize 14 -draw "text 680,500 'hbautista'" $N pt/$N; done
ls -l pt/
```

Aquí ya no importaba la extensión y a diferencia de los dos primeros, en este caso lo que hacía era reducir la calidad al 44% de la imagen original, crear un subdirectorio dentro del directorio en donde se ejecutase el script y añadir la marca de agua "hbautista.usoli.org" en las fotografías y poniendo las reducidas y con la marca de agua en el subdirectorio "pt".

[foto_coapilla

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_coapilla-1.jpg?fit=648%2C486&ssl=1" class="aligncenter size-medium wp-image-579" title="foto_coapilla" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_coapilla-1.jpg?resize=300%2C225&ssl=1" alt="foto_coapilla" width="300" height="225" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_coapilla-1.jpg?resize=300%2C225&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_coapilla-1.jpg?resize=768%2C576&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_coapilla-1.jpg?w=1024&ssl=1 1024w" sizes="auto, (max-width: 300px) 100vw, 300px" />][1]

 

## Script final

 

Luego hice una mezcla de los primeros scripts con el último para que reduciera el tamaño y además le pusiera la marca de agua, pero digamos que era desperdicio de código porque nada más junte los tres scripts. Finalmente éste fue el script final que a mi gusto estaba bastante funcional, le puse el nombre de "blogfoto":

```bash
#!/bin/bash
# blogfoto
# Pequeño script que cambia la resolución de la imagenes del tamaño original a 800*600. Usa ImageMagick
# Además de reducir la calidad de la imagen resultante.
# Realizado por: Hbautista, hbautista@usoli.org
# http://blog.hbautista.com/linux/redimencionar-imagenes-con-imagemagick/

# Primero nos aseguramos que la extensión esté en minúsculas y creamos fotoblog
rename 's/.JPG/.jpg/' *.JPG
mkdir fotoblog

#Empezamos el ciclo con las fotos de extensión jpg para reducirlo a 800*600.
#Además de poner las fotos dentro de fotoblog

for file in $( ls *.jpg ); do
convert -size 2048x1536 $file -thumbnail 800x600 fotoblog/foto_$file
done
echo “Listo!

# Ahora procedemos a comprimir más las imágenes dentro de fotoblog
cd fotoblog
for N in *; do
convert -compress jpeg -quality 55 -enhance -font Bookman-DemiItalic  -fill white -pointsize 14 -draw "text 680,500 'hbautista'" $N $N;
done
echo "Hemos terminado!"
```

Ahora bien, primeramente usando el comando rename pasamos de mayúsculas a minúsculas las extensiones, si es que están así. Creamos el directorio "fotoblog" y hacemos que las fotos sean reducidas a un tamaño de 800×600 y queden con el nombre de foto_loquesea.jpg dentro de ese directorio.

 

Una vez que haya terminado ese proceso que depende de cuántas fotografías estén dentro del directorio lo que hace es que accede al directorio fotoblog y ahí procede a añadirle la marca de agua.

## ¿Cómo usar el script?

foto_chiapatuit

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_chiapatuit-1.jpg?fit=648%2C496&ssl=1" class="aligncenter size-medium wp-image-580" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_chiapatuit-1.jpg?resize=300%2C230&ssl=1" alt="" width="300" height="230" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_chiapatuit-1.jpg?resize=300%2C230&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_chiapatuit-1.jpg?resize=768%2C588&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_chiapatuit-1.jpg?w=1024&ssl=1 1024w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Copiar el contenido del script final (blogfoto) en tu editor de texto favorito y adecuarlo a tus necesidades, es decir cambiar el nombre del subdirectorio, el tipo de letra o cambiar el texto de la marca de agua y guardarlo con el nombre de "loquesea.sh" para este ejemplo lo dejaré con el nombre original **blogfoto.sh** y lo dejaré en el directorio raíz de mi /home para luego como root copiarlo a /usr/local/bin y darle los respectivos permisos de ejecución:

Pant_script_foto

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_script_foto-1.png?fit=648%2C316&ssl=1" class="aligncenter size-medium wp-image-582" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_script_foto-1.png?resize=300%2C147&ssl=1" alt="" width="300" height="147" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_script_foto-1.png?resize=300%2C147&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_script_foto-1.png?resize=768%2C375&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_script_foto-1.png?w=944&ssl=1 944w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

```bash
root@luke:/home/hbautista# cp blogfoto.sh /usr/local/bin/
root@luke:/home/hbautista# chmod +x /usr/local/bin/blogfoto.sh
root@luke:/home/hbautista#
```

Luego con tu usuario normal ubicarte en el directorio que tiene las fotos y ejecutar el script:

Pant_scriptfoto2

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_scriptfoto2-1.png?fit=648%2C316&ssl=1" class="aligncenter size-medium wp-image-583" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_scriptfoto2-1.png?resize=300%2C147&ssl=1" alt="" width="300" height="147" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_scriptfoto2-1.png?resize=300%2C147&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_scriptfoto2-1.png?resize=768%2C375&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/Pant_scriptfoto2-1.png?w=944&ssl=1 944w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

```bash
hbautista@luke:~$ cd Imágenes/Taller_Foto/
hbautista@luke:~/Imágenes/Taller_Foto$ blogfoto.sh
Can't rename *.JPG *.jpg: No existe el fichero o el directorio
“Listo!
Hemos terminado!
hbautista@luke:~/Imágenes/Taller_Foto$
```

El resultado se ve como esto:

[Luces

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_dsc07862-1.jpg?fit=648%2C434&ssl=1" class="aligncenter size-medium wp-image-581" title="Luces" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_dsc07862-1.jpg?resize=300%2C201&ssl=1" alt="Luces" width="300" height="201" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_dsc07862-1.jpg?resize=300%2C201&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_dsc07862-1.jpg?resize=768%2C515&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/05/foto_dsc07862-1.jpg?w=800&ssl=1 800w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2]

Espero que les sirva

Enlaces:

Jugando con Imagemagick

<a title="ImageMagick manipulando centenares de imagenes" href="http://bit.ly/mrOOFK" target="_blank" rel="noopener">ImageMagick manipulando centenares de imágenes</a>

 [1]: /images/2011/foto_coapilla-1.jpg
 [2]: /images/2011/foto_dsc07862-1.jpg
