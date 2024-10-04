from datetime import date
from adotante import Adotante
from doador import Doador


class ControladorPessoa():
    def __init__(self):
        self.adotantes = []
        self.doadores = []

    def incluir_doador(self, cpf, nome, data_nascimento, endereco):
        if self.verificacoes_basicas(cpf, nome, data_nascimento, endereco):
            doador = Doador(cpf, nome, data_nascimento, endereco)

            self.doadores.append(doador)

            return doador


    def incluir_adotante(self, cpf, nome, data_nascimento, endereco, tipo_habitacao, tamanho_habitacao, possui_animais):
        if not isinstance(tipo_habitacao, str):
            raise ValueError('O tipo de habitação deve ser uma string')
        
        if not isinstance(tamanho_habitacao, str):
            raise ValueError('O tamanho da habitação deve ser uma string')
        
        if not isinstance(possui_animais, bool):
            raise ValueError('O campo possui animais deve ser um booleano')
        
        if not self.validar_idade(data_nascimento):
            raise ValueError("O adotante precisa ser maior de 18 anos")
                
        if self.verificacoes_basicas(cpf,nome, data_nascimento, endereco):
            adotante = Adotante(cpf, nome, data_nascimento, endereco, tipo_habitacao, tamanho_habitacao, possui_animais)

            self.adotantes.append(adotante)

            return adotante

    def listar_doadores(self):
        return self.doadores
    
    def listar_adotantes(self):
        return self.adotantes

    def buscar_pessoa(self, cpf):
        pessoas = []
        pessoas.append(self.adotantes).append(self.doadores)

        for pessoa in pessoas:
            if pessoa.cpf == cpf:
                return pessoa
            return None
    
    def validar_idade(self, data_nascimento):
        # Passa a data de nascimento para o formato de data
        nascimento = date.fromisoformat(data_nascimento)

        # Calcula a idade
        idade = date.today().year - nascimento.year

        # Retorna se a pessoa é maior de idade
        return idade >= 18    

    def verificacoes_basicas(self, cpf, nome, data_nascimento, endereco):
        if not isinstance(cpf, int):
            return False
        
        if not self.validar_cpf(cpf):
            return False
        
        if not isinstance(nome, str):
            return False
        
        if not isinstance(data_nascimento, str):
            return False
        
        if not isinstance(endereco, str):
            return False
        
        return True
    

    def validar_cpf(self, cpf):
        cpf = str(cpf)
        conjunto = set(list(cpf))

        if len(conjunto) > 1:
            multiplicador = len(cpf)-1
            parada = multiplicador-1
            comparador = -2
            valido = True

            while comparador < 0 and valido:
                i = 0
                soma = 0
                while i < parada:
                    soma += int(cpf[i]) * multiplicador
                    multiplicador -= 1
                    i += 1
                    
                resto = soma%11

                if  (resto <= 9 and int(cpf[comparador]) == 11-resto) or (resto > 9 and int(cpf[comparador]) == 0):
                    multiplicador = len(cpf)
                    parada = multiplicador-1
                    comparador += 1
                else:
                    valido = False
        
        else:
            valido = False

        if not valido:
            raise ValueError("CPF inválido")
        
        else:
            return True