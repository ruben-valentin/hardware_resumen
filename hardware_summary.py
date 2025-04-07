import platform  # Para obtener información del sistema operativo y hardware
import psutil  # Para obtener información sobre el uso de la CPU, memoria y almacenamiento
import cpuinfo  # Para obtener detalles sobre el procesador
import GPUtil  # Para obtener información sobre la GPU


def get_system_info():
    """
    Función para obtener información del hardware del sistema.
    Retorna un diccionario con detalles sobre el sistema operativo, CPU, memoria, almacenamiento y GPU.
    """
    info = {}  # Diccionario donde se almacenará la información recopilada

    # Información del sistema operativo
    info["Sistema Operativo"] = platform.system(
    ) + " " + platform.release()  # Nombre y versión del SO
    # Arquitectura del sistema (32 o 64 bits)
    info["Arquitectura"] = platform.architecture()[0]
    info["Nombre del Host"] = platform.node()  # Nombre del equipo en la red

    # Información del procesador
    cpu = cpuinfo.get_cpu_info()  # Obtiene la información detallada del procesador
    info["Procesador"] = cpu["brand_raw"]  # Marca y modelo del procesador
    info["Núcleos Físicos"] = psutil.cpu_count(
        logical=False)  # Número de núcleos físicos
    # Número de núcleos lógicos (con Hyper-Threading)
    info["Núcleos Lógicos"] = psutil.cpu_count(logical=True)
    # Frecuencia máxima del procesador en MHz
    info["Frecuencia (MHz)"] = psutil.cpu_freq().max

    # Memoria RAM
    ram = psutil.virtual_memory()  # Obtiene información sobre la memoria RAM
    info["Memoria RAM Total (GB)"] = round(
        ram.total / (1024**3), 2)  # Convertir de bytes a gigabytes

    # Almacenamiento
    # Obtiene información del almacenamiento principal
    disk = psutil.disk_usage('/')
    # Tamaño total del almacenamiento en GB
    info["Almacenamiento Total (GB)"] = round(disk.total / (1024**3), 2)
    info["Almacenamiento Disponible (GB)"] = round(
        disk.free / (1024**3), 2)  # Espacio disponible en GB

    # Información de la GPU
    try:
        gpus = GPUtil.getGPUs()  # Obtiene la lista de GPUs disponibles
        if gpus:
            info["GPU"] = gpus[0].name  # Nombre de la primera GPU detectada
            info["VRAM Total (GB)"] = round(
                gpus[0].memoryTotal, 2)  # Memoria de la GPU en GB
        else:
            info["GPU"] = "No se encontró GPU"
    except Exception as e:
        # En caso de error, se indica que no se pudo recuperar la información
        info["GPU"] = "No se pudo obtener información"

    return info  # Retorna el diccionario con la información del sistema


def print_system_info(info):
    """
    Función para imprimir la información del sistema de forma organizada.
    """
    print("\n📌 Resumen del Hardware del Sistema\n")  # Encabezado de la información
    for key, value in info.items():
        print(f"{key}: {value}")  # Imprime cada clave y valor del diccionario


if __name__ == "__main__":  # Punto de entrada principal del script
    system_info = get_system_info()  # Obtiene la información del sistema
    print_system_info(system_info)  # Imprime la información obtenida
