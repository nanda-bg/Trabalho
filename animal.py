from abc import ABC
from vacina import Vacina


class Animal(ABC):
    def __init__(self, chip: int, nome: str, raca: str, vacinas = None):
        self.__vacinas = []

        if vacinas:
            for vacina in vacinas:
                if not isinstance(vacina, Vacina):
                    raise ValueError(f'A vacina {vacina.nome} deve ser um objeto da classe Vacina.')
                
                self.__vacinas.append(vacina)
            
        self.__chip = chip
        self.__nome = nome
        self.__raca = raca

    @property
    def chip(self):
        return self.__chip
    
    @chip.setter
    def chip(self, chip: int):
        if not isinstance(chip, int):
            raise ValueError('O chip deve ser um número inteiro.')
        
        self.__chip = chip

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        if not isinstance(nome, str):
            raise ValueError('O nome deve ser uma string.')
        
        self.__nome = nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, raca: str):
        if not isinstance(raca, str):
            raise ValueError('A raça deve ser uma string.')
        
        self.__raca = raca
        
    @property
    def vacinas(self):
        return self.__vacinas


    def nova_vacina(self, vacina):
        if not isinstance(vacina, Vacina):
            raise ValueError('A vacina deve ser um objeto da classe Vacina.')
        
        self.__vacinas.append(vacina)    

    def tem_vacinas_basicas(self):
        vacinas_basicas = ['raiva', 'leptospirose', 'hepatite infecciosa']
        vacinas_dadas = [vacina.nome for vacina in self.__vacinas]

        for vacina in vacinas_basicas:
            if vacina not in vacinas_dadas:
                return False

        return True
    
    def __str__(self):
        return f'Chip: {self.__chip}, Nome: {self.__nome}, Raça: {self.__raca}'