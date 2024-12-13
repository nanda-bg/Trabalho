class CPFInvalidoException(Exception):
    def __init__(self):
        super().__init__("CPF inválido. Insira no formato NNNNNNNNNNN")