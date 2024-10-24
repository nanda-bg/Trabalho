from limite.abstract_tela import AbstractTela


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

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])

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

    