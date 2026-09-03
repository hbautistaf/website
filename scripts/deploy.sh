#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue Automatizado para hbautista.com
# ==============================================================================
# Sube archivos nuevos y modificados vía SFTP/lftp hacia el servidor.
# NOTA: No utiliza '--delete' para proteger directorios y archivos existentes en
#       el servidor remoto ajenos a este blog.
# ==============================================================================

set -e

# --- Configuración del Servidor ---
SSH_USER="hbautista"
SSH_HOST="ftp.hbautista.com"
SSH_PORT="9822"
REMOTE_PATH="/home/hbautista/public_html/"

# --- Compilación de Hugo ---
echo "==> Limpiando y compilando sitio en Hugo..."
rm -rf public/
hugo --minify --gc

echo "==> Sitio generado con éxito en ./public/"

MODE="${1:-sftp}"

if [ "$MODE" == "sftp" ] || [ "$MODE" == "rsync" ]; then
    if ! command -v lftp &> /dev/null; then
        echo "Error: 'lftp' no está instalado localmente. Instálalo con: sudo pacman -S lftp"
        exit 1
    fi

    echo "==> Sincronizando archivos nuevos/modificados vía SFTP hacia $SSH_USER@$SSH_HOST:$REMOTE_PATH..."
    echo "==> [Seguridad] Los archivos y carpetas remotos existentes NO serán eliminados."

    lftp -c "
      open -u $SSH_USER, sftp://$SSH_HOST:$SSH_PORT;
      mirror -R \
        --only-newer \
        --verbose \
        --parallel=3 \
        public/ $REMOTE_PATH;
    "
    echo "==> ¡Despliegue incremental completado exitosamente!"

elif [ "$MODE" == "--dry-run" ]; then
    echo "==> [Simulación] Verificando archivos generados localmente:"
    find public -type f | head -n 30
    echo "... y $(find public -type f | wc -l) archivos en total."
else
    echo "Modo desconocido: $MODE. Usa 'sftp' o '--dry-run'."
    exit 1
fi
