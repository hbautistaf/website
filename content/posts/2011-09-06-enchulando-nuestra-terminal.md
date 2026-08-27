---
title: Enchulando nuestra terminal
date: 2011-09-07 04:26:20+00:00
slug: enchulando-nuestra-terminal
image: /wp-content/uploads/2011/09/Pant_bashrc-1.png
categories:
- Cómos
- Gnu/Linux
tags:
- Bash
- Consola
- Debian
- Gnu/Linux
- Howto
- Linux
- Terminal
- Tips
aliases:
- /2011/09/06/enchulando-nuestra-terminal/
- /comos/enchulando-nuestra-terminal/
---

Bash_demo

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Bash_demo-1.png?fit=564%2C607&ssl=1" class="aligncenter size-medium wp-image-721" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Bash_demo-1.png?resize=279%2C300&ssl=1" alt="" width="279" height="300" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Bash_demo-1.png?resize=279%2C300&ssl=1 279w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Bash_demo-1.png?w=564&ssl=1 564w" sizes="auto, (max-width: 279px) 100vw, 279px" />

  Pues hace un tiempo, <a title="Picando Código" href="http://picandocodigo.net/2009/personalizando-el-prompt-de-bash-en-debian/" target="_blank" rel="noopener">había encontrado</a> una bonita forma de poner el logo de <span style="color: #ff0000;">**Debian**</span> en mi perfil de **bash** (~/.bashrc) y me había gustado.

Pero con eso de que reinstalé (y probablemente dentro de muy poco lo vuelva a hacer :-/ ) perdí por completo esa utilidad.

Bueno, instalen el paquete fortune y todos aquellos adicionales que requieran que son varios:

```bash
hbautista@luke:~$ aptitude search fortune
v fortune -
v fortune-cookie-db -
i A fortune-mod - proporciona galletas de la fortuna bajo demanda
p fortune-zh - Chinese Data files for fortune
i fortunes - Archivos de datos que contienen mensajes de galletas de la suerte
p fortunes-bg - archivos de datos en búlgaro para fortune
i fortunes-bofh-excuses - BOFH excuses for fortune
p fortunes-br - Data files with fortune cookies in Portuguese
p fortunes-cs - Czech and Slovak data files for fortune
p fortunes-de - German data files for fortune
i fortunes-debian-hints - Debian Hints for fortune
p fortunes-eo - Collection of esperanto fortunes.
p fortunes-eo-ascii - Collection of esperanto fortunes (ascii encoding).
p fortunes-eo-iso3 - Collection of esperanto fortunes (ISO3 encoding).
i fortunes-es - Spanish fortune database
i fortunes-es-off - Frases de fortune en español (sección ofensiva)
p fortunes-fr - Frases de fortunes en francés
p fortunes-ga - Archivos de datos de fortune en irlandés (gaélico)
p fortunes-it - Archivos de datos que contienen citas de fortune en italiano
p fortunes-it-off - Archivos de datos en italiano que contienen frases de fortune, sección
p fortunes-mario - Archivos de fortune de Mario
i A fortunes-min - Archivos de datos que contienen frases de fortune
p fortunes-off - Archivos de datos que contienen frases de fortune ofensivas
p fortunes-pl - Archivos de datos de fortune en polaco
p fortunes-ru - Russian data files for fortune
p libfortune-perl - Perl module to read fortune (strfile) databases
hbautista@luke:~$
```

Después de eso, procedemos a editar nuestro **~/.bashrc** con el editor de su preferencia, en mi caso uso nano:

```bash
hbautista@luke:~$ nano .bashrc
```

Y copiar el siguiente código:

