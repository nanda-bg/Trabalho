from abc import ABC

class Pessoa(ABC):
    def __init__(self, cpf, nome, data_nascimento, endereco): 
        self.__nome = nome

        self.__data_nascimento = data_nascimento

        self.__endereco = endereco

        self.__cpf = cpf

    @property
    def cpf(self):
        return self.__cpf
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, endereco):
        self.__endereco = endereco
    
    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Endereço: {self.endereco}'