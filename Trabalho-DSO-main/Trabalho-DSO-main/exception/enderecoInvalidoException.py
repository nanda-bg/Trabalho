class EnderecoInvalidoException(Exception):
    def __init__(self):
        super().__init__("O endereço deve conter pelo menos 3 caracteres.")