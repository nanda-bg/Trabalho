class PorteInvalidoException(Exception):
    def __init__(self):
        super().__init__("O porte do animal deve ser 'pequeno', 'médio' ou 'grande'.")