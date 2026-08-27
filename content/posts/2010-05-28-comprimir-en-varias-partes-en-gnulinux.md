---
title: Comprimir en varias partes en Gnu/Linux
date: 2010-05-28 19:47:57+00:00
slug: comprimir-en-varias-partes-en-gnulinux
categories:
- Cómos
- Debian
- Gnu/Linux
tags:
- Cómos
- Debian
- Gnu/Linux
- Tips
- Ubuntu
aliases:
- /2010/05/28/comprimir-en-varias-partes-en-gnulinux/
- /comos/comprimir-en-varias-partes-en-gnulinux/
---

Sucede que ando migrando algunas cosas de un servidor a otro y tengo la necesidad de hacer un archivo comprimido por eso de los permisos y así además de que ocupa un poco menos de espacio y es más chido descargar un solo archivo (o pocos si son varias carpetas) a chingomil \*_\*

Dense una idea de una de las carpetas a respaldar:

```bash
[root@server1 somewhere]# du -sh trabajal/
5.7G    trabajal/
[root@server1 somewhere]#
```

<!--more-->Así que pues el clásico comando para dejar un 

**.tar.gz** es realizar lo siguiente:

```bash
[root@server1 somewhere]# tar czvf trabajal.tar.gz trabajal/
```

Después de un buen tiempo te deja el archivo **trabajal.tar.gz**

```bash
[root@server1 somewhere]# ls -lh
-rw-r--r--  1 root root 5.1G  may 28 10:58 trabajal.tar.gz
[root@server1 somewhere]#
```

La cuestión es que tuve la necesidad de ponerlo en una carpeta del servidor web apache para después descargarmelo con un wget y nomás no se pudo debido a que el archivo generado es superior a 2GB, luego entonces hay que comprimir (en esta segunda ocasión usando Bz2) y partir el archivo que en este caso los dejé de 1.8GB para evitar complicaciones, entonces para hacer esto usaremos **tar** y **split**.

```bash
[root@server1 somewhere]# tar cvj trabajal/ |split -b 1800m -d - trabajal.tbz.
```

Al igual que el anterior se tarda un rato en hacer el proceso y nos deja en este caso concreto 3 archivitos bien bonitos y empacaditos u_U

Veamos:

```bash
[root@server1 somewhere]# du -c trabajal.tbz.0*
1845004 trabajal.tbz.00
1845004 trabajal.tbz.01
1656504 trabajal.tbz.02
5346512 total
[root@server1 somewhere]# du -ch trabajal.tbz.0*
1.8G    trabajal.tbz.00
1.8G    trabajal.tbz.01
1.6G    trabajal.tbz.02
5.1G    total
[root@server1 somewhere]#
```

Es el mismo comando, la diferencia con el segundo es el "h" para que en lugar de tanto numeraje salga el espacio en **M** (Megas) o **G** (Gigas)

Y bueno, ahora si queda descargar los archivos y unirlos usando para esto **cat**:

```bash
[root@server1 somewhere]# cat trabajal.tbz.00 trabajal.tbz.01 trabajal.tbz.02 > trabajal.tbz2
```

También podemos unirlos usando el siguiente comando:

```bash
[root@server1 somewhere]# cat trabajal* > trabajal.tbz2
```

Una vez que tengamos el archivo **trabajal.tbz2** pues toca descomprimirlo:

```bash
[root@server1 somewhere]# tar -xvf trabajal.tbz2
```

Y eso es todo D:
