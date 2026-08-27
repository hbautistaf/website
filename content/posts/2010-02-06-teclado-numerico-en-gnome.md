---
title: Teclado numérico en Gnome
date: 2010-02-06 20:13:43+00:00
slug: teclado-numerico-en-gnome
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Debian
- Linux
- Problema
- Teclado
- Tips
aliases:
- /2010/02/06/teclado-numerico-en-gnome/
- /comos/teclado-numerico-en-gnome/
---

Ya me había pasado esto hace tiempo y buscando le encontré. 🙂

Resulta que algo presioné, alguna actualización o que se yo, que de repente el teclado numérico de la pc dejó de funcionar en Gnome. 🙁 pero haciendo pruebas en la pantalla de login de GDM y en la terminal funcionaba bien :S

Primeras pruebas:

  * Enciende el foquito del "Bloq Num" pero no "escribe" números, pero al oprimir una tecla (creo que el 1) aparece un menú contextual. Raro.
  * Desconecto el teclado fí­sicamente (es USB )
  * Despues de 1 minuto vuelvo a conectar el teclado.
  * Verificando casi tecla por tecla veo que únicamente el teclado numérico es el que no responde, ni siquiera el /, *, -, + solo la tecla "Intro" y obviamente el botoncito que enciende y apaga la luz (y que se supone activa y desactivo dicho teclado)
  * Nada.. el teclado no reacciona. Ni pex.. a cambiarlo.
  * Le conecto un teclado Ps/2, el otro ya lo habí­a desconectado.
  * Mismo problema, pero según yo ese teclado está en perfectas condiciones.
  * Pruebo el teclado "enfermo" en otra pc y ¡¡Oh!! funciona perfectamente incluí­do el teclado numérico.

Volvemos a estar más o menos como al principio, pero con más datos y con la certeza de que NO es el teclado.

Entonces reiniciemos completamente el sistema para ver si algo pasó.  
Ya a dos segundos de hacerlo se me ocurre checar la configuración del teclado en **Sistema** -> **Preferencias** -> **Teclado**

[Configurar teclado

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado1.png?fit=631%2C511&ssl=1" class="aligncenter size-medium wp-image-751" title="Configurar teclado" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado1.png?resize=300%2C242&ssl=1" alt="Configurar teclado" width="300" height="242" />][1]

 

Y luego le dí­ en **Distribuciones**

[Configurando distribuciones de teclado

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado2.png?fit=631%2C527&ssl=1" class="aligncenter size-medium wp-image-752" title="Configurando distribuciones de teclado" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado2.png?resize=300%2C250&ssl=1" alt="Configurando distribuciones de teclado" width="300" height="250" />][2]

 

Pues dije le modificaré al "Microsoft Natural" y reiniciaré el entorno gráfico. Y así­ lo hice, pero nada ocurrió, entonces decidí­ dejarlo como estaba

[Configurando distribuciones de teclado

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado2.png?fit=631%2C527&ssl=1" class="aligncenter size-medium wp-image-752" title="Configurando distribuciones de teclado" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado2.png?resize=300%2C250&ssl=1" alt="Configurando distribuciones de teclado" width="300" height="250" />][2]

 

Y volver a reiniciar el entorno gráfico. Pero sucede que checo mi teclado numérico que si funciona en el campo donde escribo mi nombre de usuario. Total que vuelvo a entrar a Gnome y nada.. el teclado numérico se rehusa a funcionar.

Ya viendo que efectivamente reiniciaré la máquina para ver si algo pudiese cambiar leo un enlace que me salió en la búsqueda a google sobre problemas con el teclado numérico. Y me encontré con esta serie de mensajes del [Grupo es.comp.os.linux.instalacion][3]

Especifí­camente este texto

> 

>   A mi lo que me ha pasado con gnome, es que tocando teclas se activa el<br /> teclado numérico para controlar el ratón. Me explico del teclado numérico<br /> solo funcionan las teclas con las flechas, esto sirve para utilizar el<br /> teclado numérico para controlar el cursor en lugar del ratón. Hay una<br /> opción en gnome para usarlo como ratón o no, me imagino que en kde también<br /> estará.
> 

Luego de ese mensaje vi este otro.

> 

>   Buenas. Pues si van por ahi los tiros. En KDE, los pasos a seguir para<br /> desactivar esta caracteristica son los siguientes:
> 

Entonces volví­ a abrir las preferencias del teclado y vi que estaba así­.

[Teclas del ratón

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado3.png?fit=631%2C511&ssl=1" class="aligncenter size-medium wp-image-753" title="Teclas del ratón" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado3.png?resize=300%2C242&ssl=1" alt="Teclas del ratón" width="300" height="242" />][4]

 

Bastó con desactivar esa opción para que quedará así­ y con eso se solucionó el problema.

 

[Teclas del ratón 2

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado4.png?fit=631%2C511&ssl=1" class="aligncenter size-medium wp-image-754" title="Teclas del ratón 2" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/10/Pant_teclado4.png?resize=300%2C242&ssl=1" alt="Teclas del ratón 2" width="300" height="242" />][5]

A final de cuentas el asunto era un tanto simple, pero ya ven la paranoia a veces resulta infructuosa 😡

Me pregunto ¿Soy tan paranoico que primero busqué algún desperfecto fí­sico? o ¿Soy de los que comunmente dejan al final verificar la configuración?

¿Qué habrí­a hecho usted, apreciable lector?

En fin.. un caso sospechoso que resulto en un conocimiento sobre este mundo de la informática y el software libre.

Lo sigo diciendo, siempres aprendes algo nuevo todos los dí­as. 😀

 [1]: /images/2011/Pant_teclado1.png
 [2]: /images/2011/Pant_teclado2.png
 [3]: http://groups.google.com/group/es.comp.os.linux.instalacion/browse_thread/thread/b9cccb1015fc1af5
 [4]: /images/2011/Pant_teclado3.png
 [5]: /images/2011/Pant_teclado4.png
