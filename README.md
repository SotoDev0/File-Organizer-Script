# File Organizer Python Script 📂

Este es un script de automatización desarrollado en **Python** diseñado para organizar directorios caóticos (como la carpeta de Descargas) clasificando los archivos automáticamente en carpetas según su extensión.

## Propósito del Script
El objetivo de este script es comprender el funcionamiento de la libreria OS y practicar la interacción con el sistema Operativo

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Librerías estándar:** * `os`: Para manipulación de rutas y directorios.
    * `shutil`: Para operaciones avanzadas de movimiento de archivos.

## 📋 Funcionalidades
- [x] **Clasificación automática:** Detecta la extensión de cada archivo y crea una carpeta correspondiente.
- [x] **Seguridad integrada:** El script ignora archivos con extensión `.py` para evitar moverse a sí mismo durante la ejecución.
- [x] **Manejo de archivos sin extensión:** Agrupa archivos desconocidos en una carpeta específica para evitar pérdida de datos.

## 🔧 Cómo usarlo
1. Clona este repositorio o descarga el archivo `organizador.py`.
2. Coloca el script en la carpeta que deseas organizar.
3. Ejecuta el script desde tu terminal:
   ```bash
   python organizador.py