```bash
rojo='\e[1;31m'
NC='\e[0m'

echo -e "${rojo} _,met\$\$\$\$\$gg.";
echo -e " ,g\$\$\$\$\$\$\$\$\$\$\$\$\$\$\$P.";
echo -e " ,g\$\$P\"\" \"\"\"Y\$\$.\".";
echo -e " ,\$\$P' \`\$\$\$.";
echo -e " ',\$\$P ,ggs. \`\$\$b:";
echo -e " \`d\$\$' ,\$P\"' . \$\$\$";
echo -e " \$\$P d\$' , \$\$P";
echo -e " \$\$: \$\$. - ,d\$\$' ";
echo -e " \$\$; Y\$b._ _,d\$P' ${NC} _, _, ,'\`.";
echo -e "${rojo} Y\$\$. \`.\`\"Y\$\$\$\$P\"'${NC} \`\$\$' \`\$\$' \`. ,'";
echo -e "${rojo} \`\$\$b \"-.__ ${NC} \$\$ \$\$ \`'";
echo -e "${rojo} \`Y\$\$b ${NC} \$\$ \$\$ _, _";
echo -e "${rojo} \`Y\$\$. ${NC} ,d\$\$\$g\$\$ ,d\$\$\$b. \$\$,d\$\$\$b.\`\$\$' g\$\$\$\$\$b.\`\$\$,d\$\$b.";
echo -e "${rojo} \`\$\$b. ${NC} ,\$P' \`\$\$ ,\$P' \`Y\$. \$\$\$' \`\$\$ \$\$ \"' \`\$\$ \$\$\$' \`\$\$";
echo -e "${rojo} \`Y\$\$b. ${NC} \$\$' \$\$ \$\$' \`\$\$ \$\$' \$\$ \$\$ ,ggggg\$\$ \$\$' \$\$";
echo -e "${rojo} \`\"Y\$b._ ${NC} \$\$ \$\$ \$\$ggggg\$\$ \$\$ \$\$ \$\$ ,\$P\" \$\$ \$\$ \$\$";
echo -e "${rojo} \`\"\"\"\" ${NC} \$\$ ,\$\$ \$\$. \$\$ ,\$P \$\$ \$\$' ,\$\$ \$\$ \$\$";
echo -e "${NC} \`\$g. ,\$\$\$ \`\$\$._ _., \$\$ _,g\$P' \$\$ \`\$b. ,\$\$\$ \$\$ \$\$";
echo -e " \`Y\$\$P'\$\$. \`Y\$\$\$\$P',\$\$\$\$P\"' ,\$\$. \`Y\$\$P'\$\$.\$\$. ,\$\$.";
echo -e "${rojo}Debian GNU/Linux ${NC}" 'cat /etc/debian_version'

# Imprimimos algunas cosas interesantes en la pantalla
echo
echo "La cita del día:"
fortune -a
echo " --- "
```

Pant_ebashrc

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashrc-1.png?fit=648%2C380&ssl=1" class="aligncenter size-medium wp-image-723" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashrc-1.png?resize=300%2C176&ssl=1" alt="" width="300" height="176" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashrc-1.png?resize=300%2C176&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashrc-1.png?resize=768%2C450&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashrc-1.png?resize=1024%2C600&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashrc-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Lo guardamos y la próxima vez que entremos a la terminal veremos algo como lo siguiente:

Pant_bashrc

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc-1.png?fit=648%2C380&ssl=1" class="aligncenter size-medium wp-image-722" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc-1.png?resize=300%2C176&ssl=1" alt="" width="300" height="176" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc-1.png?resize=300%2C176&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc-1.png?resize=768%2C450&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc-1.png?resize=1024%2C600&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

También añadí como mencionan en el artículo anterior el siguiente código justo antes de imprimir la cita del día en el .bashrc de root.

```bash
root@luke:/home/hbautista# nano /root/.bashrc
```

```bash
# Esto es para la cuenta de root
echo -e '\e[1;31m';
echo " ______ _____ _____ _______";
echo " |_____/ | | | | |";
echo " | \_ |_____| |_____| |";
echo -e '\e[m';
echo "With great power comes great responsibility"
```

Pant_ebashroot

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashroot-1.png?fit=648%2C380&ssl=1" class="aligncenter size-medium wp-image-724" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashroot-1.png?resize=300%2C176&ssl=1" alt="" width="300" height="176" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashroot-1.png?resize=300%2C176&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashroot-1.png?resize=768%2C450&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashroot-1.png?resize=1024%2C600&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_ebashroot-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Y cuando se logueen como root, verán la siguiente pantalla:

Pant_bashrc2

" data-image-caption="" data-large-file="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc2-1.png?fit=648%2C380&ssl=1" class="aligncenter size-medium wp-image-725" src="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc2-1.png?resize=300%2C176&ssl=1" alt="" width="300" height="176" srcset="https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc2-1.png?resize=300%2C176&ssl=1 300w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc2-1.png?resize=768%2C450&ssl=1 768w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc2-1.png?resize=1024%2C600&ssl=1 1024w, https://i0.wp.com/blog.hbautista.com/wp-content/uploads/2011/09/Pant_bashrc2-1.png?w=1280&ssl=1 1280w" sizes="auto, (max-width: 300px) 100vw, 300px" /> 

Créditos a los que ya lo habían escrito 😉
