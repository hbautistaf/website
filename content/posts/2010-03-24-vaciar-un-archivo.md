---
title: Vaciar un archivo
date: 2010-03-24 15:43:24+00:00
slug: vaciar-un-archivo
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Debian
- Gnu/Linux
- Tips
aliases:
- /2010/03/24/vaciar-un-archivo/
- /comos/vaciar-un-archivo/
---

Sucede que el día de hoy me encuentro con que los dos servidores proxy que tenemos andan fallando :S

Reviso y veo que hay muchos archivos para ser eliminados, hasta que veo esto:

```bash
proxy2:/home/hbautista# du -sh /var/mail/*
6.2G    /var/mail/hbautista
proxy2:/home/hbautista#
```

<!--more-->Entonces me toca eliminar el contenido del archivo sin eliminar dicho archivo, es decir solo su contenido.

Existen 3 formas de lograr esto:

```bash
proxy2:/home/hbautista# > /var/mail/hbautista
```

Otra manera, redirigiendo a **/dev/null**:

```bash
proxy2:/home/hbautista# cat /dev/null /var/mail/hbautista
```

O copiando el “archivo vacío” **/dev/null** machando el que tenemos:

```bash
proxy2:/home/hbautista# cp /dev/null /var/mail/hbautista
```

En cualquiera de los 3 casos el resultado se vería así:

```bash
proxy2:/home/hbautista# du -sh /var/mail/*
0	/var/mail/hbautista
```

Y eso es todo (^_^) espero que les haya servido como a mi 😉
