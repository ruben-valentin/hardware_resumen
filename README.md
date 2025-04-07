# 📌 Guía para Obtener un Resumen de Hardware con Python y Virtualenv

Esta guía te ayudará a configurar un entorno virtual en Python y ejecutar un script para obtener un resumen del hardware de tu ordenador.

## 🚀 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- Python (versión 3.6 o superior)
- `pip` (el gestor de paquetes de Python)
- `virtualenv` (si no lo tienes, lo instalaremos en los siguientes pasos)

## 1️⃣ Crear y Activar un Entorno Virtual

Primero, abre una terminal y ejecuta los siguientes comandos:

### 🔹 Instalar Virtualenv (si no lo tienes)
```sh
pip install virtualenv
```

### 🔹 Crear un Entorno Virtual
```sh
virtualenv venv
```
Esto creará una carpeta llamada `venv` que contendrá todas las dependencias del proyecto.

### 🔹 Activar el Entorno Virtual
#### En Windows (CMD o PowerShell):
```sh
venv\Scripts\activate
```

#### En macOS/Linux:
```sh
source venv/bin/activate
```

Cuando el entorno virtual esté activo, verás `(venv)` antes del prompt en la terminal.

## 2️⃣ Instalar las Dependencias

Dentro del entorno virtual, instala las librerías necesarias:
```sh
pip install psutil py-cpuinfo GPUtil setuptools
```

Si estás usando Python 3.10 o superior, también actualiza `setuptools` y `pip`:
```sh
python -m pip install --upgrade pip setuptools
```

## 3️⃣ Crear el Script en Python

Crea un archivo llamado `hardware_summary.py` y copia el siguiente código:

```python
import platform
import psutil
import cpuinfo
import GPUtil

def get_system_info():
    info = {}

    # Información del sistema operativo
    info["Sistema Operativo"] = platform.system() + " " + platform.release()
    info["Arquitectura"] = platform.architecture()[0]
    info["Nombre del Host"] = platform.node()

    # Información del procesador
    cpu = cpuinfo.get_cpu_info()
    info["Procesador"] = cpu["brand_raw"]
    info["Núcleos Físicos"] = psutil.cpu_count(logical=False)
    info["Núcleos Lógicos"] = psutil.cpu_count(logical=True)
    info["Frecuencia (MHz)"] = psutil.cpu_freq().max

    # Memoria RAM
    ram = psutil.virtual_memory()
    info["Memoria RAM Total (GB)"] = round(ram.total / (1024**3), 2)

    # Almacenamiento
    disk = psutil.disk_usage('/')
    info["Almacenamiento Total (GB)"] = round(disk.total / (1024**3), 2)
    info["Almacenamiento Disponible (GB)"] = round(disk.free / (1024**3), 2)

    # Información de la GPU
    try:
        gpus = GPUtil.getGPUs()
        if gpus:
            info["GPU"] = gpus[0].name
            info["VRAM Total (GB)"] = round(gpus[0].memoryTotal, 2)
        else:
            info["GPU"] = "No se encontró GPU"
    except Exception as e:
        info["GPU"] = "No se pudo obtener información"

    return info

def print_system_info(info):
    print("\n📌 Resumen del Hardware del Sistema\n")
    for key, value in info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    system_info = get_system_info()
    print_system_info(system_info)
```

## 4️⃣ Ejecutar el Script

Para ejecutar el script, usa el siguiente comando:
```sh
python hardware_summary.py
```

Si todo está bien configurado, verás un resumen del hardware de tu sistema en la terminal.

## 5️⃣ Solución de Problemas

### ❌ Error `ModuleNotFoundError: No module named 'distutils'`
Si ves este error al ejecutar el script, instala `setuptools`:
```sh
pip install setuptools
```
O actualiza `pip` y `setuptools`:
```sh
python -m pip install --upgrade pip setuptools
```

### ❌ Error `GPUtil` no funciona en Python 3.10+
Si continúa el problema y estás en Python 3.10+, prueba utilizar una versión anterior de Python (3.9 o menor) o usa una alternativa como `torch.cuda` para verificar la GPU.

## 6️⃣ Salir y Eliminar el Entorno Virtual

Cuando termines, puedes desactivar el entorno virtual con:
```sh
deactivate
```

Si deseas eliminar completamente el entorno virtual, simplemente borra la carpeta `venv`:
```sh
rm -rf venv  # macOS/Linux
rd /s /q venv  # Windows
```

---

## 🎯 Conclusión
Siguiendo esta guía, has creado un script en Python para obtener información sobre el hardware de tu ordenador dentro de un entorno virtual seguro. Además, has aprendido a solucionar errores comunes relacionados con `GPUtil` y `distutils`. 🚀

