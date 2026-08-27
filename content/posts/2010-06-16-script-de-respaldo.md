---
title: Script de respaldo
date: 2010-06-16 21:21:59+00:00
slug: script-de-respaldo
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- 7Zip
- Cómos
- Debian
- Gnu/Linux
- Scripts
- Tips
aliases:
- /2010/06/16/script-de-respaldo/
- /comos/script-de-respaldo/
---

Este script lo hice hace ya un buen tiempo y que ayer estaba modificándolo y a partir de éste crear otros, que finalmente en un descuido borré todo mi home y con los scripts igual..

Como lo he mencionado varias veces google es el chamuko. ¿Porqué? Realicé una búsqueda porque recuerdo haber subido este script u alguno parecido en algún sitio y lo encontré ñ_ñ para mi fortuna puesto que no tenía en ningún lado respaldo de dicho script.

<!--more-->Lo publico por si a alguien le puede servir de guía o se encuentra en alguna situación como la mía y para que quede registrada la modificación que hice

```bash
#!/bin/sh
# Script pitero de respaldo de la BD del Serape
# serape.sh

# Hecho por: hbautista ;-)
# Fecha: 20 de Julio de 2006
# Modificado: 16 de Junio de 2010 porque lo borré :-(
# http://hbautista.com

# Mensaje de inicio
echo -e "\nIniciando Script"

# Aqui vemos la fecha y hora de ejecucion de este script, nuestras variables
# Dia_Mes_Año_Hora_Minuto
fecha=$(date +%d%B%Y-%H.%M)

# Para saber el mes en el que estamos
mes=$(date +%B)

# El año
anio=$(date +%Y)

# Nombre de la BD
nombre="Serape_$fecha.mdb"

#Aqui es donde definimos que se cree las carpetas por mes
carpeta="/home/respaldos/Serape/$anio/$mes"
carpeta2="/home/respaldos/Serape/$anio"

# Verificamos que la carpeta del año esté creada
if [ -d "$carpeta2" ]; then
echo -e "\nDirectorio $carpeta2 ya creado"
else
echo -e "\nCreando $carpeta2"
mkdir $carpeta2
fi

# Comparamos que la carpeta final existe, de otro modo se crea
if [ -d "$carpeta" ]; then
echo -e "\nDirectorio $carpeta ya creado"
else
echo -e "\nCreando $carpeta"
mkdir $carpeta
fi

#Aqui copiamos la bd a la carpeta destino, despues "entramos" a esa carpeta
cp /home/serape/Serape.mdb $carpeta
cd $carpeta
#Renombramos la bd para que incluya fecha y hora de ejecucion del script
mv Serape.mdb $nombre
#Comprimimos la bd renombrada con 7zip, que tiene el nivel de compresion mas alto.
7za a -bd -y -mx=5 $nombre.7z $nombre
#Eliminamos la bd de datos original
rm -f $nombre

# Mensaje final
echo -e "\nTerminado"
```

El nombre que le asigné se llama **serape.sh** y le asigné permisos de ejecución y lo copié a **/usr/local/bin** y además lo tengo en el **cron** para que lo haga del diario.

Nota: Uso **7zip** porque me pareció adecuado debido a que es un che archivito .mdb, aunque claro si quisieran más de un archivo y conservar permisos de usuario y de archivo es más recomendable usar tar
