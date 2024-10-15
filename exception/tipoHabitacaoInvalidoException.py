class TipoHabitacaoInvalidoException(Exception):
    def __init__(self):
        super().__init__("O tipo da habitação deve ser 'casa' ou 'apartamento'.")