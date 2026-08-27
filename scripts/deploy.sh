#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue Automatizado para hbautista.com
# ==============================================================================
# Uso:
#   ./scripts/deploy.sh rsync       -> Despliegue mediante SSH / rsync
#   ./scripts/deploy.sh ftp         -> Despliegue mediante FTPS / LFTP
#   ./scripts/deploy.sh --dry-run   -> Simulación sin subir archivos
# ==============================================================================

set -e

# --- Configuración del Servidor (Personalizar con los datos de tu hosting) ---
SSH_USER="tu_usuario_ssh"
SSH_HOST="hbautista.com"
SSH_PORT="22"
REMOTE_PATH="/var/www/hbautista.com/public_html/"

FTP_HOST="ftp.hbautista.com"
FTP_USER="tu_usuario_ftp"
FTP_PASS="tu_contraseña_ftp"
FTP_REMOTE_PATH="/public_html/"

# --- Compilación de Hugo ---
echo "==> Limpiando y compilando sitio en Hugo..."
rm -rf public/
hugo --minify --gc

echo "==> Sitio generado con éxito en ./public/"

MODE="${1:-rsync}"

if [ "$MODE" == "rsync" ]; then
    echo "==> Sincronizando con rsync / SSH hacia $SSH_USER@$SSH_HOST:$REMOTE_PATH..."
    rsync -avz --delete \
        -e "ssh -p $SSH_PORT" \
        public/ "$SSH_USER@$SSH_HOST:$REMOTE_PATH"
    echo "==> ¡Despliegue con SSH completado exitosamente!"

elif [ "$MODE" == "ftp" ]; then
    if ! command -v lftp &> /dev/null; then
        echo "Error: 'lftp' no está instalado. Instálalo con: sudo apt install lftp (o pacman -S lftp)"
        exit 1
    fi
    echo "==> Sincronizando mediante LFTP / FTPS hacia $FTP_HOST:$FTP_REMOTE_PATH..."
    lftp -c "
      set ftp:ssl-allow yes;
      set ssl:verify-certificate no;
      open -u $FTP_USER,$FTP_PASS $FTP_HOST;
      mirror -R --delete --verbose public/ $FTP_REMOTE_PATH;
    "
    echo "==> ¡Despliegue con LFTP completado exitosamente!"

elif [ "$MODE" == "--dry-run" ]; then
    echo "==> [Simulación] Verificando archivos que se subirían:"
    find public -type f | head -n 30
    echo "... y $(find public -type f | wc -l) archivos en total."
else
    echo "Modo desconocido: $MODE. Usa 'rsync', 'ftp' o '--dry-run'."
    exit 1
fi
