class ChipInvalidoException(Exception):
    def __init__(self):
        super().__init__("O chip deve conter 7 caracteres numéricos.")