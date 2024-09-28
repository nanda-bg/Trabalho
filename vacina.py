from datetime import date


class Vacina:
    def __init__(self, nome):
        self.__nome = nome
        self.__data = date.today().isoformat()

    @property
    def nome(self):
        return self.__nome

    @property
    def data(self):
        return self.__data
    
    def __str__(self):
        return f'Vacina {self.nome} aplicada em {self.data}'