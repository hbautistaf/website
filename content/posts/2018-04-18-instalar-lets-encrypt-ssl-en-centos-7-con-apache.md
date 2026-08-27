---
title: Instalar Let’s Encrypt SSL en CentOS 7 con Apache
date: 2018-04-18 14:10:21+00:00
slug: instalar-lets-encrypt-ssl-en-centos-7-con-apache
image: /wp-content/uploads/2018/04/lets-encrypt-ssl-on-centos7.png
categories:
- Gnu/Linux
tags:
- Apache
- CentOS
- Letsencrypt
- SSL
aliases:
- /2018/04/18/instalar-lets-encrypt-ssl-en-centos-7-con-apache/
- /linux/instalar-lets-encrypt-ssl-en-centos-7-con-apache/
---

<a href="https://letsencrypt.org" target="_blank" rel="noopener">Let's Encrypt</a> es una autoridad de certificacion (CA) gratuita, automatizada y abierta:[

![Let](/wp-content/uploads/2018/04/letsencrypt-logo-horizontal.png)

][1]

> 

>   Let’s Encrypt is a free, automated, and open certificate authority (CA), run for the public’s benefit. It is a service provided by the Internet Security Research Group (ISRG).
> 

Para el propósito de esta guía usaremos el dominio **chingon.com** y será referenciado de ahora en adelante.

 

# Paso 1 – Instalando el software necesario

Nos conectamos a nuestro servidor e instalamos los paquetes **mod_ssl** y **certbot-apache**. El primero es una dependencia para poder hacer uso de los certificados.

