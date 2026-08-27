---
title: Sources.list de Squeeze
date: 2010-09-28 15:44:37+00:00
slug: sources-list-de-squeeze
image: /images/2011/debian-squeeze-two-454-1.jpg
categories:
- Cómos
- Debian
tags:
- Cómos
- Debian
- Gnu/Linux
- Tips
aliases:
- /2010/09/28/sources-list-de-squeeze/
- /comos/sources-list-de-squeeze/
---

Pues bueno, ya que lo necesitaré en breve, pongo acá mi sources.list para Debian Squeeze.

```bash
deb http://mmc.geofisica.unam.mx/debian/ squeeze main contrib
# deb-src http://mmc.geofisica.unam.mx/debian/ squeeze main

deb http://ftp.mx.debian.org/debian/ squeeze main
deb http://ftp.rediris.es/debian squeeze main contrib non-free
# deb-src http://ftp.mx.debian.org/debian/ squeeze main

deb http://security.debian.org/ squeeze/updates main
# deb-src http://security.debian.org/ squeeze/updates main

# Google software repository
# deb http://dl.google.com/linux/deb/ stable non-free

#Debian Multimedia
deb http://www.debian-multimedia.org squeeze main non-free

# Google testing repository
deb http://dl.google.com/linux/deb/ testing non-free

#Opera for Debian Lenny
deb http://deb.opera.com/opera/ squeeze non-free

# Skype
deb http://download.skype.com/linux/repos/debian/ stable non-free

## Thí¨mes du projet bisigi
deb http://ppa.launchpad.net/bisigi/ppa/ubuntu jaunty main
```

Luego hay que hacer

```bash
root@soporte:/home/hbautista# aptitude update
```

Y dependiendo un:

```bash
root@soporte:/home/hbautista# aptitude safe-ugrade
```

Y un:

```bash
root@soporte:/home/hbautista# aptitude full-upgrade
```

🙂
