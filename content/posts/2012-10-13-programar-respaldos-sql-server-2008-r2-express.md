---
title: Programar respaldos SQL Server 2008 r2 express
date: 2012-10-13 17:41:05+00:00
slug: programar-respaldos-sql-server-2008-r2-express
image: /images/2012/sql_server_2008_r2_small-1.jpg
categories:
- Cómos
tags:
- Backups
- Scripts
- SQL
- SQL Server
- sqlcmd
aliases:
- /2012/10/13/programar-respaldos-sql-server-2008-r2-express/
- /comos/programar-respaldos-sql-server-2008-r2-express/
---

![SQL Server 2008 R2](/images/2012/sql_server_2008_r2_small-1.jpg)

Resulta que por cuestiones laborales tengo la necesidad de hacer respaldos de una base de datos del MS SQL Server 2008 R2 express, y pues resulta que aunque se pueda instalar el <a title="MS SQL Server Management Studio Express" href="http://www.microsoft.com/es-es/download/details.aspx?id=8961" target="_blank" rel="noopener">MS SQL Server Management Studio Express</a>, simplemente no podremos tener un plan de mantenimiento o automatización, puesto que esa <a title="http://msdn.microsoft.com/en-us/library/ms187658.aspx" href="http://msdn.microsoft.com/en-us/library/ms187658.aspx" target="_blank" rel="noopener">versión carece</a> del <a title="SQL Agent Service" href="http://msdn.microsoft.com/en-us/library/ms189237.aspx" target="_blank" rel="noopener">SQL Agent Service</a>.

  Buscando una posible solución me encontré muchas formas de hacerlo.

  * Usando <a title="SQL Server Databases Backup with PowerShell" href="http://j.mp/QXNgXc" target="_blank" rel="noopener">Powershell</a>
  * Usando el <a title="Management Studio 1" href="http://www.sectorgamer.com/threads/crear-respaldos-autom%C3%A1ticos-en-sql-server-2005-y-2008.3570/" target="_blank" rel="noopener">Management</a> Studio
  * <a title="Backups automáticos de SQL Server Express" href="http://j.mp/QXNpcX" target="_blank" rel="noopener">Management Studio</a> con un archivo .bat
  * Y finalmente usando <a title="Backup automáticos de bases de datos SQL Server 2008" href="http://j.mp/QXNqh2" target="_blank" rel="noopener">sqlcmd</a>

  Claro, el Management Studio te facilita enormemente las cosas, puedes realizar muchas cosas más aparte de los planes de mantenimiento.

  

![Multi-Server-Mgmt-Dashboard](/images/2012/Multi-Server-Mgmt-Dashboard-1.png)

  Había una forma bastante simple de hacerlo y la encontré <a title="Hacer backup de Sql server mediante línea de comandos" href="http://j.mp/QXNLjK" target="_blank" rel="noopener">aquí</a>, pero me encontré con el inconveniente de que para empezar si ejecutaba el comando sqlcmd así sin argumentos, simplemente me marcaba un error:

```bash
sqlcmd
HResult 0x2, Level 16, State 1
Named Pipes Provider: Could not open a connection to SQL Server [2].
```

Entonces ahí mismo encontré este <a title="Hacer backup de Sql server mediante línea de comandos" href="http://j.mp/QXNLjK" target="_blank" rel="noopener">interesante artículo</a> donde habla de cómo usar esa shell de SQL Server. Las pruebas simples que hice funcionaron muy bien y ahí habría quedado sino fuera porque quería que me guardara el formato de fecha y hora, porque como quedan en un mismo directorio (por ahora), el anterior no me funcionaba, porque me machacaría las copias previas.

Así que use <a title="Backup automáticos de bases de datos SQL Server 2008" href="http://j.mp/QXNqh2" target="_blank" rel="noopener">este otro</a> que está más elaborado. Aunque lo tuve que cambiar debido a que no me gustaba la forma en que me dejaba los nombres de los archivos generados. Como ya tenía rato de no tocar este tipo de cosas, pues a googlear un poco y me encontré dos interesantes artículos: <a title="How to Format Date/Time" href="http://j.mp/QXOLoh" target="_blank" rel="noopener">How to format Date/Time</a> y <a title="Date and Time Conversions Using SQL Server" href="http://j.mp/QXONwi" target="_blank" rel="noopener">Date and Time Conversions Using SQL Server</a>, esos artículos me ayudaron a entender mejor la forma de tratar las fechas.

Funcionó, hice varias pruebas y funcionaron ambas, pero aún no estaba del todo contento con el resultado, sobre todo porque me dejaba archivos del tipo: **RespaldoBD\_13.10.2012\_12:40.BAK** y esos puntos en las fechas no me gustaban nadita ¬¬.

Hasta que finalmente vi que había una función que podría facilitarme un poco las cosas: <a title="Substring Transact_SQL" href="http://j.mp/QXP7LD" target="_blank" rel="noopener">Substring()</a>.

Así que este es el código como finalmente quedó:

```sql
declare @fecha varchar(MAX)
declare @archivo varchar(MAX)
set @fecha = SUBSTRING(Convert(Varchar(10), GetDate(),105),1,2)+SUBSTRING(Convert(Varchar(10), GetDate(),105),4,2)+SUBSTRING(Convert(Varchar(10), GetDate(),105),7,4)+'_'+SUBSTRING(CONVERT(Varchar(10), GetDate(),108),1,2)+SUBSTRING(CONVERT(Varchar(10), GetDate(),108),4,2)
set @archivo ='C:\Ruta\del\Directorio\Base_De_Datos_'+@fecha+'.bak'
BACKUP DATABASE Base_De_Datos_Respaldada
TO DISK = @archivo
   WITH FORMAT,
      MEDIANAME = 'D_SQLServerBackups',
      NAME = 'Full Backup of ERP2012_Pycsur';
GO
```

El anterior archivo lo pueden guardar en un archivo de texto "archivo.sql" y se manda a llamar así:

```bash
sqlcmd -S Servidor\Instancia_BD -i C:\Ruta\archivo.sql
```

Ese último comando lo pueden poner en el programador de tareas y listo, proceso automatizado ñ_ñ
