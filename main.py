# main.py
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo, Asesoria
from reservas import Reserva
from sistema import SistemaReservas
from gestion_logs import registrar_log
from typing import Callable

def ejecutar_operacion(numero: int, descripcion: str, logica: Callable) -> None:
    """
    Función que encapsula la ejecución de las operaciones en un bloque try/except.
    Garantiza que el programa nunca se detenga, incluso si las pruebas fallan.
    """
    print(f"[Op {numero}] - {descripcion}")
    try:
        # Ejecutamos la función de prueba que llega por parámetro
        logica()
    except Exception as e:
        # Si la prueba falla, atrapamos la excepción, mostramos el error y lo guardamos
        print(f"❌ Error controlado: {e}\n")
        registrar_log(f"Operación {numero} fallida: {e}")

def simulacion_completa() -> None:
    """
    Simulación principal que ejecuta 10 operaciones (exitosas y erróneas) 
    para demostrar la estabilidad del sistema y el manejo de excepciones.
    """
    # Guardamos en el log el inicio de la simulación
    registrar_log("--- INICIO DE SIMULACIÓN ---")
    
    # commit 2 Majurehy Lilian Coy Ruiz implementando listas como memoria
    # Instanciamos el sistema central que administra las listas internas
    sistema = SistemaReservas()
    
    # ---------------- PRUEBA 1: CLIENTE VÁLIDO ----------------
    def op1():
        global c1 # Usamos global para reutilizar este cliente en otras pruebas
        # Instanciamos un cliente válido y lo agregamos al sistema
        c1 = Cliente("1001", "Sindy Grisela", 25)
        sistema.agregar_cliente(c1)
    ejecutar_operacion(1, "Crear cliente válido", op1)

    # ---------------- PRUEBA 2: ERROR DE EDAD ----------------
    def op2(): 
        # Intentamos crear un menor de edad (esto lanzará ClienteInvalido)
        c_inv = Cliente("1002", "Pedro", 15)
        sistema.agregar_cliente(c_inv)
    ejecutar_operacion(2, "Crear cliente menor de edad", op2)

    # ---------------- PRUEBA 3: ERROR DE NOMBRE ----------------
    def op3(): 
        # Intentamos crear un cliente con nombre vacío
        Cliente("1003", "", 30)
    ejecutar_operacion(3, "Crear cliente sin nombre", op3)

    # ---------------- PRUEBA 4: RESERVA EXITOSA Y SOBRECARGA ----------------
    def op4():
        # Creamos un servicio de Sala y una Reserva
        s = ReservaSala(4, capacidad=10)
        r = Reserva(c1, s)
        sistema.agregar_reserva(r)
        # Usamos sobrecarga enviando los argumentos opcionales de impuesto y descuento
        r.confirmar(impuesto=0.19, descuento=0.10)
    ejecutar_operacion(4, "Reserva de sala exitosa", op4)

    # ---------------- PRUEBA 5: ERROR MATEMÁTICO AL CREAR SERVICIO ----------------
    def op5(): 
        # Intentamos alquilar una sala con horas negativas
        ReservaSala(-5, 20)
    ejecutar_operacion(5, "Crear servicio horas negativas", op5)

    # ---------------- PRUEBA 6: USO DE VALORES DEFAULT ----------------
    def op6():
        # Reservamos un equipo sin especificar impuestos (usa defaults)
        s = AlquilerEquipo(2, "Portátil")
        r = Reserva(c1, s)
        sistema.agregar_reserva(r)
        r.confirmar()
    ejecutar_operacion(6, "Alquiler de equipo", op6)

    # ---------------- PRUEBA 7: ERROR DE TIPADO ----------------
    def op7():
        # Pasamos un String en lugar de un objeto Cliente
        s = Asesoria(3, "Bases de datos")
        r = Reserva("String en vez de Cliente", s)
        sistema.agregar_reserva(r)
    ejecutar_operacion(7, "Reserva con cliente no instanciado", op7)

    # ---------------- PRUEBA 8: ESTADO INACTIVO ----------------
    def op8():
        # Desactivamos el servicio manualmente antes de reservarlo
        s = Asesoria(5, "Redes")
        s.disponible = False
        r = Reserva(c1, s)
    ejecutar_operacion(8, "Reserva servicio inhabilitado", op8)

    # ---------------- PRUEBA 9: ENCADENAMIENTO DE EXCEPCIONES ----------------
    def op9():
        s = ReservaSala(2, 5)
        r = Reserva(c1, s)
        # Rompemos el atributo interno para que estalle al multiplicar
        r.servicio.horas = "Texto" 
        r.confirmar()
    ejecutar_operacion(9, "Error matemático forzado (Encadenamiento)", op9)

    # ---------------- PRUEBA 10: RESERVA MASIVA ----------------
    def op10():
        # Creamos nuevo cliente y reservamos una asesoría larga
        c2 = Cliente("1004", "Andres Silva", 40)
        sistema.agregar_cliente(c2)
        s = Asesoria(10, "Experto Python")
        r = Reserva(c2, s)
        sistema.agregar_reserva(r)
        # Usamos sobrecarga parcial enviando solo el impuesto
        r.confirmar(impuesto=0.15)
    ejecutar_operacion(10, "Reserva larga duración", op10)

    # ---------------- REPORTE FINAL ----------------
    # Llamamos a los métodos encapsulados en el sistema para imprimir los resultados
    sistema.mostrar_clientes()
    sistema.mostrar_reservas()

# Punto de entrada principal de ejecución en Python
if __name__ == "__main__":
    simulacion_completa()