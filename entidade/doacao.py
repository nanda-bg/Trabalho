from datetime import date

class Doacao:
    def __init__(self, animal, doador, motivo_doacao, data = None):        
        if data is None:
            data = date.today().isoformat()
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
    
    @animal.setter
    def animal(self, animal):
        self.__animal = animal

    @property
    def doador(self):
        return self.__doador
    
    @doador.setter
    def doador(self, doador):
        self.__doador = doador

    @property
    def motivo_doacao(self):
        return self.__motivo_doacao
    
    @motivo_doacao.setter
    def motivo_doacao(self, motivo_doacao):
        self.__motivo_doacao = motivo_doacao

    def __str__(self):
        return f'{self.doador.nome} doou o animal {self.animal.nome}'    