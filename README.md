# Mi Música Rock — Taller CRUD básico (Create / Select)

Aplicación web con **Python + Flask + MySQL** para registrar las canciones de rock que he escuchado
y consultarlas en una tabla HTML. Tema oscuro con acentos neón.

## Estructura

```
musica_rock/
├── app.py              # Rutas Flask: formulario, guardar (INSERT) y consultar (SELECT)
├── db.py               # Conexión a MySQL (variables de entorno)
├── schema.sql          # Crea la base de datos musica_rock y su única tabla
├── requirements.txt
├── templates/
│   ├── base.html       # Estructura común (menú, mensajes)
│   ├── index.html      # Formulario de registro
│   └── canciones.html  # Tabla generada con los datos de MySQL
└── static/css/style.css
```

## Cómo ejecutarla

1. **Requisitos:** Python 3.9+ y un servidor MySQL (o MariaDB) en marcha.
2. **Crear la base de datos y la tabla:**
   ```
   mysql -u root -p < schema.sql
   ```
   (o pega el contenido de `schema.sql` en MySQL Workbench / phpMyAdmin).
3. **Entorno virtual e instalación:**
   ```
   python -m venv venv
   venv\Scripts\activate          # Windows   (Linux/macOS: source venv/bin/activate)
   pip install -r requirements.txt
   ```
4. **Credenciales de MySQL** (por defecto: `localhost`, usuario `root`, sin contraseña, base `musica_rock`):
   ```
   set DB_PASSWORD=tu_clave       # Windows CMD
   $env:DB_PASSWORD="tu_clave"    # Windows PowerShell
   export DB_PASSWORD=tu_clave    # Linux/macOS
   ```
   También se pueden cambiar `DB_HOST`, `DB_PORT`, `DB_USER` y `DB_NAME`.
5. **Iniciar:** `python app.py` y abrir <http://127.0.0.1:5000>.

## Prueba sugerida (mínimo 5 canciones)

formulario con cinco canciones:

| Canción | Artista | Género |
|---|---|---|
| Smells Like Teen Spirit | Nirvana | Grunge |
| Sweet Child O' Mine | Guns N' Roses | Hard rock |
| Enter Sandman | Metallica | Heavy metal |
| Zombie | The Cranberries | Rock alternativo |
| Persiana Americana | Soda Stereo | Rock en español |

Luego entra a **Mis canciones**: la tabla se llena con un `SELECT` a MySQL.

## Cumplimiento del taller

| Requerimiento | Dónde |
|---|---|
| RF01 Formulario HTML | `templates/index.html` |
| RF02 Guardar en MySQL | `app.py` → `guardar()` (INSERT con parámetros) |
| RF03 Python y Flask | `app.py` |
| RF04 SELECT de todos los registros | `app.py` → `canciones()` |
| RF05 Tabla HTML | `templates/canciones.html` (bucle Jinja) |
| RF06 Campos obligatorios | `app.py` → `validar()` |
