# sistema.py
from clientes import Cliente
from reservas import Reserva
from excepciones import ClienteInvalido, ReservaError
from gestion_logs import registrar_log
from typing import List

class SistemaReservas:
    # Prueba de commit 2 Majurehy Lilian Coy Ruiz: sistema de reservas con listas sin bases de datos
    def __init__(self) -> None:
        self.clientes: List[Cliente] = []
        self.reservas: List[Reserva] = []

    def agregar_cliente(self, cliente: Cliente) -> None:
        if not isinstance(cliente, Cliente):
            raise ClienteInvalido("Solo se puede ingresar clientes válidos")
        self.clientes.append(cliente)
        registrar_log("Ingreso de cliente exitoso")

    def agregar_reserva(self, reserva: Reserva) -> None:
        if not isinstance(reserva, Reserva):
            raise ReservaError("Solo reservas válidas")
        self.reservas.append(reserva)
        registrar_log("Reserva ingresada correctamente")

    def mostrar_clientes(self) -> None:
        print("\n--- Clientes registrados ---")
        for cliente in self.clientes:
            print(cliente.mostrar_info())

    def mostrar_reservas(self) -> None:
        print("\n--- Reservas realizadas ---")
        for reserva in self.reservas:
            print(
                f"Cliente: {reserva.cliente.nombre} | "
                f"Servicio: {reserva.servicio.nombre} | "
                f"Estado: {reserva.estado} | Total: ${reserva.costo_final:,.2f}"
            )