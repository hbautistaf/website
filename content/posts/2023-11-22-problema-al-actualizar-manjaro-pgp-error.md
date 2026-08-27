---
title: 'Problema al actualizar Manjaro: PGP Error'
date: 2023-11-23 03:59:17+00:00
slug: problema-al-actualizar-manjaro-pgp-error
image: /wp-content/uploads/2023/11/Manjaro-Terminal.png
categories:
- Gnu/Linux
aliases:
- /2023/11/22/problema-al-actualizar-manjaro-pgp-error/
- /linux/problema-al-actualizar-manjaro-pgp-error/
---

## Antecedentes 

  Hola a todos, a pasado un buen tiempo desde la última vez que puse algo en este blog. La verdad es que no tenía como un tema del cuál escribir, ya que mayormente es/era para hablar de temas de software libre, Gnu/Linux, Opensource en general. Pero a final de cuentas es un espacio donde puedo mostrar mis piensos y demás.

<!--more-->

  Tengo alrededor de poco más de 3 años usando <a href="https://manjaro.org/" target="_blank" rel="noopener" title="">**Manjaro** **Linux**</a>, lo instalé allá por Abril del 2020. Y me parece que por alguna razón reinstalé completamente en esta laptop, borrar particiones e instalar desde cero en Febrero de este año (2023).

![Imagen](/wp-content/uploads/2023/11/Manjaro-Jiraiya1.jpg)

![Imagen](/wp-content/uploads/2023/11/Mi-Manjaro.jpg)

  Me considero (o consideraba) Debianita, ya que fui usuario de **<a href="https://www.debian.org/" target="_blank" rel="noopener" title="Debian Gnu/Linux">Debian Gnu/Linux</a>** alrededor de 17 años. Mi última laptop, una vieja Lenovo Thinkpad T430 la tenía con **Debian Testing** usando Mate. Me pasé a Manjaro para probar otro entorno de escritorio y para ver si me adaptaba a la forma de trabajar en Manjaro. Actualmente tengo una Lenovo Thinkpad T470s usando <a href="https://kde.org/es/plasma-desktop/" target="_blank" rel="noopener" title="KDE Plasma">KDE Plasma</a>.

  Desde siempre he sido usuario de GTK/Gnome en general, pero cuando salió <a href="https://www.gnome.org/" target="_blank" rel="noopener" title="Gnome">Gnome</a> 3 y luego todas las demás cosas que le pusieron encima, me pasé a <a href="https://www.xfce.org/" target="_blank" rel="noopener" title="XFCE">XFCE</a>, hasta que encontré <a href="https://mate-desktop.org/" target="_blank" rel="noopener" title="Mate">Mate</a>, que básicamente es un Gnome2 renombrado y parchado. Probablemente me decidí a cambiar de aires por algún problema con LightDM o alguna actualización que me rompió el entorno gráfico y que a esas alturas y más pensando de forma más pragmática que otra cosa, me decidí a probar otra cosa.

