---
title: Configurando y usando OpenSSH en CentOS 7
date: 2018-04-17 13:39:26+00:00
slug: configurando-y-usando-openssh-en-centos-7
image: /wp-content/uploads/2018/04/Secure_Shell.png
categories:
- Gnu/Linux
tags:
- CentOS
- Debian
- Linux
- OpenSSH
- Red Hat
- Secure Shell
- SSH
aliases:
- /2018/04/17/configurando-y-usando-openssh-en-centos-7/
- /linux/configurando-y-usando-openssh-en-centos-7/
---

![SSH Logo](/wp-content/uploads/2018/04/SSH_Logo.png)

El escenario es el siguiente, <a href="https://www.centos.org" target="_blank" rel="noopener">**CentOS 7**</a> recién instalado con **OpenSSH** instalado y configurado por default y **SELinux** desactivado.

  Aunque usemos contraseñas con 20 o 30 caracteres usando caracteres especiales y todo eso, siempre es mejor el uso de llaves y cambiar algunos valores en el servidor al que nos queremos conectar.

  Para generar una clave SSH en Linux usando el comando **ssh-keygen** deberías ejecutarlo usando la línea de comandos, esto se hace desde el cliente:

```bash
perengao@elrond:~$ ssh-keygen -t rsa -b 4096 -C "perengano@gmail.com"  
Generating public/private rsa key pair.  
Enter file in which to save the key (/home/perengano/.ssh/id_rsa):  
Created directory '/home/perengano/.ssh'.  
Enter passphrase (empty for no passphrase):  
Enter same passphrase again:  
Your identification has been saved in /home/perengano/.ssh/id_rsa.  
Your public key has been saved in /home/perengano/.ssh/id_rsa.pub.  
The key fingerprint is:  
SHA256:1AfAgsKI7fv/9h0dTHkUccMR2bwD+XkUcBQbWOaq/LA perengano@gmail.com  
The key's randomart image is:  
+—[RSA 4096]—-+  
|.+ . …. .B/%|  
|o + . . .. . ++=O|  
| . . .. . . =++|  
| . . . o.*.|  
| . S .o o|  
| . . .. . |  
| . +. . |  
| . . .+. |  
| ..o…E.. |  
+—-[SHA256]—–+  
perengano@elrond:~$ cat .ssh/id_rsa.pub
```

En este ejemplo no estoy usando una passphrase, pero se aconseja usar una.

Una vez que la llave ha sido generada, podemos copiarla al servidor destino usando el siguiente comando:

```bash
ssh-copy-id user@serverip
```

También pueden hacerlo usando copiar y pegar, subiendo el archivo con scp, etc.

```bash
perengano@elrond:~$ ssh-copy-id perengano@vpsmikel.ds  
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/perengano/.ssh/id_rsa.pub"  
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed  
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed — if you are prompted now it is to install the new keys  
perengano@vpsmikel.ds's password:

Number of key(s) added: 1

Now try logging into the machine, with: "ssh 'perengano@vpsmikel.ds'"  
and check to make sure that only the key(s) you wanted were added.

perengano@elrond:~$
```

  Ahora nos toca realizar lo siguiente del lado del servidor, primeramente dejar los permisos para que OpenSSH no nos de lata:

```bash
perengano@elrond:~$ ssh perengano@vpsmikel.ds  
perengano@vpsmikel.ds's password:  
Last login: Mon Apr 10 19:22:07 2018 from 189.201.191.13  
[perengano@B8GUsg ~]$ chmod 700 .ssh  
[perengano@B8GUsg ~]$ chmod 600 .ssh/authorized_keys  
[perengano@B8GUsg ~]$
```

  OpenSSH es muy quisquilloso con los permisos tanto del directorio como del archivo, en mi caso había hecho el segundo comando, pero no el primero y no me permitía loguearme con las llaves.

```bash
[perengano@B8GUsg ~]$ sudo su –  
[sudo] password for perengano:  
Último inicio de sesión:lun abr 16 21:40:02 EDT 2018en pts/0  
Último inicio de sesión fallido:lun abr 16 22:47:05 EDT 2018de 195.208.185.50en ssh:notty  
Hubo 2 intentos de logueo fallidos desde el último logueo exitoso.  
[root@B8GUsg ~]#
```

Ya como root, hacemos una copia de seguridad del archivo de configuración original y editamos:

```bash
[root@B8GUsg ~]# cp /etc/ssh/sshd\_config /etc/ssh/orig.sshd\_config  
[root@B8GUsg ~]# nano /etc/ssh/sshd_config
```

Y los valores que hay que cambiar son los siguientes

```vim
\# Desactivamos que root pueda loguearse usando ssh  
PermitRootLogin no

\# Estos valores nos permiten usar SSH keys en lugar de passwords  
RSAAuthentication yes  
PubkeyAuthentication yes

\# Desactivamos las contraseñas  
PasswordAuthentication no
```

Reiniciamos el servicio:

```bash
[root@B8GUsg ~]# systemctl restart sshd.service
```

  Nota: Abrir una segunda terminal o pestaña de terminal y desde ahí hacer pruebas, no te desconectes en caso de que algo no funcione como debe:

```bash
perengano@elrond:~$ ssh vpsmikel.ds  
Last login: Mon Apr 16 21:52:28 2018 from 189.201.191.13  
[perengano@B8GUsg ~]$
```

  Con eso deben tener todo listo para poder hacer uso de las llaves. Sin embargo, si quieren usar un cliente como Filezilla para copiar archivos y todo eso, necesitamos exportar nuestra llave. Esto lo podemos hacer usando <a href="https://the.earth.li/~sgtatham/putty/0.70/w64/puttygen.exe" target="_blank" rel="noopener">puttygen.exe</a>

