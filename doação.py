from datetime import date
from animal import Animal
from doador import Doador


class Doacao:
    def __init__(self, ong, animal, doador, motivo_doacao, data = date.today().isoformat()):
        if not isinstance(animal, Animal):
            raise ValueError("animal deve ser um objeto da classe Animal")
        
        if not isinstance(doador, Doador):
            raise ValueError("doador deve ser um objeto da classe Doador")
        
        if not isinstance(motivo_doacao, str):
            raise ValueError("motivo_doacao deve ser uma string")
        
        self.__data = data
        self.__animal = animal
        self.__doador = doador
        self.__motivo_doacao = motivo_doacao
        self.__ong = ong

        self.doar()

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
    
    @property
    def ong(self):
        return self.__ong
    
    def doar(self):
        self.ong.doacoes.append(self)
        self.ong.adicionar_animal(self.animal)

    def __str__(self):
        return f'{self.doador.nome} doou o animal {self.animal.nome} para a ONG {self.ong.nome}'    