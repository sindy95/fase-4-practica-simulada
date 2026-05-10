import datetime

def registrar_log(mensaje):
    # Escribe los eventos y errores sin borrar el historial
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"[{datetime.datetime.now()}] - {mensaje}\n")