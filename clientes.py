from entidades import Entidad
from excepciones import ClienteInvalido

class Cliente(Entidad):
    def __init__(self, identificacion, nombre, edad):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad

    # Aplicando encapsulamiento y validaciones robustas
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or len(valor.strip()) < 3:
            raise ClienteInvalido("El nombre no puede estar vacío o ser muy corto.")
        self.__nombre = valor

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if not isinstance(valor, int) or valor < 18:
            raise ClienteInvalido("El cliente debe ser mayor de edad (18+).")
        self.__edad = valor

    def mostrar_info(self):
        return f"Cliente [ID: {self.identificacion}] - {self.nombre}, {self.edad} años"