from datetime import date

class Doacao:
    def __init__(self, animal, doador, motivo_doacao, data = date.today().isoformat):        
        self.__data = data
        self.__animal = animal
        self.__doador = doador
        self.__motivo_doacao = motivo_doacao

    @property
    def data(self):
        return self.__data

    @property
    def animal(self):
        return self.__animal

    @property
    def doador(self):
        return self.__doador

    @property
    def motivo_doacao(self):
        return self.__motivo_doacao

    def __str__(self):
        return f'{self.doador.nome} doou o animal {self.animal.nome}'    