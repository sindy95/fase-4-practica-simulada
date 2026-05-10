class ErrorSistema(Exception):
    """Clase base para las excepciones del sistema"""
    pass

class ClienteInvalido(ErrorSistema):
    pass

class ServicioNoDisponible(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    pass