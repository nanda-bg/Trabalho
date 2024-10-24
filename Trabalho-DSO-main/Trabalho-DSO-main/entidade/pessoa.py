from abc import ABC

class Pessoa(ABC):
    def __init__(self, cpf, nome, data_nascimento, endereco): 
        self._nome = nome

        self._data_nascimento = data_nascimento

        self._endereco = endereco

        self._cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    
    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def data_nascimento(self):
        return self._data_nascimento

    @property
    def endereco(self):
        return self._endereco

    @endereco.setter
    def endereco(self, endereco):
        self._endereco = endereco
    
    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Endereço: {self.endereco}'