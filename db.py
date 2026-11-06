"""Conexión a MySQL. Los datos de acceso se leen de variables de entorno."""
import os

import mysql.connector

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "port": int(os.getenv("DB_PORT", "3306")),
    "user": os.getenv("DB_USER", "root"),
    "password": os.getenv("DB_PASSWORD", ""),
    "database": os.getenv("DB_NAME", "musica_rock"),
}


def get_connection():
    """Abre y devuelve una conexión nueva a la base de datos musica_rock."""
    return mysql.connector.connect(**DB_CONFIG)
