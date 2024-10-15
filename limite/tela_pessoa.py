from exception.booleanInvalidoException import BooleanInvalidoException
from exception.tipoHabitacaoInvalidoException import TipoHabitacaoInvalidoException
from exception.tamanhoHabitacaoInvalidoException import TamanhoHabitacaoInvalidoException
from exception.cpfInvalidoException import CPFInvalidoException
from exception.enderecoInvalidoException import EnderecoInvalidoException
from exception.nomeInvalidoException import NomeInvalidoException
from limite.abstract_tela import AbstractTela
from datetime import datetime
import re

class TelaPessoa(AbstractTela):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA PESSOAS ----------")
        print("Escolha uma opção")
        print("1 - Incluir Doador")
        print("2 - Incluir Adotante")
        print("3 - Listar Doadores")
        print("4 - Listar Adotantes")
        print("5 - Buscar Pessoa por CPF")
        print("0 - Retornar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ")

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR ----------")
        
        cpf = self.valida_cpf()
        nome = self.valida_nome()
        data_nascimento = self.valida_data_nascimento()
        endereco = self.valida_endereco()

        return {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
        
        cpf = self.valida_cpf()
        nome = self.valida_nome()
        data_nascimento = self.valida_data_nascimento()
        endereco = self.valida_endereco()
        tipo_habitacao = self.valida_tipo_habitacao()
        tamanho_habitacao = self.valida_tamanho_habitacao()
        possui_animais = self.valida_possui_animais()

        return {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco,
                "tipo_habitacao": tipo_habitacao, "tamanho_habitacao": tamanho_habitacao, "possui_animais": possui_animais}

    def mostra_pessoa(self, pessoa):
        print(f"Nome: {pessoa.nome}")
        print(f"CPF: {pessoa.cpf}")
        print(f"Data de Nascimento: {pessoa.data_nascimento}")
        print(f"Endereço: {pessoa.endereco}")

        if hasattr(pessoa, 'tipo_habitacao'):
            print(f"Tipo de Habitação: {pessoa.tipo_habitacao}")
            print(f"Tamanho da Habitação: {pessoa.tamanho_habitacao}")
            print(f"Possui Animais: {pessoa.possui_animais}")
        print("\n")

    def seleciona_pessoa(self):
        cpf = self.valida_cpf()
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)

    # Validações básicas de formatação
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
                print(e)      

    def valida_nome(self):
        while True:
            try:
                nome = input("Nome: ")
                if len(nome.strip()) < 3:
                    raise NomeInvalidoException()
                
                return nome
            
            except NomeInvalidoException as e:
                self.mostra_mensagem(e)

    def valida_data_nascimento(self):
        while True:
            try:
                data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
                datetime.strptime(data_nascimento, "%Y-%m-%d")
                return data_nascimento
            except ValueError:
                self.mostra_mensagem("Data inválida. O formato correto é AAAA-MM-DD.")

    def valida_endereco(self):
        while True:
            try:
                endereco = input("Endereço: ")
                if len(endereco.strip()) < 3:
                    raise EnderecoInvalidoException()
                
                return endereco
            
            except EnderecoInvalidoException as e:
                self.mostra_mensagem(e)

    def valida_tipo_habitacao(self):
        while True:
            try:
                tipo_habitacao = input("Tipo de Habitação (casa/apartamento): ").lower()
                if tipo_habitacao not in ['casa', 'apartamento']:
                    raise TipoHabitacaoInvalidoException()
                
                return tipo_habitacao
            except TipoHabitacaoInvalidoException as e:
                self.mostra_mensagem(e)

    def valida_tamanho_habitacao(self):
        while True:
            try:
                tamanho_habitacao = input("Tamanho da Habitação (pequeno/grande): ").lower()
                if tamanho_habitacao not in ['pequeno', 'grande']:
                    raise TamanhoHabitacaoInvalidoException()
                
                return tamanho_habitacao
            
            except TamanhoHabitacaoInvalidoException as e:
                self.mostra_mensagem(e)

    def valida_possui_animais(self):
        while True:
            try:
                possui_animais = input("Possui Animais? (s/n): ").lower()

                if possui_animais not in ['s', 'n']:
                    raise BooleanInvalidoException()

                return possui_animais == 's'
            
            except BooleanInvalidoException as e:
                self.mostra_mensagem(e) 
