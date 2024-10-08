from datetime import datetime
import re

class TelaPessoa():
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

        opcao = int(input("Escolha a opção: "))
        print()

        return opcao

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
                print("CPF inválido. Insira no formato NNNNNNNNNNN ou NNN.NNN.NNN-NN.")

    def valida_nome(self):
        while True:
            nome = input("Nome: ")
            if len(nome.strip()) > 0:
                return nome
            else:
                print("Nome não pode ser vazio.")

    def valida_data_nascimento(self):
        while True:
            data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
            try:
                datetime.strptime(data_nascimento, "%Y-%m-%d")
                return data_nascimento
            except ValueError:
                print("Data inválida. O formato correto é AAAA-MM-DD.")

    def valida_endereco(self):
        while True:
            endereco = input("Endereço: ")
            if len(endereco.strip()) > 0:
                return endereco
            else:
                print("Endereço não pode ser vazio.")

    def valida_tipo_habitacao(self):
        while True:
            tipo_habitacao = input("Tipo de Habitação (casa/apartamento): ").lower()
            if tipo_habitacao in ['casa', 'apartamento']:
                return tipo_habitacao
            else:
                print("Tipo de Habitação inválido. Insira 'casa' ou 'apartamento'.")

    def valida_tamanho_habitacao(self):
        while True:
            tamanho_habitacao = input("Tamanho da Habitação (pequeno/grande): ").lower()
            if tamanho_habitacao in ['pequeno', 'grande']:
                return tamanho_habitacao
            else:
                print("Tamanho da Habitação inválido. Insira 'pequeno' ou 'grande'.")


    def valida_possui_animais(self):
        while True:
            possui_animais = input("Possui Animais? (True/False): ").lower()
            if possui_animais in ['true', 'false']:
                return possui_animais == 'true'
            else:
                print("Valor inválido. Digite 'True' ou 'False'.")    
