import subprocess
import os

# Ruta del notebook
notebook_path = "archivo.ipynb"

# Verificar que el archivo existe
if not os.path.exists(notebook_path):
    raise FileNotFoundError("No se encontró el archivo .ipynb")

# Comando nbconvert
command = [
    "jupyter",
    "nbconvert",
    "--to",
    "pdf",
    notebook_path
]

# Ejecutar el comando
subprocess.run(command, check=True)

print("Conversión a PDF completada correctamente")
