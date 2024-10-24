class DataFinalInvalida(Exception):
    def __init__(self):
        super().__init__("A data final deve ser maior que a data inicial.")