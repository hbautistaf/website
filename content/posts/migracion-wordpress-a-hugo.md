---
title: "Migrando de WordPress a Hugo: Un nuevo capítulo más rápido y ligero"
date: 2026-09-02T16:00:00-06:00
draft: false
tags: ["Hugo", "WordPress", "Web Development", "Markdown", "Static Site Generator"]
categories: ["Tech"]
description: "Detalles sobre la migración del blog de WordPress a un generador de sitios estáticos basado en Hugo."
---

Después de tiempo manteniendo el blog sobre **WordPress**, he decidido dar el paso hacia un generador de sitios estáticos: **Hugo**.

### ¿Por qué dejar WordPress?

Aunque WordPress sigue siendo una de las herramientas más robustas y populares del mercado, para las necesidades de mi sitio web personal resultaba innecesariamente complejo:

- **Mantenimiento constante:** Actualizaciones frecuentes de plugins, temas y del núcleo de PHP.
- **Rendimiento y velocidad:** Un sitio estático sirve archivos HTML directamente desde el servidor o un CDN sin consultar bases de datos MySQL en cada petición.
- **Seguridad:** Al no ejecutar PHP ni depender de una base de datos activa, la superficie de ataque se reduce drásticamente.

<!--more-->

### La nueva arquitectura con Hugo

La nueva versión del sitio y del blog (`hbautista.com/blog/`) está construida con **Hugo** y gestionada totalmente en Markdown a través de Git:

1. **Flujo de trabajo limpio:** Redacto las entradas localmente usando archivos Markdown y mantengo todo el código fuente versionado en [GitHub](https://github.com/hbautistaf/website).
2. **Generación ultrarrápida:** Hugo compila todo el sitio en cuestión de milisegundos.
3. **Control total del diseño y despliegue:** Mayor flexibilidad sobre el código HTML/CSS generado.

El contenido anterior ha sido exportado e integrado en este nuevo formato. ¡Espero que disfruten de la mejora en velocidad y simplicidad!
