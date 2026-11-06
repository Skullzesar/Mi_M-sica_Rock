"""Mi Música Rock - Taller CRUD básico (Create / Select) con Flask y MySQL."""
import os
from datetime import date

from flask import Flask, flash, redirect, render_template, request, url_for
from mysql.connector import Error

from db import get_connection

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "clave-de-desarrollo-solo-para-el-taller")

# Longitudes máximas definidas en la tabla (schema.sql)
LIMITES = {"nombre_cancion": 100, "artista": 100, "genero": 50, "observacion": 255}

GENEROS_SUGERIDOS = [
    "Rock clásico", "Hard rock", "Heavy metal", "Rock alternativo", "Grunge",
    "Punk rock", "Pop rock", "Rock en español", "Rock progresivo", "Blues rock",
]


def validar(datos):
    """RF06: devuelve la lista de errores de validación (vacía si todo está bien)."""
    errores = []
    etiquetas = {
        "nombre_cancion": "El nombre de la canción",
        "artista": "El artista",
        "genero": "El género",
    }
    for campo, etiqueta in etiquetas.items():
        if not datos[campo]:
            errores.append(f"{etiqueta} es obligatorio.")

    for campo, maximo in LIMITES.items():
        if len(datos[campo]) > maximo:
            errores.append(f"El campo {campo.replace('_', ' ')} no puede superar {maximo} caracteres.")

    if not datos["fecha_registro"]:
        errores.append("La fecha en que escuchaste la canción es obligatoria.")
    else:
        try:
            date.fromisoformat(datos["fecha_registro"])
        except ValueError:
            errores.append("La fecha no tiene un formato válido.")
    return errores


@app.route("/")
def index():
    """Muestra el formulario de registro (RF01)."""
    return render_template(
        "index.html",
        datos={"fecha_registro": date.today().isoformat()},
        generos=GENEROS_SUGERIDOS,
    )


@app.route("/guardar", methods=["POST"])
def guardar():
    """Valida el formulario y guarda la canción en MySQL (RF02, RF03, RF06)."""
    datos = {
        campo: request.form.get(campo, "").strip()
        for campo in ("nombre_cancion", "artista", "genero", "fecha_registro", "observacion")
    }

    errores = validar(datos)
    if errores:
        for error in errores:
            flash(error, "error")
        return render_template("index.html", datos=datos, generos=GENEROS_SUGERIDOS), 400

    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor()
        cursor.execute(
            "INSERT INTO canciones "
            "(nombre_cancion, artista, genero, fecha_registro, observacion) "
            "VALUES (%s, %s, %s, %s, %s)",
            (
                datos["nombre_cancion"],
                datos["artista"],
                datos["genero"],
                datos["fecha_registro"],
                datos["observacion"] or None,
            ),
        )
        conexion.commit()
        cursor.close()
    except Error as e:
        flash(f"No se pudo guardar la canción en la base de datos: {e}", "error")
        return render_template("index.html", datos=datos, generos=GENEROS_SUGERIDOS), 500
    finally:
        if conexion is not None and conexion.is_connected():
            conexion.close()

    flash(f"¡Canción «{datos['nombre_cancion']}» registrada!", "ok")
    return redirect(url_for("canciones"))


@app.route("/canciones")
def canciones():
    """Consulta todos los registros con SELECT y los muestra en una tabla (RF04, RF05)."""
    registros = []
    conexion = None
    try:
        conexion = get_connection()
        cursor = conexion.cursor(dictionary=True)
        cursor.execute(
            "SELECT id, nombre_cancion, artista, genero, fecha_registro, observacion "
            "FROM canciones ORDER BY id DESC"
        )
        registros = cursor.fetchall()
        cursor.close()
    except Error as e:
        flash(f"No se pudo consultar la base de datos: {e}", "error")
    finally:
        if conexion is not None and conexion.is_connected():
            conexion.close()

    return render_template("canciones.html", canciones=registros)


if __name__ == "__main__":
    app.run(debug=True)
