---
title: Admin CFDI en Debian
date: 2015-03-19 14:20:57+00:00
slug: admin-cfdi-en-debian
image: /images/2018/Admin_CFDI_01.png
categories:
- Gnu/Linux
tags:
- CFDI
- Cómos
- Debian
- Facturación
- Facturas
- Howto
- Howtos
- SAT
aliases:
- /2015/03/19/admin-cfdi-en-debian/
- /linux/admin-cfdi-en-debian/
---

<h2 style="text-align: center;">
  ¿Qué es Admin CFDI?
</h2>

  Es una herramienta para descargar facturas CFDI desde el SAT (tanto emitidas como recibidas), de uno o más correos electrónicos, organizar, validar y reportar facturas CFDI desde directorios.

  Los creadores son de <a title="Factura Libre" href="https://facturalibre.net/servicios/" target="_blank" rel="noopener">Factura Libre</a> que vienen desarrollando esta poderosa herramienta desde hace ya un tiempo.

  Tomado de la página del proyecto:

  Esta herramienta te permite realizar las siguientes acciones:

<li style="text-align: justify;">
  Descargar facturas (CFDI) emitidas o recibidas directamente del SAT.
</li>
<li style="text-align: justify;">
  Descargar facturas (CFDI) recibidas de uno o más correos electrónicos.
</li>
<li style="text-align: justify;">
  Organizar las facturas (CFDI) en carpetas por emisor o receptor, año y mes.
</li>
<li style="text-align: justify;">
  Generar PDFs de facturas (CFDI) usando una plantilla ODS de Calc de LibreOffice
</li>
<li style="text-align: justify;">
  Generar un reporte de facturas (CFDI), así como validar los sellos y su estatus en el SAT
</li>

El desarrollo y últimas versiones del proyecto se están llevando en Github.

Requerimientos:

  * Python 3.4
  * Tk si usas Linux, si usas Windows ya lo integra Python
  * Firefox para la automatización de la descarga del SAT
  * Selenium para la automatización de la descarga del SAT
  * PyGubu para la interfaz gráfica.
  * ReportLab si usas una plantilla JSON (por implementar)
  * LibreOffice si usas la plantilla ODS
  * Extensiones win32 para Python si usas Windows

Tanto en la página del proyecto como en el <a title="Administrar CFDI" href="http://blog.facturalibre.net/stories/admin-cfdi2.html" target="_blank" rel="noopener">sitio</a> del buen <a title="Linuxman" href="http://linuxmanr4.com/2015/01/20/descargar-los-xml-del-sat-de-una-manera-mas-sencilla/" target="_blank" rel="noopener">Linuxman</a>, encontrarán información para la instalación de lo necesario para que funcione.

En el caso particular de Debian, viene Python 2.7 por default, así que es necesario instalar los paquetes necesarios para que funcione.

root@kenobi:/home/hbautista# aptitude install python3-tk python3-pip python3-uno</pre>

Hay que tener instalado LibreOffice y Firefox además de los paquetes que se acaban de instalar. Una vez instaladas las dependencias, procedemos a instalar con pip, selenium y pygubu:

root@kenobi:/home/hbautista# pip3 install selenium pygubu</pre>

Tanto la instalación de paquetes con apt-get o aptitude, como los que se instalan con pip3, debe hacerse como root.

Descargar versión más reciente de producción: [AdminCFDI v0.2.2][1] (**567**).

Como usuario normal, procedemos a ejecutar Admin CFDI en el directorio en dónde hayamos extraído el contenido de AdminCFDI:

hbautista@kenobi:~/AdminCFDI_v0.2.2$ python3 admincfdi.py</pre>

[

![](/images/2018/Admin_CFDI_01.png)

][2][

![](/images/2018/Admin_CFDI_02.png)

][3]

Y eso sería todo

Agradecimientos a <a title="Factura Libre" href="https://facturalibre.net/" target="_blank" rel="noopener">Factura Libre</a> y a <a title="Linuxman" href="http://linuxmanr4.com/" target="_blank" rel="noopener">Linuxman</a> por la ayuda prestada.

 [1]: https://facturalibre.net/download_test/6
 [2]: /images/2018/Admin_CFDI_01.png
 [3]: /images/2018/Admin_CFDI_02.png