![Imagen](/wp-content/uploads/2023/11/Manjaro-Nov2023.png)

  No era la primera vez que lo hacía, intenté usar varias distribuciones, como <a href="https://www.centos.org/" target="_blank" rel="noopener" title="CentOs">CentOs</a>, <a href="https://fedoraproject.org/es/" target="_blank" rel="noopener" title="Fedora">Fedora</a>, <a href="https://www.opensuse.org/" target="_blank" rel="noopener" title="Opensuse">Opensuse</a>, <a href="https://linuxmint.com/" target="_blank" rel="noopener" title="LinuxMint">LinuxMint</a> y alguna otra que ahorita no recuerdo. Y luego escuché de <a href="https://archlinux.org/" target="_blank" rel="noopener" title="ArchLinux">ArchLinux</a>, que es/era bastante popular y con mucha documentación siendo una rolling release, y me gustó y me llamó la atención su filosofía y la forma en cómo hacían las cosas. No estoy muy al tanto de todo lo que acontece, pero alguna que otra cosa básica la sé o la he leído.

  Al principio la idea era cambiarme a <a href="https://archlinux.org/" target="_blank" rel="noopener" title="">ArchLinux</a>, como mencioné, pensando de forma pragmática y práctica, quería una distribución que me quitara unas horas en la mañana o tarde, para tenerla funcionando, al menos con lo mínimo para que luego pudiese ir instalando los paquetes que fuese necesitando e ir transfiriendo la información de mi viejo equipo. Y aquí es dónde me topé con pared.

  <a href="https://archlinux.org/" target="_blank" rel="noopener" title="ArchLinux">ArchLinux</a>, a diferencia de la gran mayoría de distribuciones Gnu/Linux, no cuenta con un instalador como <a href="https://www.debian.org/" target="_blank" rel="noopener" title="Debian">Debian</a>/<a href="https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux" target="_blank" rel="noopener" title="Red Hat">Red Hat</a>/<a href="https://www.opensuse.org/" target="_blank" rel="noopener" title="OpenSuse">OpenSuse</a>/<a href="https://ubuntu.com/" target="_blank" rel="noopener" title="Ubuntu">Ubuntu</a> y una gran lista de distribuciones si lo tienen, y para mí y de forma personal, es un gran fallo. Porque había que hacer muchos pasos para hacer las particiones, formatear, copiar y todo ese proceso que se sigue. Y eso requería que invirtiera tiempo, esfuerzo y ganas, cosas que no tenía en ese momento.

  Como mencioné al principio, mi premisa es que fuese algo fácil de instalar, sin mucho esfuerzo y en el menor tiempo de ser posible, no más de 2-3 horas, incluyendo descargar la imágen, ponerla en un USB y finalmente instalarlo.

  Y ahí es donde entra <a href="https://manjaro.org/" target="_blank" rel="noopener" title="Manjaro">Manjaro</a>, pues si trae un instalador, a mi parecer bastante práctico, tal vez simple para algunas personas, pero que en mi caso particular, en ese tiempo que cumplían casi al 100 las premisas que me impuse. KDE Plasma no consume tanta memoria como solía hacerlo hace 10-20 años. No agobiarme con tantas opciones y tenerlo casi listo para usar contribuyeron mucho para darle una oportunidad. No se ha metido conmigo y me ha funcionado relativamente bien, razón por la cuál aún lo sigo usando.

  Nota: Si <a href="https://archlinux.org/" target="_blank" rel="noopener" title="ArchLinux">ArchLinux</a> tenía o ahora tiene algún método o instalador para facilitar esa tediosa labor de instalarlo por primera vez, me da mucho gusto, como mencioné en su momento, las formas que yo encontré en ese entonces nada más no me terminaron de convencer para darle una oportunidad. Si el próximo año me hago con una Lenovo Thinkpad más actualizada, tal vez me lo planteé.

  Ahora sí al problema. Resulta que tenía ya unas dos semanas sin actualizar <a href="https://manjaro.org/" target="_blank" rel="noopener" title="Manjaro">Manjaro</a>, no soy tan compulsivo para hacerlo cada semana, o peor, más de 2 veces a la semana D:

  Total, que primeramente me empezó a dar errores relacionados, al parecer, con Sublime Text. Tuve el error de no copiar esos mensajes de errores, al estar revisando el historial de Konsole, como lo dejé con 40k líneas, pues ya no me fue posible recuperarlos =(

---

  Los errores eran parecidos a estos:

```
"El archivo ... está dañado (paquete no válido o dañado (firma PGP))"
==> ERROR: No se pudo actualizar la clave: 206CBC892D1493D2
```

  Y en inglés algo parecido a esto:

```
:: Import PGP key 94657AB20F2A092B, "Andreas Radke <andyrtr@archlinux.org>"? [Y/n] 
error: key "Andreas Radke <andyrtr@archlinux.org>" could not be imported
:: Import PGP key C06086337C50773E, "Jelle van der Waa <jelle@archlinux.org>"? [Y/n] 
error: key "Jelle van der Waa <jelle@vdwaa.nl>" could not be imported
:: Import PGP key 9C02FF419FECBE16, "Morten Linderud <foxboron@archlinux.org>"? [Y/n] 
error: key "Morten Linderud <morten@linderud.pw>" could not be imported
```

  Buscando en internet intenté solucionarlo sin mucho éxito:

```
sudo pacman-mirrors -f 3 && sudo pacman -Syyu
sudo rm /var/cache/pacman/pkg/archlinux-keyring*
curl -O https://download.sublimetext.com/sublimehq-pub.gpg && sudo pacman-key --add sublimehq-pub.gpg && sudo pacman-key --lsign-key 8A8F901A && rm sublimehq-pub.gpg
sudo pacman -Scc
sudo pacman -Sy archlinux-keyring
```

  Finalmente, buscando encontré la información que necesitaba en las referencias que puse al final. A continuación los pasos que seguí y que sí funcionaron para poder actualizar Manjaro.

```
## Eliminar la cache de gnupg
sudo rm -rf /etc/pacman.d/gnupg/*

## Inicializar
sudo pacman-key --init

## Populate
sudo pacman-key --populate archlinux manjaro 

## Instalar keyrings
sudo pacman -Sy archlinux-keyring manjaro-keyring

## Refrescar llaves
sudo pacman-key --refresh-keys

## Actualizar el sistema
sudo pacman -Syyuu
```

---

  Y siguiendo esos pasos en esa secuencia fue que pude finalmente arreglar ese problema y actualizar los paquetes. Dejo algo de los mensajes que sí pude rescatar:

## Mensajes de la terminal 

gpg: keyring_get_keyblock: read error: Paquete incorrecto
gpg: keyring_get_keyblock failed: Anillo de claves incorrecto
gpg: fallo reconstruyendo caché del anillo de claves: Anillo de claves incorrecto
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: [don't know]: invalid packet (ctb=00)
gpg: keyring_get_keyblock: read error: Paquete incorrecto
gpg: keydb_get_keyblock failed: Anillo de claves incorrecto
gpg: validate_key_list failed
gpg: clave 206CBC892D1493D2: "Rémy Oudompheng <oudomphe@phare.normalesup.org>" sin cambios
gpg: Cantidad total procesada: 1
gpg:              sin cambios: 1
pub   rsa4096 2011-02-16 [SC]
      44EA62ACDBC81B6A0D1FD267206CBC892D1493D2
uid        [desconocida] Rémy Oudompheng <oudomphe@phare.normalesup.org>
uid        [desconocida] Rémy Oudompheng <remy@archlinux.org>
sub   rsa4096 2011-02-16 [E]

gpg: [don't know]: invalid packet (ctb=00)
gpg: renovación al servidor de claves fallida: Paquete incorrecto
==> ERROR: No se pudo actualizar la clave: 206CBC892D1493D2

sudo pacman-key --init                                                                                                                                                                                                     1 ✘ 
gpg: /etc/pacman.d/gnupg/trustdb.gpg: se ha creado base de datos de confianza
gpg: no se encuentran claves absolutamente fiables
==> Se está generando la clave principal de pacman, puede tardar un poco.
gpg: Generating pacman keyring master key...
gpg: creado el directorio '/etc/pacman.d/gnupg/openpgp-revocs.d'
gpg: certificado de revocación guardado como '/etc/pacman.d/gnupg/openpgp-revocs.d/DCE896ABBE2EBDC5E6AEC0C34FBA8F8FBC1658A7.rev'
gpg: Done
==> Actualizando la base de datos de claves de confianza...
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: nivel: 0  validez:   1  firmada:   0  confianza: 0-, 0q, 0n, 0m, 0f, 1u

sudo pacman-key --refresh-keys                                                                                                                                                                                               ✔ 
==> ERROR: No tiene permisos suficientes para leer el depósito pacman.
==> Use "pacman-key --init" para corregir los permisos del depósito.

sudo pacman-key --populate archlinux manjaro                                                                                                                                                                       1 ✘  34s  
==> Añadiendo las claves de archlinux.gpg...
==> Añadiendo las claves de manjaro.gpg...
==> Firmando localmente las claves de confianza en el depósito...
  -> Se han firmado localmente 23 claves.
==> Importando los valores de confianza del propietario...
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: inserting ownertrust of 4
gpg: setting ownertrust to 4
gpg: inserting ownertrust of 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: inserting ownertrust of 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
gpg: setting ownertrust to 4
==> Desactivando las claves revocadas en el depósito...
  -> Se han desactivado 46 claves.
==> Actualizando la base de datos de claves de confianza...
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: nivel: 0  validez:   1  firmada:  21  confianza: 0-, 0q, 0n, 0m, 0f, 1u
gpg: nivel: 1  validez:  21  firmada:  91  confianza: 0-, 0q, 0n, 21m, 0f, 0u
gpg: nivel: 2  validez:  68  firmada:  25  confianza: 68-, 0q, 0n, 0m, 0f, 0u
gpg: siguiente comprobación de base de datos de confianza el: 2023-12-07

sudo pacman -Sy archlinux-keyring manjaro-keyring                                                                                                                                                                    ✔  42s  
:: Sincronizando las bases de datos de los paquetes...
 core está actualizado
 extra está actualizado
 community está actualizado
 multilib está actualizado
:: Some packages should be upgraded first...
resolviendo dependencias...
buscando conflictos entre paquetes...

Paquetes (1) archlinux-keyring-20231113-1

Tamaño total de la instalación:  1.63 MiB
Tamaño neto tras actualizar:     0.01 MiB

:: ¿Continuar con la instalación? [S/n] s
(1/1) comprobando las claves del depósito                                                                                                     [#######################################################################################] 100%
(1/1) verificando la integridad de los paquetes                                                                                               [#######################################################################################] 100%
(1/1) cargando los archivos de los paquetes                                                                                                   [#######################################################################################] 100%
(1/1) comprobando conflictos entre archivos                                                                                                   [#######################################################################################] 100%
(1/1) comprobando el espacio disponible en el disco                                                                                           [#######################################################################################] 100%
:: Ejecutando los "hooks" de preinstalación...
(1/1) Creating Timeshift snapshot before upgrade...
==> skipping timeshift-autosnap due skipRsyncAutosnap in /etc/timeshift-autosnap.conf set to TRUE.
:: Procesando los cambios de los paquetes...
(1/1) actualizando archlinux-keyring                                                                                                          [#######################################################################################] 100%
==> Añadiendo las claves de archlinux.gpg...
==> Firmando localmente las claves de confianza en el depósito...
  -> Se han firmado localmente 1 claves.
==> Importando los valores de confianza del propietario...
gpg: inserting ownertrust of 4
==> Desactivando las claves revocadas en el depósito...
  -> Se han desactivado 3 claves.
==> Actualizando la base de datos de claves de confianza...
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: key CAA6A59611C7F07E: no user ID for key signature packet of class 10
gpg: marginals needed: 3  completes needed: 1  trust model: pgp
gpg: nivel: 0  validez:   1  firmada:  22  confianza: 0-, 0q, 0n, 0m, 0f, 1u
gpg: nivel: 1  validez:  22  firmada:  95  confianza: 0-, 0q, 0n, 22m, 0f, 0u
gpg: nivel: 2  validez:  73  firmada:  27  confianza: 73-, 0q, 0n, 0m, 0f, 0u
gpg: siguiente comprobación de base de datos de confianza el: 2023-12-31
:: Ejecutando los "hooks" de posinstalación...
(1/3) Reloading system manager configuration...
(2/3) Arming ConditionNeedsUpdate...
(3/3) Refreshing PackageKit...

advertencia: manjaro-keyring-20230719-2 está actualizado -- reinstalándolo
resolviendo dependencias...
buscando conflictos entre paquetes...

Paquetes (1) manjaro-keyring-20230719-2

Tamaño total de la instalación:  0.09 MiB
Tamaño neto tras actualizar:     0.00 MiB

:: ¿Continuar con la instalación? [S/n] s
(1/1) comprobando las claves del depósito                                                                                                     [#######################################################################################] 100%
(1/1) verificando la integridad de los paquetes                                                                                               [#######################################################################################] 100%
(1/1) cargando los archivos de los paquetes                                                                                                   [#######################################################################################] 100%
(1/1) comprobando conflictos entre archivos                                                                                                   [#######################################################################################] 100%
(1/1) comprobando el espacio disponible en el disco                                                                                           [#######################################################################################] 100%
:: Ejecutando los "hooks" de preinstalación...
(1/1) Creating Timeshift snapshot before upgrade...
==> skipping timeshift-autosnap due skipRsyncAutosnap in /etc/timeshift-autosnap.conf set to TRUE.
:: Procesando los cambios de los paquetes...
(1/1) reinstalando manjaro-keyring                                                                                                            [#######################################################################################] 100%
==> Añadiendo las claves de manjaro.gpg...
==> Firmando localmente las claves de confianza en el depósito...
  -> Se han firmado localmente 2 claves.
==> Importando los valores de confianza del propietario...
==> Actualizando la base de datos de claves de confianza...
gpg: siguiente comprobación de base de datos de confianza el: 2023-12-31
:: Ejecutando los "hooks" de posinstalación...
(1/2) Arming ConditionNeedsUpdate...
(2/2) Refreshing PackageKit...</pre>

---

## Referencias  
 

<ul class="wp-block-list">
  <li>
    <a href="https://wiki.archlinux.org/title/Pacman/Package_signing#Resetting_all_the_keys" target="_blank" rel="noopener" title="">https://wiki.archlinux.org/title/Pacman/Package_signing#Resetting_all_the_keys</a>
  </li>
  <li>
    <a href="https://forum.manjaro.org/t/pgp-could-not-be-imported/124279" target="_blank" rel="noopener" title="">https://forum.manjaro.org/t/pgp-could-not-be-imported/124279</a>
  </li>
  <li>
    <a href="https://www.linkedin.com/pulse/archlinux-paquete-v%C3%A1lido-o-da%C3%B1ado-firma-pgp-soluci%C3%B3n-en-d-ulivo" target="_blank" rel="noopener" title="">https://www.linkedin.com/pulse/archlinux-paquete-v%C3%A1lido-o-da%C3%B1ado-firma-pgp-soluci%C3%B3n-en-d-ulivo</a>
  </li>
  <li>
    <a href="https://bbs.archlinux.org/viewtopic.php?id=268153" target="_blank" rel="noopener" title="">https://bbs.archlinux.org/viewtopic.php?id=268153</a>
  </li>
  <li>
    <a href="https://forum.manjaro.org/t/error-firma-pgp/29231" target="_blank" rel="noopener" title="">https://forum.manjaro.org/t/error-firma-pgp/29231</a>
  </li>
</ul>
