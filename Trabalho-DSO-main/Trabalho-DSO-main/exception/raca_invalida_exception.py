class RacaInvalidaException(Exception):
    def __init__(self):
        super().__init__("A raça deve conter pelo menos 3 letras.")