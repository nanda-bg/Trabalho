class MotivoInvalidoException(Exception):
    def __init__(self):
        super().__init__("O motivo deve conter pelo menos 4 letras.")