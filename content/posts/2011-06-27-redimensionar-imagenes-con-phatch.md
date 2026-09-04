---
title: Redimensionar imagenes con Phatch
date: 2011-06-27 20:46:19+00:00
slug: redimensionar-imagenes-con-phatch
image: /images/2011/Phatch-1.png
categories:
- Gnu/Linux
tags:
- Cómos
- Debian
- Fotografía
- Fotos
- Howto
- Phatch
- Photography
aliases:
- /2011/06/27/redimensionar-imagenes-con-phatch/
- /linux/redimensionar-imagenes-con-phatch/
---

Escribí hace poco el cómo <a title="Redimensionar imagenes con ImageMagick" href="http://blog.hbautista.com/linux/redimencionar-imagenes-con-imagemagick/" target="_blank" rel="noopener">redimensionar imágenes con ImageMagick</a> desde la línea de comando y crear un script exprofeso para ello.

Pero para aquellos que no quieran usar la consola y prefieran una herramienta gráfica para ello, pues les presento <a title="Photo Batch" href="http://photobatch.stani.be/" target="_blank" rel="noopener">Photo Batch Processor</a> o Phatch (Phatch = Photo & Batch!) de forma abreviada.

Phatch

" data-image-caption="" data-large-file="/images/2011/Phatch-1.png" class="aligncenter size-medium wp-image-610" src="/images/2011/Phatch-1.png" alt="" width="300" height="167" srcset="/images/2011/Phatch-1.png 300w, /images/2011/Phatch-1.png 768w, /images/2011/Phatch-1.png 769w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

> Phatch es fácil de usar, Procesador de Fotos multi-plataforma y un editor de datos EXIF con una bonita interfaz gráfica de usuario. Phatch maneja todos los formatos de imágen y puede duplicar las jerarquías de (sub) carpetas. Phatch puede procesar por tamaño, rotar, aplicar sombras, perspectiva, redondear esquinas, etc y muchas más acciones en minutos en lugar de horas o días si se hiciera de forma manual.

Al ser multiplataforma pueden usarlo en Hasefroch, Mac y obviamente Gnu/Linux.

Para ser instalado en Debian/Ubuntu se puede hacer desde la consola escribiendo:

```bash
root@luke:/home/hbautista# aptitude install phatch
```

Una vez instalado se lanza la aplicación desde **Aplicaciones** -> **Gŕaficos** – **Phatch Procesador de fotografías por lotes**

Iniciando Phatch

" data-image-caption="" data-large-file="/images/2011/Pant_phatch00-1.png" class="aligncenter size-medium wp-image-611" src="/images/2011/Pant_phatch00-1.png" alt="" width="300" height="281" srcset="/images/2011/Pant_phatch00-1.png 300w, /images/2011/Pant_phatch00-1.png 657w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Una vez que el programa se inicie nos toparemos con su pantalla principal:

Phatch 1

" data-image-caption="" data-large-file="/images/2011/Pant_phatch1-1.png" class="aligncenter size-medium wp-image-612" src="/images/2011/Pant_phatch1-1.png" alt="" width="225" height="300" srcset="/images/2011/Pant_phatch1-1.png 225w, /images/2011/Pant_phatch1-1.png 402w" sizes="auto, (max-width: 225px) 100vw, 225px" /> 

Basta aclarar que el programa hará en un proceso por lotes, las "**acciones**" que nosotros le indiquemos que haga y en el orden preestablecido. Es decir si le decimos que haga 3 acciones, la primera que sea "redimensionar" luego "**guardar**" y por último "a**plicar redondeado**" basta decir que ésto último no lo veremos en el resultado final, puesto que la acción "guardar" es puesta antes.

Con esto quiero decir que sean 2 o más "acciones" que pongan, asegúrense que la última sea la de "**guardar**" pues será ahí donde se complete el proceso.

Una vez terminadas de definir las acciones que queremos realizar, éstas se aplican a una o más fotografías o bien a toda una carpeta completa y si tiene "subcarpetas" también pueden ser aplicadas.

