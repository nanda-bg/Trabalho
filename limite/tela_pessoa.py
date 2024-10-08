class TelaPessoa():
    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Doador")
        print("2 - Incluir Adotante")
        print("3 - Listar Doadores")
        print("4 - Listar Adotantes")
        print("5 - Buscar Pessoa por CPF")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR ----------")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
        endereco = input("Endereço: ")

        return {"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")
        cpf = input("CPF: ")
        nome = input("Nome: ")
        data_nascimento = input("Data de Nascimento (AAAA-MM-DD): ")
        endereco = input("Endereço: ")
        tipo_habitacao = input("Tipo de Habitação: ")
        tamanho_habitacao = input("Tamanho da Habitação: ")
        possui_animais = input("Possui Animais? (True/False): ").lower() == 'true'

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
        cpf = input("Digite o CPF da pessoa que deseja selecionar: ")
        return cpf

    def mostra_mensagem(self, msg):
        print(msg)
