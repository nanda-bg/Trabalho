class TipoAnimalInvalidoException(Exception):
    def __init__(self):
        super().__init__("O tipo do animal deve ser 'cachorro' ou 'gato'.")