Creo un directorio con los archivos generados al inicio:

```bash
perengano@elrond:~$ mkdir keys  
perengano@elrond:~$ cp .ssh/id_rsa keys  
perengano@elrond:~$ cp .ssh/id_rsa.pub keys
```

Vamos a usar Wine, si no lo tienen pueden instalarlo:

```bash
perengano@elrond:~$ sudo apt install wine wine-utils  
perengano@elrond:~$ cd keys  
perengano@elrond:~$ wine ../Descargas/puttygen.exe  
it looks like wine32 is missing, you should install it.  
as root, please execute "apt-get install wine32"
```

[Puttygen

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_puttygen.png?fit=483%2C463&ssl=1" class="alignnone size-medium wp-image-1450" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_puttygen.png?resize=300%2C288&ssl=1" alt="Puttygen" width="300" height="288" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_puttygen.png?resize=300%2C288&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_puttygen.png?w=483&ssl=1 483w" sizes="auto, (max-width: 300px) 100vw, 300px" />][1][Import key

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_importkey.png?fit=476%2C450&ssl=1" class="alignnone size-medium wp-image-1451" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_importkey.png?resize=300%2C284&ssl=1" alt="Import key" width="300" height="284" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_importkey.png?resize=300%2C284&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_importkey.png?w=476&ssl=1 476w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2][Puttygen Warning

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen_warning.png?fit=471%2C458&ssl=1" class="alignnone size-medium wp-image-1452" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen_warning.png?resize=300%2C292&ssl=1" alt="Puttygen Warning" width="300" height="292" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen_warning.png?resize=300%2C292&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen_warning.png?w=471&ssl=1 471w" sizes="auto, (max-width: 300px) 100vw, 300px" />][3][Puttygen save key

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen-guardarppk.png?fit=416%2C289&ssl=1" class="alignnone size-medium wp-image-1453" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen-guardarppk.png?resize=300%2C208&ssl=1" alt="Puttygen save key" width="300" height="208" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen-guardarppk.png?resize=300%2C208&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/puttygen-guardarppk.png?w=416&ssl=1 416w" sizes="auto, (max-width: 300px) 100vw, 300px" />][4]

Después de hacerlo, podemos ver los archivos que tenemos:

```bash
perengano@elrond:~/keys$ ls -la  
total 20  
drwxr-xr-x 2 perengano perengano 4096 abr 16 23:21 .  
drwxr-xr-x 49 perengano perengano 4096 abr 16 17:51 ..  
-rw-r–r– 1 perengano perengano 3244 abr 16 23:15 id_rsa  
-rw-r–r– 1 perengano perengano 755 abr 16 23:15 id_rsa.pub  
-rw-r–r– 1 perengano perengano 2701 abr 16 23:21 perengano.ppk  
perengano@elrond:~/keys$
```

Ahora sí, podemos añadir nuestro archivo .ppk a Filezilla

[Filezilla

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_Filezilla.png?fit=648%2C440&ssl=1" class="alignnone size-medium wp-image-1454" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_Filezilla.png?resize=300%2C204&ssl=1" alt="Filezilla" width="300" height="204" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_Filezilla.png?resize=300%2C204&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_Filezilla.png?resize=768%2C521&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Pant_Filezilla.png?w=781&ssl=1 781w" sizes="auto, (max-width: 300px) 100vw, 300px" />][5][Filezilla warning

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/filezilla_confiar.png?fit=648%2C282&ssl=1" class="alignnone size-medium wp-image-1455" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/filezilla_confiar.png?resize=300%2C131&ssl=1" alt="Filezilla warning" width="300" height="131" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/filezilla_confiar.png?resize=300%2C131&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/filezilla_confiar.png?w=691&ssl=1 691w" sizes="auto, (max-width: 300px) 100vw, 300px" />][6][Filezilla connected

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?fit=648%2C340&ssl=1" class="alignnone size-medium wp-image-1456" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?resize=300%2C157&ssl=1" alt="Filezilla connected" width="300" height="157" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?resize=300%2C157&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?resize=768%2C403&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?resize=1024%2C537&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?w=1366&ssl=1 1366w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/Filezilla_conectado.png?w=1296&ssl=1 1296w" sizes="auto, (max-width: 300px) 100vw, 300px" />][7]

Y eso sería todo.

### Referencias:

  * <a href="https://www.linuxtotal.com.mx/index.php?cont=info_seyre_010" target="_blank" rel="noopener">https://www.linuxtotal.com.mx/index.php?cont=info_seyre_010</a>
  * <a href="https://www.codeenigma.com/host/faq/how-do-i-create-ssh-public-key-windows-pc" target="_blank" rel="noopener">https://www.codeenigma.com/host/faq/how-do-i-create-ssh-public-key-windows-pc</a>
  * <a href="https://www.hostinger.mx/tutoriales/llaves-ssh" target="_blank" rel="noopener">https://www.hostinger.mx/tutoriales/llaves-ssh</a>

 

 [1]: /wp-content/uploads/2018/04/Pant_puttygen.png
 [2]: /wp-content/uploads/2018/04/Pant_importkey.png
 [3]: /wp-content/uploads/2018/04/puttygen_warning.png
 [4]: /wp-content/uploads/2018/04/puttygen-guardarppk.png
 [5]: /wp-content/uploads/2018/04/Pant_Filezilla.png
 [6]: /wp-content/uploads/2018/04/filezilla_confiar.png
 [7]: /wp-content/uploads/2018/04/Filezilla_conectado.png
