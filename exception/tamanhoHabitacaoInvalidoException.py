class TamanhoHabitacaoInvalidoException(Exception):
    def __init__(self):
        super().__init__("O tamanho da habitação deve ser 'grande' ou 'pequeno'.")