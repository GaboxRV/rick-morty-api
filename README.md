# Rick and Morty API

## Herramientas necesarias

- Python 3.14 o superior
- Poetry
- Conexión a internet

## Instalar Poetry en Windows

Si Poetry aún no está instalado, abre PowerShell y ejecuta:

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Para más información, consulta la [guía oficial de instalación de Poetry](https://python-poetry.org/docs/#installing-with-the-official-installer).

Reinicia la terminal y verifica que el comando esté disponible:

```powershell
poetry --version
```

Si el comando no está disponible, verifica que la ruta de instalación de Poetry esté incluida en `PATH`.

## Instalación y ejecución

Desde la carpeta del proyecto, instala las dependencias:

```powershell
poetry install
```

Ejecuta el script:

```powershell
poetry run python .\test.py
```
