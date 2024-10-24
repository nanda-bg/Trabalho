from abc import ABC, abstractmethod
import re
from exception.cpfInvalidoException import CPFInvalidoException
from limite.abstract_tela import AbstractTela
from exception.booleanInvalidoException import BooleanInvalidoException
from exception.tipoHabitacaoInvalidoException import TipoHabitacaoInvalidoException
from exception.tamanhoHabitacaoInvalidoException import TamanhoHabitacaoInvalidoException
from exception.cpfInvalidoException import CPFInvalidoException
from exception.enderecoInvalidoException import EnderecoInvalidoException
from exception.nomeInvalidoException import NomeInvalidoException
from limite.abstract_tela import AbstractTela
from datetime import datetime
import re

class AbstractTelaPessoa(ABC):
    def __init__(self):
        super().__init__()

    def valida_cpf(self):
        while True:
            try:
                cpf = input("CPF: ")

                # Verifica se o CPF tem apenas números (11 dígitos)
                if re.match(r'^\d{11}$', cpf):
                    # Formata o CPF para NNN.NNN.NNN-NN
                    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                    return cpf_formatado
                
                # Verifica se o CPF já está no formato NNN.NNN.NNN-NN
                elif re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
                    return cpf
                
                else:
                    raise CPFInvalidoException()

            except CPFInvalidoException as e:
                self.mostrar_mensagem(e)       

    def valida_nome(self):
        while True:
            try:
                nome = input("Nome: ")
                if len(nome.strip()) < 3:
                    raise NomeInvalidoException()
                
                return nome
            
            except NomeInvalidoException as e:
                self.mostrar_mensagem(e)

    def valida_data_nascimento(self):
        while True:
            try:
                data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
                datetime.strptime(data_nascimento, "%Y-%m-%d")
                return data_nascimento
            except ValueError:
                self.mostrar_mensagem("Data inválida. O formato correto é AAAA-MM-DD.")

    def valida_endereco(self):
        while True:
            try:
                endereco = input("Endereço: ")
                if len(endereco.strip()) < 3:
                    raise EnderecoInvalidoException()
                
                return endereco
            
            except EnderecoInvalidoException as e:
                self.mostrar_mensagem(e)

    def valida_tipo_habitacao(self):
        while True:
            try:
                tipo_habitacao = input("Tipo de Habitação (casa/apartamento): ").lower()
                if tipo_habitacao not in ['casa', 'apartamento']:
                    raise TipoHabitacaoInvalidoException()
                
                return tipo_habitacao
            except TipoHabitacaoInvalidoException as e:
                self.mostrar_mensagem(e)

    def valida_tamanho_habitacao(self):
        while True:
            try:
                tamanho_habitacao = input("Tamanho da Habitação (pequeno/grande): ").lower()
                if tamanho_habitacao not in ['pequeno', 'grande']:
                    raise TamanhoHabitacaoInvalidoException()
                
                return tamanho_habitacao
            
            except TamanhoHabitacaoInvalidoException as e:
                self.mostrar_mensagem(e)

    def valida_possui_animais(self):
        while True:
            try:
                possui_animais = input("Possui Animais? (s/n): ").lower()

                if possui_animais not in ['s', 'n']:
                    raise BooleanInvalidoException()

                return possui_animais == 's'
            
            except BooleanInvalidoException as e:
                self.mostrar_mensagem(e) 
            