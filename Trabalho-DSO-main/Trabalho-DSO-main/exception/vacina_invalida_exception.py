class VacinaInvalidaException(Exception):
    def __init__(self):
        super().__init__('A vacina deve ser um objeto da classe Vacina.')