```bash
perengano@elrond:~$ ssh vpsmikel.ds  
Last login: Tue Apr 17 03:08:56 2018 from 189.201.191.13  
[perengano@B8GUsg ~]$ sudo su –  
[sudo] password for perengano:  
Último inicio de sesión:mar abr 17 03:09:03 EDT 2018en pts/0  
[root@B8GUsg ~]# yum install mod_ssl  
[root@B8GUsg ~]# yum install certbot-apache  
Loaded plugins: fastestmirror  
base | 3.6 kB 00:00:00  
epel/x86_64/metalink | 29 kB 00:00:00  
extras | 3.4 kB 00:00:00  
remi-php70 | 2.9 kB 00:00:00  
remi-php72 | 2.9 kB 00:00:00  
remi-safe | 2.9 kB 00:00:00  
updates | 3.4 kB 00:00:00  
vz-base | 951 B 00:00:00  
vz-updates | 951 B 00:00:00  
updates/7/x86\_64/primary\_db | 6.9 MB 00:00:01  
Loading mirror speeds from cached hostfile  
* base: mirror.reconn.ru  
* epel: mirror.logol.ru  
* extras: mirror.reconn.ru  
* remi-php70: mirror.reconn.ru  
* remi-php72: mirror.reconn.ru  
* remi-safe: mirror.reconn.ru  
* updates: mirror.reconn.ru  
Resolving Dependencies  
–> Running transaction check  
—> Package python2-certbot-apache.noarch 0:0.22.2-1.el7 will be installed  
–> Processing Dependency: certbot >= 0.21.1 for package: python2-certbot-apache-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-certbot >= 0.21.1 for package: python2-certbot-apache-0.22.2-1.el7.noarch  
–> Processing Dependency: python-augeas for package: python2-certbot-apache-0.22.2-1.el7.noarch  
–> Running transaction check  
—> Package certbot.noarch 0:0.22.2-1.el7 will be installed  
–> Processing Dependency: /usr/sbin/semanage for package: certbot-0.22.2-1.el7.noarch  
—> Package python-augeas.noarch 0:0.5.0-2.el7 will be installed  
–> Processing Dependency: augeas-libs for package: python-augeas-0.5.0-2.el7.noarch  
—> Package python2-certbot.noarch 0:0.22.2-1.el7 will be installed  
–> Processing Dependency: python2-acme > 0.21.1 for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python-configobj for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python-parsedatetime for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python-setuptools for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python-zope-component for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python-zope-interface for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-configargparse for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-cryptography for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-future for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-josepy for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-mock for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-pyrfc3339 for package: python2-certbot-0.22.2-1.el7.noarch  
–> Processing Dependency: pytz for package: python2-certbot-0.22.2-1.el7.noarch  
–> Running transaction check  
—> Package augeas-libs.x86\_64 0:1.4.0-2.el7\_4.2 will be installed  
—> Package policycoreutils-python.x86_64 0:2.5-17.1.el7 will be installed  
–> Processing Dependency: setools-libs >= 3.3.8-1 for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: libsemanage-python >= 2.5-5 for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: audit-libs-python >= 2.1.3-4 for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: python-IPy for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: libqpol.so.1(VERS\_1.4)(64bit) for package: policycoreutils-python-2.5-17.1.el7.x86\_64  
–> Processing Dependency: libqpol.so.1(VERS\_1.2)(64bit) for package: policycoreutils-python-2.5-17.1.el7.x86\_64  
–> Processing Dependency: libcgroup for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: libapol.so.4(VERS\_4.0)(64bit) for package: policycoreutils-python-2.5-17.1.el7.x86\_64  
–> Processing Dependency: checkpolicy for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: libqpol.so.1()(64bit) for package: policycoreutils-python-2.5-17.1.el7.x86_64  
–> Processing Dependency: libapol.so.4()(64bit) for package: policycoreutils-python-2.5-17.1.el7.x86_64  
—> Package python-configobj.noarch 0:4.7.2-7.el7 will be installed  
—> Package python-setuptools.noarch 0:0.9.8-7.el7 will be installed  
–> Processing Dependency: python-backports-ssl\_match\_hostname for package: python-setuptools-0.9.8-7.el7.noarch  
—> Package python-zope-component.noarch 1:4.1.0-3.el7 will be installed  
–> Processing Dependency: python-zope-event for package: 1:python-zope-component-4.1.0-3.el7.noarch  
—> Package python-zope-interface.x86_64 0:4.0.5-4.el7 will be installed  
—> Package python2-acme.noarch 0:0.22.2-1.el7 will be installed  
–> Processing Dependency: pyOpenSSL >= 0.13 for package: python2-acme-0.22.2-1.el7.noarch  
–> Processing Dependency: python-ndg_httpsclient for package: python2-acme-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-pyasn1 for package: python2-acme-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-requests for package: python2-acme-0.22.2-1.el7.noarch  
–> Processing Dependency: python2-six for package: python2-acme-0.22.2-1.el7.noarch  
—> Package python2-configargparse.noarch 0:0.11.0-1.el7 will be installed  
—> Package python2-cryptography.x86\_64 0:1.7.2-1.el7\_4.1 will be installed  
–> Processing Dependency: python-six >= 1.4.1 for package: python2-cryptography-1.7.2-1.el7\_4.1.x86\_64  
–> Processing Dependency: python-idna >= 2.0 for package: python2-cryptography-1.7.2-1.el7\_4.1.x86\_64  
–> Processing Dependency: python-cffi >= 1.4.1 for package: python2-cryptography-1.7.2-1.el7\_4.1.x86\_64  
–> Processing Dependency: python-ipaddress for package: python2-cryptography-1.7.2-1.el7\_4.1.x86\_64  
–> Processing Dependency: python-enum34 for package: python2-cryptography-1.7.2-1.el7\_4.1.x86\_64  
—> Package python2-future.noarch 0:0.16.0-6.el7 will be installed  
—> Package python2-josepy.noarch 0:1.0.1-1.el7 will be installed  
—> Package python2-mock.noarch 0:1.0.1-9.el7 will be installed  
—> Package python2-parsedatetime.noarch 0:2.4-5.el7 will be installed  
—> Package python2-pyrfc3339.noarch 0:1.0-2.el7 will be installed  
—> Package pytz.noarch 0:2016.10-2.el7 will be installed  
–> Running transaction check  
—> Package audit-libs-python.x86_64 0:2.7.6-3.el7 will be installed  
—> Package checkpolicy.x86_64 0:2.5-4.el7 will be installed  
—> Package libcgroup.x86_64 0:0.41-13.el7 will be installed  
—> Package libsemanage-python.x86_64 0:2.5-8.el7 will be installed  
—> Package pyOpenSSL.x86_64 0:0.13.1-3.el7 will be installed  
—> Package python-IPy.noarch 0:0.75-6.el7 will be installed  
—> Package python-backports-ssl\_match\_hostname.noarch 0:3.4.0.2-4.el7 will be installed  
–> Processing Dependency: python-backports for package: python-backports-ssl\_match\_hostname-3.4.0.2-4.el7.noarch  
—> Package python-cffi.x86_64 0:1.6.0-5.el7 will be installed  
–> Processing Dependency: python-pycparser for package: python-cffi-1.6.0-5.el7.x86_64  
—> Package python-enum34.noarch 0:1.0.4-1.el7 will be installed  
—> Package python-idna.noarch 0:2.4-1.el7 will be installed  
—> Package python-ipaddress.noarch 0:1.0.16-2.el7 will be installed  
—> Package python-ndg_httpsclient.noarch 0:0.3.2-1.el7 will be installed  
—> Package python-six.noarch 0:1.9.0-2.el7 will be installed  
—> Package python-zope-event.noarch 0:4.0.3-2.el7 will be installed  
—> Package python2-pyasn1.noarch 0:0.1.9-7.el7 will be installed  
—> Package python2-requests.noarch 0:2.6.0-0.el7 will be installed  
–> Processing Dependency: python-requests >= 2.6.0 for package: python2-requests-2.6.0-0.el7.noarch  
—> Package python2-six.noarch 0:1.9.0-0.el7 will be installed  
—> Package setools-libs.x86_64 0:3.3.8-1.1.el7 will be installed  
–> Running transaction check  
—> Package python-backports.x86_64 0:1.0-8.el7 will be installed  
—> Package python-pycparser.noarch 0:2.14-1.el7 will be installed  
–> Processing Dependency: python-ply for package: python-pycparser-2.14-1.el7.noarch  
—> Package python-requests.noarch 0:2.6.0-1.el7_1 will be installed  
–> Processing Dependency: python-urllib3 >= 1.10.2-1 for package: python-requests-2.6.0-1.el7_1.noarch  
–> Running transaction check  
—> Package python-ply.noarch 0:3.4-11.el7 will be installed  
—> Package python-urllib3.noarch 0:1.10.2-3.el7 will be installed  
–> Finished Dependency Resolution

Dependencies Resolved

========================================================================================================================================================================  
Package Arch Version Repository Size  
========================================================================================================================================================================  
Installing:  
python2-certbot-apache noarch 0.22.2-1.el7 epel 214 k  
Installing for dependencies:  
audit-libs-python x86_64 2.7.6-3.el7 base 73 k  
augeas-libs x86\_64 1.4.0-2.el7\_4.2 updates 355 k  
certbot noarch 0.22.2-1.el7 epel 21 k  
checkpolicy x86_64 2.5-4.el7 base 290 k  
libcgroup x86_64 0.41-13.el7 base 65 k  
libsemanage-python x86_64 2.5-8.el7 base 104 k  
policycoreutils-python x86_64 2.5-17.1.el7 base 446 k  
pyOpenSSL x86_64 0.13.1-3.el7 base 133 k  
python-IPy noarch 0.75-6.el7 base 32 k  
python-augeas noarch 0.5.0-2.el7 base 25 k  
python-backports x86_64 1.0-8.el7 base 5.8 k  
python-backports-ssl\_match\_hostname noarch 3.4.0.2-4.el7 base 12 k  
python-cffi x86_64 1.6.0-5.el7 base 218 k  
python-configobj noarch 4.7.2-7.el7 base 117 k  
python-enum34 noarch 1.0.4-1.el7 base 52 k  
python-idna noarch 2.4-1.el7 base 94 k  
python-ipaddress noarch 1.0.16-2.el7 base 34 k  
python-ndg_httpsclient noarch 0.3.2-1.el7 epel 43 k  
python-ply noarch 3.4-11.el7 base 123 k  
python-pycparser noarch 2.14-1.el7 base 104 k  
python-requests noarch 2.6.0-1.el7_1 base 94 k  
python-setuptools noarch 0.9.8-7.el7 base 397 k  
python-six noarch 1.9.0-2.el7 base 29 k  
python-urllib3 noarch 1.10.2-3.el7 base 101 k  
python-zope-component noarch 1:4.1.0-3.el7 epel 227 k  
python-zope-event noarch 4.0.3-2.el7 epel 79 k  
python-zope-interface x86_64 4.0.5-4.el7 base 138 k  
python2-acme noarch 0.22.2-1.el7 epel 135 k  
python2-certbot noarch 0.22.2-1.el7 epel 481 k  
python2-configargparse noarch 0.11.0-1.el7 epel 30 k  
python2-cryptography x86\_64 1.7.2-1.el7\_4.1 updates 502 k  
python2-future noarch 0.16.0-6.el7 epel 799 k  
python2-josepy noarch 1.0.1-1.el7 epel 86 k  
python2-mock noarch 1.0.1-9.el7 epel 92 k  
python2-parsedatetime noarch 2.4-5.el7 epel 78 k  
python2-pyasn1 noarch 0.1.9-7.el7 base 100 k  
python2-pyrfc3339 noarch 1.0-2.el7 epel 13 k  
python2-requests noarch 2.6.0-0.el7 epel 2.9 k  
python2-six noarch 1.9.0-0.el7 epel 2.9 k  
pytz noarch 2016.10-2.el7 base 46 k  
setools-libs x86_64 3.3.8-1.1.el7 base 612 k

Transaction Summary  
========================================================================================================================================================================  
Install 1 Package (+41 Dependent packages)

Total download size: 6.5 M  
Installed size: 28 M  
Is this ok [y/d/N]: y  
Downloading packages:  
(1/42): audit-libs-python-2.7.6-3.el7.x86_64.rpm | 73 kB 00:00:00  
(2/42): libsemanage-python-2.5-8.el7.x86_64.rpm | 104 kB 00:00:00  
(3/42): libcgroup-0.41-13.el7.x86_64.rpm | 65 kB 00:00:00  
(4/42): augeas-libs-1.4.0-2.el7\_4.2.x86\_64.rpm | 355 kB 00:00:00  
(5/42): python-IPy-0.75-6.el7.noarch.rpm | 32 kB 00:00:00  
(6/42): pyOpenSSL-0.13.1-3.el7.x86_64.rpm | 133 kB 00:00:00  
(7/42): checkpolicy-2.5-4.el7.x86_64.rpm | 290 kB 00:00:00  
(8/42): python-augeas-0.5.0-2.el7.noarch.rpm | 25 kB 00:00:00  
(9/42): python-backports-1.0-8.el7.x86_64.rpm | 5.8 kB 00:00:00  
(10/42): python-configobj-4.7.2-7.el7.noarch.rpm | 117 kB 00:00:00  
(11/42): certbot-0.22.2-1.el7.noarch.rpm | 21 kB 00:00:00  
(12/42): python-enum34-1.0.4-1.el7.noarch.rpm | 52 kB 00:00:00  
(13/42): python-cffi-1.6.0-5.el7.x86_64.rpm | 218 kB 00:00:00  
(14/42): python-ipaddress-1.0.16-2.el7.noarch.rpm | 34 kB 00:00:00  
(15/42): python-ndg_httpsclient-0.3.2-1.el7.noarch.rpm | 43 kB 00:00:00  
(16/42): python-ply-3.4-11.el7.noarch.rpm | 123 kB 00:00:00  
(17/42): python-pycparser-2.14-1.el7.noarch.rpm | 104 kB 00:00:00  
(18/42): python-requests-2.6.0-1.el7_1.noarch.rpm | 94 kB 00:00:00  
(19/42): python-idna-2.4-1.el7.noarch.rpm | 94 kB 00:00:00  
(20/42): python-six-1.9.0-2.el7.noarch.rpm | 29 kB 00:00:00  
(21/42): python-urllib3-1.10.2-3.el7.noarch.rpm | 101 kB 00:00:00  
(22/42): python-backports-ssl\_match\_hostname-3.4.0.2-4.el7.noarch.rpm | 12 kB 00:00:00  
(23/42): policycoreutils-python-2.5-17.1.el7.x86_64.rpm | 446 kB 00:00:00  
(24/42): python-setuptools-0.9.8-7.el7.noarch.rpm | 397 kB 00:00:00  
(25/42): python-zope-component-4.1.0-3.el7.noarch.rpm | 227 kB 00:00:00  
(26/42): python-zope-event-4.0.3-2.el7.noarch.rpm | 79 kB 00:00:00  
(27/42): python2-acme-0.22.2-1.el7.noarch.rpm | 135 kB 00:00:00  
(28/42): python-zope-interface-4.0.5-4.el7.x86_64.rpm | 138 kB 00:00:00  
(29/42): python2-certbot-0.22.2-1.el7.noarch.rpm | 481 kB 00:00:00  
(30/42): python2-certbot-apache-0.22.2-1.el7.noarch.rpm | 214 kB 00:00:00  
(31/42): python2-configargparse-0.11.0-1.el7.noarch.rpm | 30 kB 00:00:00  
(32/42): python2-future-0.16.0-6.el7.noarch.rpm | 799 kB 00:00:00  
(33/42): python2-cryptography-1.7.2-1.el7\_4.1.x86\_64.rpm | 502 kB 00:00:00  
(34/42): python2-josepy-1.0.1-1.el7.noarch.rpm | 86 kB 00:00:00  
(35/42): python2-mock-1.0.1-9.el7.noarch.rpm | 92 kB 00:00:00  
(36/42): python2-parsedatetime-2.4-5.el7.noarch.rpm | 78 kB 00:00:00  
(37/42): python2-pyrfc3339-1.0-2.el7.noarch.rpm | 13 kB 00:00:00  
(38/42): python2-requests-2.6.0-0.el7.noarch.rpm | 2.9 kB 00:00:00  
(39/42): python2-six-1.9.0-0.el7.noarch.rpm | 2.9 kB 00:00:00  
(40/42): pytz-2016.10-2.el7.noarch.rpm | 46 kB 00:00:00  
(41/42): python2-pyasn1-0.1.9-7.el7.noarch.rpm | 100 kB 00:00:00  
(42/42): setools-libs-3.3.8-1.1.el7.x86_64.rpm | 612 kB 00:00:00  
————————————————————————————————————————————————————————  
Total 4.4 MB/s | 6.5 MB 00:00:01  
Running transaction check  
Running transaction test  
Transaction test succeeded  
Running transaction  
Installing : python-six-1.9.0-2.el7.noarch 1/42  
Installing : python2-pyasn1-0.1.9-7.el7.noarch 2/42  
Installing : pyOpenSSL-0.13.1-3.el7.x86_64 3/42  
Installing : pytz-2016.10-2.el7.noarch 4/42  
Installing : python2-pyrfc3339-1.0-2.el7.noarch 5/42  
Installing : python2-future-0.16.0-6.el7.noarch 6/42  
Installing : python-zope-interface-4.0.5-4.el7.x86_64 7/42  
Installing : python2-parsedatetime-2.4-5.el7.noarch 8/42  
Installing : python2-six-1.9.0-0.el7.noarch 9/42  
Installing : setools-libs-3.3.8-1.1.el7.x86_64 10/42  
Installing : python-enum34-1.0.4-1.el7.noarch 11/42  
Installing : checkpolicy-2.5-4.el7.x86_64 12/42  
Installing : audit-libs-python-2.7.6-3.el7.x86_64 13/42  
Installing : augeas-libs-1.4.0-2.el7\_4.2.x86\_64 14/42  
Installing : python-augeas-0.5.0-2.el7.noarch 15/42  
Installing : python-ipaddress-1.0.16-2.el7.noarch 16/42  
Installing : python-zope-event-4.0.3-2.el7.noarch 17/42  
Installing : 1:python-zope-component-4.1.0-3.el7.noarch 18/42  
Installing : python-configobj-4.7.2-7.el7.noarch 19/42  
Installing : python2-mock-1.0.1-9.el7.noarch 20/42  
Installing : python-ply-3.4-11.el7.noarch 21/42  
Installing : python-pycparser-2.14-1.el7.noarch 22/42  
Installing : python-cffi-1.6.0-5.el7.x86_64 23/42  
Installing : python-backports-1.0-8.el7.x86_64 24/42  
Installing : python-backports-ssl\_match\_hostname-3.4.0.2-4.el7.noarch 25/42  
Installing : python-setuptools-0.9.8-7.el7.noarch 26/42  
Installing : python-ndg_httpsclient-0.3.2-1.el7.noarch 27/42  
Installing : python-urllib3-1.10.2-3.el7.noarch 28/42  
Installing : python-requests-2.6.0-1.el7_1.noarch 29/42  
Installing : python2-requests-2.6.0-0.el7.noarch 30/42  
Installing : libsemanage-python-2.5-8.el7.x86_64 31/42  
Installing : python-idna-2.4-1.el7.noarch 32/42  
Installing : python2-cryptography-1.7.2-1.el7\_4.1.x86\_64 33/42  
Installing : python2-josepy-1.0.1-1.el7.noarch 34/42  
Installing : python2-acme-0.22.2-1.el7.noarch 35/42  
Installing : libcgroup-0.41-13.el7.x86_64 36/42  
Installing : python-IPy-0.75-6.el7.noarch 37/42  
Installing : policycoreutils-python-2.5-17.1.el7.x86_64 38/42  
Installing : python2-configargparse-0.11.0-1.el7.noarch 39/42  
Installing : python2-certbot-0.22.2-1.el7.noarch 40/42  
Installing : certbot-0.22.2-1.el7.noarch 41/42  
ValueError: SELinux policy is not managed or store cannot be accessed.  
Installing : python2-certbot-apache-0.22.2-1.el7.noarch 42/42  
Verifying : python-augeas-0.5.0-2.el7.noarch 1/42  
Verifying : python-backports-ssl\_match\_hostname-3.4.0.2-4.el7.noarch 2/42  
Verifying : python2-configargparse-0.11.0-1.el7.noarch 3/42  
Verifying : python-zope-interface-4.0.5-4.el7.x86_64 4/42  
Verifying : python-ndg_httpsclient-0.3.2-1.el7.noarch 5/42  
Verifying : 1:python-zope-component-4.1.0-3.el7.noarch 6/42  
Verifying : python2-future-0.16.0-6.el7.noarch 7/42  
Verifying : policycoreutils-python-2.5-17.1.el7.x86_64 8/42  
Verifying : python-setuptools-0.9.8-7.el7.noarch 9/42  
Verifying : python2-acme-0.22.2-1.el7.noarch 10/42  
Verifying : python2-cryptography-1.7.2-1.el7\_4.1.x86\_64 11/42  
Verifying : python2-certbot-apache-0.22.2-1.el7.noarch 12/42  
Verifying : certbot-0.22.2-1.el7.noarch 13/42  
Verifying : python2-pyrfc3339-1.0-2.el7.noarch 14/42  
Verifying : python2-six-1.9.0-0.el7.noarch 15/42  
Verifying : pytz-2016.10-2.el7.noarch 16/42  
Verifying : python-urllib3-1.10.2-3.el7.noarch 17/42  
Verifying : python-IPy-0.75-6.el7.noarch 18/42  
Verifying : libcgroup-0.41-13.el7.x86_64 19/42  
Verifying : python-six-1.9.0-2.el7.noarch 20/42  
Verifying : python2-certbot-0.22.2-1.el7.noarch 21/42  
Verifying : python-idna-2.4-1.el7.noarch 22/42  
Verifying : libsemanage-python-2.5-8.el7.x86_64 23/42  
Verifying : python2-requests-2.6.0-0.el7.noarch 24/42  
Verifying : python-backports-1.0-8.el7.x86_64 25/42  
Verifying : python-cffi-1.6.0-5.el7.x86_64 26/42  
Verifying : python-ply-3.4-11.el7.noarch 27/42  
Verifying : pyOpenSSL-0.13.1-3.el7.x86_64 28/42  
Verifying : python2-parsedatetime-2.4-5.el7.noarch 29/42  
Verifying : python-pycparser-2.14-1.el7.noarch 30/42  
Verifying : python2-mock-1.0.1-9.el7.noarch 31/42  
Verifying : python-configobj-4.7.2-7.el7.noarch 32/42  
Verifying : python-requests-2.6.0-1.el7_1.noarch 33/42  
Verifying : python-zope-event-4.0.3-2.el7.noarch 34/42  
Verifying : python-ipaddress-1.0.16-2.el7.noarch 35/42  
Verifying : augeas-libs-1.4.0-2.el7\_4.2.x86\_64 36/42  
Verifying : python2-pyasn1-0.1.9-7.el7.noarch 37/42  
Verifying : audit-libs-python-2.7.6-3.el7.x86_64 38/42  
Verifying : python2-josepy-1.0.1-1.el7.noarch 39/42  
Verifying : checkpolicy-2.5-4.el7.x86_64 40/42  
Verifying : python-enum34-1.0.4-1.el7.noarch 41/42  
Verifying : setools-libs-3.3.8-1.1.el7.x86_64 42/42

Installed:  
python2-certbot-apache.noarch 0:0.22.2-1.el7

Dependency Installed:  
audit-libs-python.x86\_64 0:2.7.6-3.el7 augeas-libs.x86\_64 0:1.4.0-2.el7_4.2 certbot.noarch 0:0.22.2-1.el7  
checkpolicy.x86\_64 0:2.5-4.el7 libcgroup.x86\_64 0:0.41-13.el7 libsemanage-python.x86_64 0:2.5-8.el7  
policycoreutils-python.x86\_64 0:2.5-17.1.el7 pyOpenSSL.x86\_64 0:0.13.1-3.el7 python-IPy.noarch 0:0.75-6.el7  
python-augeas.noarch 0:0.5.0-2.el7 python-backports.x86\_64 0:1.0-8.el7 python-backports-ssl\_match_hostname.noarch 0:3.4.0.2-4.el7  
python-cffi.x86_64 0:1.6.0-5.el7 python-configobj.noarch 0:4.7.2-7.el7 python-enum34.noarch 0:1.0.4-1.el7  
python-idna.noarch 0:2.4-1.el7 python-ipaddress.noarch 0:1.0.16-2.el7 python-ndg_httpsclient.noarch 0:0.3.2-1.el7  
python-ply.noarch 0:3.4-11.el7 python-pycparser.noarch 0:2.14-1.el7 python-requests.noarch 0:2.6.0-1.el7_1  
python-setuptools.noarch 0:0.9.8-7.el7 python-six.noarch 0:1.9.0-2.el7 python-urllib3.noarch 0:1.10.2-3.el7  
python-zope-component.noarch 1:4.1.0-3.el7 python-zope-event.noarch 0:4.0.3-2.el7 python-zope-interface.x86_64 0:4.0.5-4.el7  
python2-acme.noarch 0:0.22.2-1.el7 python2-certbot.noarch 0:0.22.2-1.el7 python2-configargparse.noarch 0:0.11.0-1.el7  
python2-cryptography.x86\_64 0:1.7.2-1.el7\_4.1 python2-future.noarch 0:0.16.0-6.el7 python2-josepy.noarch 0:1.0.1-1.el7  
python2-mock.noarch 0:1.0.1-9.el7 python2-parsedatetime.noarch 0:2.4-5.el7 python2-pyasn1.noarch 0:0.1.9-7.el7  
python2-pyrfc3339.noarch 0:1.0-2.el7 python2-requests.noarch 0:2.6.0-0.el7 python2-six.noarch 0:1.9.0-0.el7  
pytz.noarch 0:2016.10-2.el7 setools-libs.x86_64 0:3.3.8-1.1.el7

Complete!  
[root@B8GUsg ~]#
```

