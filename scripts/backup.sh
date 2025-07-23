#!/bin/bash
# backup.sh - Backup a folder to a .tar.gz file

SOURCE_DIR="$1"
BACKUP_DIR="$HOME/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

if [ -d "$SOURCE_DIR" ]; then
    tar -czf "$BACKUP_DIR/backup_${TIMESTAMP}.tar.gz" "$SOURCE_DIR"
    echo "Backup of $SOURCE_DIR completed: $BACKUP_DIR/backup_${TIMESTAMP}.tar.gz"
else
    echo "Source directory does not exist: $SOURCE_DIR"
fi