Si aún tienen dudas, veremos que **Phatch** tiene acciones "pre-establecidas" que podemos usar para acciones concretas:

[Acciones predefinidas

" data-image-caption="" data-large-file="/images/2011/Pant_phatch2-1.png" class="aligncenter size-medium wp-image-618" title="Acciones predefinidas" src="/images/2011/Pant_phatch2-1.png" alt="Acciones predefinidas" width="300" height="245" srcset="/images/2011/Pant_phatch2-1.png 300w, /images/2011/Pant_phatch2-1.png 688w" sizes="auto, (max-width: 300px) 100vw, 300px" />][1]

Ahora bien escogeremos "Perspective Reflection":

[Perspective reflection

" data-image-caption="" data-large-file="/images/2011/Pant_phatch3-1.png" class="aligncenter size-medium wp-image-617" title="Perspective reflection" src="/images/2011/Pant_phatch3-1.png" alt="Perspective reflection" width="300" height="245" srcset="/images/2011/Pant_phatch3-1.png 300w, /images/2011/Pant_phatch3-1.png 688w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2]

Veremos que tiene un total de 5 acciones, siendo como lo comentaba **Guardar** la última.

Acciones perspective

" data-image-caption="" data-large-file="/images/2011/Pant_phatch4-1.png" class="aligncenter size-medium wp-image-619" src="/images/2011/Pant_phatch4-1.png" alt="" width="225" height="300" srcset="/images/2011/Pant_phatch4-1.png 225w, /images/2011/Pant_phatch4-1.png 402w" sizes="auto, (max-width: 225px) 100vw, 225px" /> 

 

Podemos apreciar cada una de las acciones que hacen y cambiar los valores si así lo queremos

Acciones perspectiva 1

" data-image-caption="" data-large-file="/images/2011/Pant_phatch5-1.png" class="alignnone size-medium wp-image-620" src="/images/2011/Pant_phatch5-1.png" alt="" width="160" height="300" srcset="/images/2011/Pant_phatch5-1.png 160w, /images/2011/Pant_phatch5-1.png 399w" sizes="auto, (max-width: 160px) 100vw, 160px" />Acciones perspectiva 2

" data-image-caption="" data-large-file="/images/2011/Pant_phatch6-1.png" class="alignnone size-medium wp-image-621" src="/images/2011/Pant_phatch6-1.png" alt="" width="160" height="300" srcset="/images/2011/Pant_phatch6-1.png 160w, /images/2011/Pant_phatch6-1.png 399w" sizes="auto, (max-width: 160px) 100vw, 160px" /> 

 

A un lado del botón **Abrir**, se encuentra el botón **Ejecutar** con el cual se procede a ejecutar las acciones sobre una carpeta o bien sobre una o más fotografías.

[Ejecutar Phatch

" data-image-caption="" data-large-file="/images/2011/Pant_phatch01-1.png" class="aligncenter size-full wp-image-616" title="Ejecutar Phatch" src="/images/2011/Pant_phatch01-1.png" alt="Ejecutar Phatch" width="378" height="74" srcset="/images/2011/Pant_phatch01-1.png 378w, /images/2011/Pant_phatch01-1.png 300w" sizes="auto, (max-width: 378px) 100vw, 378px" />][3]

En este caso lo haremos sobre una carpeta:

[Escogiendo carpeta

" data-image-caption="" data-large-file="/images/2011/Pant_phatch7-1.png" class="aligncenter size-medium wp-image-623" title="Escogiendo carpeta" src="/images/2011/Pant_phatch7-1.png" alt="Escogiendo carpeta" width="300" height="187" srcset="/images/2011/Pant_phatch7-1.png 300w, /images/2011/Pant_phatch7-1.png 588w" sizes="auto, (max-width: 300px) 100vw, 300px" />][4]

En el explorador vemos a cuántos elementos se aplicarán las acciones:

[Archivos para procesar

" data-image-caption="" data-large-file="/images/2011/Pant_phatch8-1.png" class="aligncenter size-medium wp-image-624" title="Archivos para procesar" src="/images/2011/Pant_phatch8-1.png" alt="Archivos para procesar" width="300" height="267" srcset="/images/2011/Pant_phatch8-1.png 300w, /images/2011/Pant_phatch8-1.png 602w" sizes="auto, (max-width: 300px) 100vw, 300px" />][5]

Y vemos como se van aplicando los cambios en los archivos que se encuentran dentro de la carpeta que antes elegimos.

Procesando archivos con Phatch

" data-image-caption="" data-large-file="/images/2011/Pant_phatch9-1.png" class="size-medium wp-image-625 aligncenter" src="/images/2011/Pant_phatch9-1.png" alt="" width="300" height="96" srcset="/images/2011/Pant_phatch9-1.png 300w, /images/2011/Pant_phatch9-1.png 638w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Te avisa en cuanto haya terminado el proceso

[Listo!

" data-image-caption="" data-large-file="/images/2011/Pant_phatch10-1.png" class="aligncenter size-full wp-image-626" title="Listo!" src="/images/2011/Pant_phatch10-1.png" alt="Listo!" width="241" height="94" />][6]

Aquí vemos un par de fotografías que fueron procesadas usando las opciones predefinidas en **Perspective Reflection**:

Luces

" data-image-caption="" data-large-file="/images/2011/dsc07862-1.png" class="alignnone size-medium wp-image-638" src="/images/2011/dsc07862-1.png" alt="" width="264" height="300" srcset="/images/2011/dsc07862-1.png 264w, /images/2011/dsc07862-1.png 556w" sizes="auto, (max-width: 264px) 100vw, 264px" />Abril

" data-image-caption="" data-large-file="/images/2011/dsc09712-1.png" class="alignnone size-medium wp-image-639" src="/images/2011/dsc09712-1.png" alt="" width="264" height="300" srcset="/images/2011/dsc09712-1.png 264w, /images/2011/dsc09712-1.png 556w" sizes="auto, (max-width: 264px) 100vw, 264px" /> 

Ahora bien, únicamente usamos acciones predefinidas que ya se encontraban junto al programa. Crearemos una lista de tan sólo 3 acciones que es la que uso para la mayoría de las fotos que subo acá en el blog.

Primeramente en el menú principal hacemos clic en el **Más** (+) que indica añadir una acción, de la lista que aparece usaremos la de **Escalar**:

Acción Escalar

" data-image-caption="" data-large-file="/images/2011/Pant_phatch11-1.png" class="size-medium wp-image-628 aligncenter" src="/images/2011/Pant_phatch11-1.png" alt="" width="212" height="300" srcset="/images/2011/Pant_phatch11-1.png 212w, /images/2011/Pant_phatch11-1.png 402w" sizes="auto, (max-width: 212px) 100vw, 212px" /> 

Y una vez hecho eso, veremos las opciones de esas acciones, en mi caso los cambios quedaron en que el tamaño de las imágenes fuera de 800×600 pixeles

Acción Escalar 2

" data-image-caption="" data-large-file="/images/2011/Pant_phatch12-1.png" class="size-medium wp-image-629 aligncenter" src="/images/2011/Pant_phatch12-1.png" alt="" width="169" height="300" srcset="/images/2011/Pant_phatch12-1.png 169w, /images/2011/Pant_phatch12-1.png 402w" sizes="auto, (max-width: 169px) 100vw, 169px" /> 

Luego añadimos la acción de **Texto**:

Acción Texto

" data-image-caption="" data-large-file="/images/2011/Pant_phatch13-1.png" class="aligncenter size-medium wp-image-630" src="/images/2011/Pant_phatch13-1.png" alt="" width="212" height="300" srcset="/images/2011/Pant_phatch13-1.png 212w, /images/2011/Pant_phatch13-1.png 402w" sizes="auto, (max-width: 212px) 100vw, 212px" /> 

Y ahí modifiqué el texto que de forma predefinida es Phatch y que yo cambié por **hbautista**, además del tipo de letra, tamaño y en qué posición debe de estar ese texto.

Acción Texto 2

" data-image-caption="" data-large-file="/images/2011/Pant_phatch14-1.png" class="aligncenter size-medium wp-image-631" src="/images/2011/Pant_phatch14-1.png" alt="" width="212" height="300" srcset="/images/2011/Pant_phatch14-1.png 212w, /images/2011/Pant_phatch14-1.png 505w" sizes="auto, (max-width: 212px) 100vw, 212px" /> 

Y por último añadir la acción de **Guardar**

Acción Guardar

" data-image-caption="" data-large-file="/images/2011/Pant_phatch15-1.png" class="aligncenter size-medium wp-image-632" src="/images/2011/Pant_phatch15-1.png" alt="" width="212" height="300" srcset="/images/2011/Pant_phatch15-1.png 212w, /images/2011/Pant_phatch15-1.png 402w" sizes="auto, (max-width: 212px) 100vw, 212px" /> 

Ahí también podemos cambiar las opciones para que se adapten a nuestras necesidades

[Opciones Guardar

" data-image-caption="" data-large-file="/images/2011/Pant_phatch16-1.png" class="aligncenter size-medium wp-image-634" title="Opciones Guardar" src="/images/2011/Pant_phatch16-1.png" alt="Opciones Guardar" width="213" height="300" srcset="/images/2011/Pant_phatch16-1.png 213w, /images/2011/Pant_phatch16-1.png 506w" sizes="auto, (max-width: 213px) 100vw, 213px" />][7]

Cuando hayamos acabado de hacer los cambios respectivos, pruebas de ejecución para que el resultado sea el deseado, hay que guardar los cambios para tener disponible estas acciones en un futuro.

[Guardar como

" data-image-caption="" data-large-file="/images/2011/Pant_phatch17-1.png" class="aligncenter size-medium wp-image-635" title="Guardar como" src="/images/2011/Pant_phatch17-1.png" alt="Guardar como" width="170" height="300" srcset="/images/2011/Pant_phatch17-1.png 170w, /images/2011/Pant_phatch17-1.png 402w" sizes="auto, (max-width: 170px) 100vw, 170px" />][8]

Le asignamos un nombre (**reducir**) y de preferencia en el directorio que viene predefinido (_~user/.local/share/phatch/actionlists_) y clic en Guardar.

Guardando

" data-image-caption="" data-large-file="/images/2011/Pant_phatch18-1.png" class="aligncenter size-medium wp-image-636" src="/images/2011/Pant_phatch18-1.png" alt="" width="300" height="203" srcset="/images/2011/Pant_phatch18-1.png 300w, /images/2011/Pant_phatch18-1.png 768w, /images/2011/Pant_phatch18-1.png 1024w, /images/2011/Pant_phatch18-1.png 1106w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Y así se vería  nuestras acciones una vez terminado el proceso.

[Reducir

" data-image-caption="" data-large-file="/images/2011/Pant_phatch19-1.png" class="aligncenter size-medium wp-image-637" title="Reducir" src="/images/2011/Pant_phatch19-1.png" alt="Reducir" width="170" height="300" srcset="/images/2011/Pant_phatch19-1.png 170w, /images/2011/Pant_phatch19-1.png 402w" sizes="auto, (max-width: 170px) 100vw, 170px" />][9]

Espero que saquen mucho más provecho de este excelente programa para trabajar con muchas imágenes de forma cómoda y sencilla.

 [1]: /images/2011/Pant_phatch2-1.png
 [2]: /images/2011/Pant_phatch3-1.png
 [3]: /images/2011/Pant_phatch01-1.png
 [4]: /images/2011/Pant_phatch7-1.png
 [5]: /images/2011/Pant_phatch8-1.png
 [6]: /images/2011/Pant_phatch10-1.png
 [7]: /images/2011/Pant_phatch16-1.png
 [8]: /images/2011/Pant_phatch17-1.png
 [9]: /images/2011/Pant_phatch19-1.png
