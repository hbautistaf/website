#!/usr/bin/env bash
# ==============================================================================
# Script de Despliegue Automatizado para hbautista.com
# ==============================================================================
# Sube archivos nuevos y modificados vía SFTP/lftp hacia el servidor.
# NOTA: No utiliza '--delete' para proteger directorios y archivos existentes en
#       el servidor remoto ajenos a este blog.
# ==============================================================================

set -euo pipefail

# --- Configuración del Servidor ---
SSH_USER="hbautista"
SSH_HOST="ftp.hbautista.com"
SSH_PORT="9822"
REMOTE_PATH="/home/hbautista/public_html/"
SSH_KEY="${HOME}/.ssh/id_rsa"

# --- Preflight: Validar llave SSH ---
preflight_check() {
    # Verificar que la llave SSH existe
    if [ ! -f "$SSH_KEY" ]; then
        echo "Error: Llave SSH no encontrada en $SSH_KEY"
        echo "       Genera una con: ssh-keygen -t ed25519 -f $SSH_KEY"
        exit 1
    fi

    # Verificar permisos correctos (600)
    KEY_PERMS=$(stat -c "%a" "$SSH_KEY")
    if [ "$KEY_PERMS" != "600" ]; then
        echo "Error: Permisos incorrectos en $SSH_KEY (actual: $KEY_PERMS, requerido: 600)"
        echo "       Corrige con: chmod 600 $SSH_KEY"
        exit 1
    fi

    # Verificar conectividad SSH antes de intentar el despliegue
    echo "==> Verificando acceso SSH a $SSH_HOST:$SSH_PORT..."
    if ! ssh -q -o BatchMode=yes -o ConnectTimeout=8 \
             -i "$SSH_KEY" -p "$SSH_PORT" \
             "${SSH_USER}@${SSH_HOST}" exit 2>/dev/null; then
        echo "Error: No se pudo establecer conexión SSH con $SSH_HOST:$SSH_PORT"
        echo "       Verifica que la llave pública esté en el servidor:"
        echo "       ssh-copy-id -i ${SSH_KEY}.pub -p $SSH_PORT ${SSH_USER}@${SSH_HOST}"
        exit 1
    fi
    echo "==> Acceso SSH verificado correctamente."
}

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

    preflight_check

    echo "==> Sincronizando archivos nuevos/modificados vía SFTP hacia $SSH_USER@$SSH_HOST:$REMOTE_PATH..."
    echo "==> [Seguridad] Los archivos y carpetas remotos existentes NO serán eliminados."

    lftp -c "
      set sftp:connect-program 'ssh -a -x -i $SSH_KEY';
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
