class NomeInvalidoException(Exception):
    def __init__(self):
        super().__init__("O nome deve conter pelo menos 3 caracteres.")