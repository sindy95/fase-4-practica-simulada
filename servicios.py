from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, disponible=True):
        self.nombre = nombre
        self.disponible = disponible

    @abstractmethod
    def calcular_costo(self, impuesto=0.0, descuento=0.0):
        pass

class ReservaSala(Servicio):
    def __init__(self, horas, capacidad):
        super().__init__(f"Reserva de Sala ({capacidad} pax)")
        if horas <= 0:
            raise ValueError("Las horas deben ser mayores a 0")
        self.horas = horas

    # Sobrecarga de método usando parámetros por defecto
    def calcular_costo(self, impuesto=0.19, descuento=0.0):
        base = self.horas * 50000
        return base + (base * impuesto) - (base * descuento)

class AlquilerEquipo(Servicio):
    def __init__(self, dias, tipo):
        super().__init__(f"Alquiler Equipo: {tipo}")
        if dias <= 0:
            raise ValueError("Los días deben ser mayores a 0")
        self.dias = dias

    def calcular_costo(self, impuesto=0.19, seguro_adicional=5000):
        base = self.dias * 30000
        return base + (base * impuesto) + seguro_adicional

class Asesoria(Servicio):
    def __init__(self, horas, especialista):
        super().__init__(f"Asesoría con {especialista}")
        self.horas = horas

    def calcular_costo(self, impuesto=0.19, descuento=0.0):
        base = self.horas * 80000
        return base + (base * impuesto) - (base * descuento)