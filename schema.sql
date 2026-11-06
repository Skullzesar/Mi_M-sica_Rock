-- Base de datos y tabla única para el taller "Mi pasión en registros"
-- Temática: música rock

CREATE DATABASE IF NOT EXISTS musica_rock
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

USE musica_rock;

CREATE TABLE IF NOT EXISTS canciones (
    id             INT AUTO_INCREMENT PRIMARY KEY,
    nombre_cancion VARCHAR(100) NOT NULL,
    artista        VARCHAR(100) NOT NULL,
    genero         VARCHAR(50)  NOT NULL,
    fecha_registro DATE         NOT NULL,
    observacion    VARCHAR(255) NULL
) ENGINE=InnoDB;
