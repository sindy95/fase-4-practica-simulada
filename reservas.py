# reservas.py
from clientes import Cliente
from servicios import Servicio
from excepciones import ReservaError, ServicioNoDisponible
from gestion_logs import registrar_log
from typing import Optional

class Reserva:
    def __init__(self, cliente: Cliente, servicio: Servicio) -> None:
        if not isinstance(cliente, Cliente):
            raise ReservaError("El objeto no es un Cliente válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaError("El objeto no es un Servicio válido.")
        if not servicio.disponible:
            raise ServicioNoDisponible(f"El servicio {servicio.nombre} está inactivo.")

        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"
        self.costo_final = 0.0

    def confirmar(self, impuesto: Optional[float] = None, descuento: Optional[float] = None) -> None:
        # Prueba de commit 1 Majurehy Lilian Coy Ruiz: 
        # Aqui coloco una opcion de un cambio para implementar
        # Try, except, else, finally, encadenamiento de excepciones y manejo robusto
        print(f"--> Procesando reserva para el cliente {self.cliente.nombre}...")
        try:
            # calculando el costo del servicio prueba
            costo = self.servicio.calcular_costo(impuesto=impuesto, descuento=descuento)
            if costo <= 0:
                 raise ValueError("Cálculo inconsistente.")
                 
        except Exception as e:
            # Este error se guarda en el archivo logs.txt
            self.estado = "Error"
            registrar_log(f"error al confirmar reserva: {e}")
            # Encadenamiento de excepciones
            raise ReservaError("No se pudo confirmar la reserva") from e
            
        else:
            self.estado = "Confirmada"
            self.costo_final = costo
            print(f"✅ Reserva hecha correctamente. Precio: ${costo:,.2f}")
            registrar_log("Reserva confirmada")
            
        finally:
            registrar_log("Proceso de confirmacion realizado")
            print(f"Estado final de la transacción: [{self.estado}]\n")
            
    def cancelar(self) -> None:
        self.estado = "Cancelada"
        print("Reserva cancelada")