[yum install certbot

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?fit=648%2C340&ssl=1" class="alignnone size-medium wp-image-1490" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?resize=300%2C157&ssl=1" alt="yum install certbot" width="300" height="157" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?resize=300%2C157&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?resize=768%2C403&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?resize=1024%2C537&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?w=1366&ssl=1 1366w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/yum-install-certbot.png?w=1296&ssl=1 1296w" sizes="auto, (max-width: 300px) 100vw, 300px" />][2][certbot installed

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?fit=648%2C340&ssl=1" class="size-medium wp-image-1488 alignnone" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?resize=300%2C157&ssl=1" alt="certbot installed" width="300" height="157" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?resize=300%2C157&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?resize=768%2C403&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?resize=1024%2C537&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?w=1366&ssl=1 1366w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-installed.png?w=1296&ssl=1 1296w" sizes="auto, (max-width: 300px) 100vw, 300px" />][3]

 

# Paso 2 – Reglas del firewall

  Si están usando **firewalld** o **iptables** para tener abiertos sólo los servicios que se ocupen, necesitamos agregar reglas para los puertos **80** y **443**.

Si usan **firewalld**, con los siguientes comandos:

```bash
[root@B8GUsg ~]# firewall-cmd –add-service=http  
[root@B8GUsg ~]# firewall-cmd –add-service=https  
[root@B8GUsg ~]# firewall-cmd –runtime-to-permanent
```

En el caso de que estemos usando **iptables**, ejecutamos lo siguiente:

```bash
[root@B8GUsg ~]# iptables -I INPUT -p tcp -m tcp –dport 80 -j ACCEPT  
[root@B8GUsg ~]# iptables -I INPUT -p tcp -m tcp –dport 443 -j ACCEPT
```

# Paso 3 – Solicitando un Certificado SSL de Let's Encrypt

Ya que tenemos esto listo, podemos solicitar un certificado **SSL** para nuestro dominio.

  Generar el certificado **SSL** para **Apache** usando el cliente para **Let's Encrypt** **certbot** es muy sencillo. El cliente obtendrá e instalará automáticamente un nuevo certificado **SSL** válido para los dominios proporcionados como parámetros.

```bash
[root@B8GUsg ~]# certbot –apache -d chingon.com -d www.chingon.com  
Saving debug log to /var/log/letsencrypt/letsencrypt.log  
Plugins selected: Authenticator apache, Installer apache  
Enter email address (used for urgent renewal and security notices) (Enter 'c' to  
cancel): perengano@gmail.com  
Starting new HTTPS connection (1): acme-v01.api.letsencrypt.org

——————————————————————————-  
Please read the Terms of Service at  
https://letsencrypt.org/documents/LE-SA-v1.2-November-15-2017.pdf. You must  
agree in order to register with the ACME server at  
https://acme-v01.api.letsencrypt.org/directory  
——————————————————————————-  
(A)gree/(C)ancel: A

——————————————————————————-  
Would you be willing to share your email address with the Electronic Frontier  
Foundation, a founding partner of the Let's Encrypt project and the non-profit  
organization that develops Certbot? We'd like to send you email about EFF and  
our work to encrypt the web, protect its users and defend digital rights.  
——————————————————————————-  
(Y)es/(N)o: Y  
Starting new HTTPS connection (1): supporters.eff.org  
Obtaining a new certificate  
Performing the following challenges:  
http-01 challenge for chingon.com  
http-01 challenge for www.chingon.com  
Waiting for verification…  
Cleaning up challenges  
Created an SSL vhost at /etc/httpd/sites-available/chingon.com-le-ssl.conf  
Deploying Certificate to VirtualHost /etc/httpd/sites-available/chingon.com-le-ssl.conf  
Enabling site /etc/httpd/sites-available/chingon.com-le-ssl.conf by adding Include to root configuration  
Deploying Certificate to VirtualHost /etc/httpd/sites-available/chingon.com-le-ssl.conf

Please choose whether or not to redirect HTTP traffic to HTTPS, removing HTTP access.  
——————————————————————————-  
1: No redirect – Make no further changes to the webserver configuration.  
2: Redirect – Make all requests redirect to secure HTTPS access. Choose this for  
new sites, or if you're confident your site works on HTTPS. You can undo this  
change by editing your web server's configuration.  
——————————————————————————-  
Select the appropriate number \[1-2] then [enter\] (press 'c' to cancel): 2  
Redirecting vhost in /etc/httpd/sites-enabled/chingon.com.conf to ssl vhost in /etc/httpd/sites-available/chingon.com-le-ssl.conf

——————————————————————————-  
Congratulations! You have successfully enabled https://chingon.com and  
https://www.chingon.com

You should test your configuration at:  
https://www.ssllabs.com/ssltest/analyze.html?d=chingon.com  
https://www.ssllabs.com/ssltest/analyze.html?d=www.chingon.com  
——————————————————————————-

IMPORTANT NOTES:  
– Congratulations! Your certificate and chain have been saved at:  
/etc/letsencrypt/live/chingon.com/fullchain.pem  
Your key file has been saved at:  
/etc/letsencrypt/live/chingon.com/privkey.pem  
Your cert will expire on 2018-07-16. To obtain a new or tweaked  
version of this certificate in the future, simply run certbot again  
with the "certonly" option. To non-interactively renew \*all\* of  
your certificates, run "certbot renew"  
– Your account credentials have been saved in your Certbot  
configuration directory at /etc/letsencrypt. You should make a  
secure backup of this folder now. This configuration directory will  
also contain certificates and private keys obtained by Certbot so  
making regular backups of this folder is ideal.  
– If you like Certbot, please consider supporting our work by:

Donating to ISRG / Let's Encrypt: https://letsencrypt.org/donate  
Donating to EFF: https://eff.org/donate-le

[root@B8GUsg ~]#
```

[certbot domain

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?fit=648%2C340&ssl=1" class="aligncenter size-medium wp-image-1489" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?resize=300%2C157&ssl=1" alt="certbot domain" width="300" height="157" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?resize=300%2C157&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?resize=768%2C403&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?resize=1024%2C537&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?w=1366&ssl=1 1366w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2018/04/certbot-domain.png?w=1296&ssl=1 1296w" sizes="auto, (max-width: 300px) 100vw, 300px" />][4]

 

# Paso 4 – Habilitando SSL en nuestro Apache

  Aunque estamos usando **CentOS**, cuando se hizo la instalación de **Apache**, fueron creados dos directorios para el uso de los **VirtualHost** y de esta manera sea más sencillo su uso. Esta forma es habitual en **Debian**, y son *sites-available* y *sites-enabled*.

```bash
[root@B8GUsg ~]# cd /etc/httpd/  
[root@B8GUsg httpd]# ls -l  
total 20  
drwxr-xr-x 2 root root 4096 Apr 17 14:40 conf  
drwxr-xr-x 2 root root 4096 Apr 17 14:40 conf.d  
drwxr-xr-x 2 root root 4096 Apr 17 03:10 conf.modules.d  
lrwxrwxrwx 1 root root 19 Apr 13 11:18 logs -> ../../var/log/httpd  
lrwxrwxrwx 1 root root 29 Apr 13 11:18 modules -> ../../usr/lib64/httpd/modules  
lrwxrwxrwx 1 root root 10 Apr 13 11:18 run -> /run/httpd  
drwxr-xr-x 2 root root 4096 Apr 17 14:41 sites-available  
drwxr-xr-x 2 root root 4096 Apr 17 14:49 sites-enabled  
[root@B8GUsg httpd]#
```

  El archivo de configuración de nuestro dominio con su certificado está en: **/etc/httpd/sites-available/chingon.com-le-ssl.conf**, y necesitamos crear un enlace simbólico en **sites-enabled** para que **Apache** lo tome en cuenta.

```bash
[root@B8GUsg httpd]# ln -s /etc/httpd/sites-available/chingon.com-le-ssl.conf /etc/httpd/sites-enabled/chingon.com.ssl.conf
```

 

# Paso 5 – Añadiendo seguridad extra a la configuración SSL de Apache

  La configuración por defecto de **CentOS 7** del **Apache** que está disponible está un poco desactualizada en cuanto a configuración se refiere, al mismo tiempo que es vulnerable a ataques y técnicas recientes.

  Se recomienda deshabilitar los siguientes valores en el archivo **/etc/httpd/conf.d/ssl.conf** así que creamos una copia de seguridad como primer paso:

  
```bash
<br /> [root@B8GUsg httpd]# cd conf.d/<br /> [root@B8GUsg conf.d]# cp ssl.conf /root/<br /> [root@B8GUsg conf.d]# nano ssl.conf<br />
```

Una vez hecho eso, es momento de editar dicho archivo y comentar **SSLProtocol** y **SSLCipherSuite**:

```apache
. . .  
\# SSLProtocol all -SSLv2  
. . .  
\# SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5:!SEED:!IDEA  
. . .
```

Copiamos lo siguiente después del fin del bloque **VirtualHost**, que en este caso está al final del archivo:

```apache
\# Begin copied text  
\# from https://cipherli.st/  
\# and https://raymii.org/s/tutorials/Strong\_SSL\_Security\_On\_Apache2.html

SSLCipherSuite EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH  
SSLProtocol All -SSLv2 -SSLv3  
SSLHonorCipherOrder On  
\# Disable preloading HSTS for now. You can use the commented out header line that includes  
\# the "preload" directive if you understand the implications.  
#Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains; preload"  
Header always set Strict-Transport-Security "max-age=63072000; includeSubdomains"  
Header always set X-Frame-Options DENY  
Header always set X-Content-Type-Options nosniff  
\# Requires Apache >= 2.4  
SSLCompression off  
SSLUseStapling on  
SSLStaplingCache "shmcb:logs/stapling-cache(150000)"  
\# Requires Apache >= 2.4.11  
\# SSLSessionTickets Off
```

Verificamos que la configuración de **Apache** no tenga ningún error:

```bash
[root@B8GUsg conf.d]# apachectl configtest  
Syntax OK  
[root@B8GUsg conf.d]#
```

Si obtenemos **Syntax OK**, quiere decir que todo está bien, así que reiniciamos el servicio de Apache:

```bash
[root@B8GUsg conf.d]# systemctl restart httpd  
[root@B8GUsg conf.d]#
```

 

# Paso 6 – Verificando el estado de tu Certificado

Si se fijaron, al final de la obtención del certificado venía el siguiente texto, así que podemos usar esa URL para comprobarlo:

```bash
——————————————————————————-  
You should test your configuration at:  
https://www.ssllabs.com/ssltest/analyze.html?d=chingon.com  
https://www.ssllabs.com/ssltest/analyze.html?d=www.chingon.com  
——————————————————————————-  
[cc lang="bash"]

# Paso 7 – Configurando la auto-renovación del Certificado

  Los certificados de **Let's Encrypt** son válidos durante 90 días, por lo que es recomendable que se renueven cada 60 días. En este ejemplo se ejecutará cada día 15 de cada mes a las 2:30hrs. Editamos **Crontab**:

[cc lang="bash"]  
[root@B8GUsg conf.d]# crontab -e  
no crontab for root – using an empty one  
crontab: installing new crontab

Añadimos el siguiente contenido:

[root@B8GUsg conf.d]#  
\# Ejecutar los 15 de cada mes a las 2:30  
30 2 15 \* \* /usr/bin/certbot renew >> /var/log/le-renew.log
```

  En esta guía vimos como instalar un **Certificado SSL** gratuito de **Let's Encrypt** para tener un sitio seguro en **Apache** en un servidor **CentOS 7**.

### Referencias

  * <a href="https://certbot.eff.org/lets-encrypt/centosrhel7-apache" target="_blank" rel="noopener">https://certbot.eff.org/lets-encrypt/centosrhel7-apache</a>
  * <a href="https://www.hostinger.com/tutorials/vps/how-to-install-lets-encrypt-ssl-apache-centos7" target="_blank" rel="noopener">https://www.hostinger.com/tutorials/vps/how-to-install-lets-encrypt-ssl-apache-centos7</a>
  * <a href="https://www.centosblog.com/use-letsencrypt-free-ssl-certificate-centos-linux/" target="_blank" rel="noopener">https://www.centosblog.com/use-letsencrypt-free-ssl-certificate-centos-linux/</a>
  * <a href="https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-centos-7" target="_blank" rel="noopener">https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-centos-7</a>
  * <a href="https://letsencrypt.org/isrg/" target="_blank" rel="noopener">https://letsencrypt.org/isrg/</a>
  * <a href="https://letsencrypt.org/about/" target="_blank" rel="noopener">https://letsencrypt.org/about/</a>

 [1]: /wp-content/uploads/2018/04/letsencrypt-logo-horizontal.png
 [2]: /wp-content/uploads/2018/04/yum-install-certbot.png
 [3]: /wp-content/uploads/2018/04/certbot-installed.png
 [4]: /wp-content/uploads/2018/04/certbot-domain.png
