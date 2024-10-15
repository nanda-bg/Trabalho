class BooleanInvalidoException(Exception):
    def __init__(self):
        super().__init__("Somente 's' ou 'n' são aceitos como resposta.")