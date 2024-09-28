from abc import ABC
from datetime import date

class Pessoa(ABC):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        if not isinstance(cpf, int):
            raise ValueError('O CPF deve ser um número inteiro')
        
        if not isinstance(nome, str):
            raise ValueError('O nome deve ser uma string')
        
        if not isinstance(data_nascimento, str):
            raise ValueError('A data de nascimento deve ser uma string no formato dd/mm/aaaa')
        
        if not isinstance(endereco, str):
            raise ValueError('O endereço deve ser uma string')
        
 
        self._nome = nome

        self._data_nascimento = data_nascimento

        self._endereco = endereco

        self._cpf = cpf

        if not self.validar_cpf():
            raise ValueError('CPF inválido')

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

    def validar_cpf(self):
        cpf = str(self.cpf)

        # Cria um conjunto com os dígitos únicos do CPF
        conjunto = set(list(cpf))

        # Verifica se o CPF tem todos os dígitos iguais, se tiver é inválido
        if len(conjunto) <= 1:
            return False

        else:
            # Define o multiplicador
            multiplicador = len(cpf) - 1

            # Define a variavél de parada do loop
            parada = multiplicador - 1

            # Define o comparador
            comparador = -2

            #Inicializa a variável de validação
            valido = True

            # Enquanto o comparador for menor que 0 e o CPF for válido
            while comparador < 0 and valido:
                # Define a variável de controle
                i = 0

                #Define a variável de soma
                soma = 0

                # Enquanto i for menor que a parada
                while i < parada:
                    # Adiciona o produto do dígito do CPF pelo multiplicador à soma
                    soma += int(cpf[i]) * multiplicador

                    # Diminui o multiplicador
                    multiplicador -= 1

                    # Avança o controle
                    i += 1
                    
                # Após pasar por todos os dígitos, calcula o resto da divisão da soma por 11    
                resto = soma % 11

                # Verifica se o dígito verificador é válido
                if  (resto <= 9 and int(cpf[comparador]) == 11-resto) or (resto > 9 and int(cpf[comparador]) == 0):
                        multiplicador = len(cpf)
                        parada = multiplicador-1
                        comparador += 1

                        return True

        return False
    
    def __str__(self):
        return f'Nome: {self.nome}, CPF: {self.cpf}, Data de nascimento: {self.data_nascimento}, Endereço: {self.endereco}'