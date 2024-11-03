from limite.abstract_tela import AbstractTela
from limite.abstract_tela_pessoa import AbstractTelaPessoa


class TelaPessoa(AbstractTela, AbstractTelaPessoa):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA PESSOAS ----------")
        print("Escolha uma opção:")
        print("1 - Incluir Doador")
        print("2 - Incluir Adotante")
        print("3 - Listar Doadores")
        print("4 - Listar Adotantes")
        print("5 - Buscar Pessoa por CPF")
        print("6 - Alterar Doador")
        print("7 - Alterar Adotante")
        print("8 - Excluir Doador")
        print("9 - Excluir Adotante")
        print("0 - Retornar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    def pega_dados_doador(self):
        print("-------- DADOS DOADOR ----------")

        cpf = self.valida_cpf()
        nome = self.valida_nome()
        data_nascimento = self.valida_data_nascimento()
        endereco = self.valida_endereco()

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        }

    def pega_dados_adotante(self):
        print("-------- DADOS ADOTANTE ----------")

        cpf = self.valida_cpf()
        nome = self.valida_nome()
        data_nascimento = self.valida_data_nascimento()
        endereco = self.valida_endereco()
        tipo_habitacao = self.valida_tipo_habitacao()
        tamanho_habitacao = self.valida_tamanho_habitacao()
        possui_animais = self.valida_possui_animais()

        return {
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
            "tipo_habitacao": tipo_habitacao,
            "tamanho_habitacao": tamanho_habitacao,
            "possui_animais": possui_animais,
        }

    def mostrar_pessoa(self, pessoa):
        print(f"Nome: {pessoa.nome}")
        print(f"CPF: {pessoa.cpf}")
        print(f"Data de Nascimento: {pessoa.data_nascimento}")
        print(f"Endereço: {pessoa.endereco}")

        if hasattr(pessoa, "tipo_habitacao"):
            print(f"Tipo de Habitação: {pessoa.tipo_habitacao}")
            print(f"Tamanho da Habitação: {pessoa.tamanho_habitacao}")
            print(f"Possui Animais: {pessoa.possui_animais}")
        print("\n")

    def seleciona_pessoa(self):
        cpf = self.valida_cpf()
        return cpf

    def mostrar_mensagem(self, msg):
        print(msg)

    def valida_vacinas(self):
        print("-------- VACINAS DO ANIMAL ----------")
        vacinas = []
        while True:
            opcao = self.le_numero_inteiro(
                "Deseja adicionar uma vacina? (1 - Sim, 0 - Não): ", [0, 1]
            )
            if opcao == 0:
                break
            nome = input("Nome da vacina: ").strip()
            data = self.valida_data("Data da vacinação (dd/mm/aaaa): ")
            vacinas.append({"nome": nome, "data": data})
        return vacinas

    def pega_dados_alteracao_doador(self):
        cpf = self.valida_cpf()

        self.mostrar_mensagem("Digite os novos dados do doador. Para manter os dados antigos, apenas aperte Enter.")

        while True:
            nome = input("Nome (mínimo 3 caracteres): ")
            if nome == "" or len(nome) >= 3:
                break
            print("O nome deve ter pelo menos 3 caracteres.")

        while True:
            endereco = input("Endereço (mínimo 3 caracteres): ")
            if endereco == "" or len(endereco) >= 3:
                break
            print("O endereço deve ter pelo menos 3 caracteres.")

        return {
            "cpf": cpf,
            "nome": nome if nome != "" else None,
            "endereco": endereco if endereco != "" else None,
        }


    def pega_dados_alteracao_adotante(self):
        cpf = self.valida_cpf()

        self.mostrar_mensagem("Digite os novos dados do adotante. Para manter os dados antigos, apenas aperte Enter.")

        while True:
            nome = input("Nome (mínimo 3 letras): ")
            if nome == "" or len(nome) >= 3:
                break
            print("O nome deve ter pelo menos 3 letras.")

        while True:
            endereco = input("Endereço (mínimo 3 letras): ")
            if endereco == "" or len(endereco) >= 3:
                break
            print("O endereço deve ter pelo menos 3 letras.")

        while True:
            tipo_habitacao = input("Tipo de Habitação (casa ou apartamento): ").lower()
            if tipo_habitacao == "" or tipo_habitacao in ["casa", "apartamento"]:
                break
            print("O tipo de habitação deve ser 'casa' ou 'apartamento'.")

        while True:
            tamanho_habitacao = input("Tamanho da Habitação (pequeno ou grande): ").lower()
            if tamanho_habitacao == "" or tamanho_habitacao in ["pequeno", "grande"]:
                break
            print("O tamanho da habitação deve ser 'pequeno' ou 'grande'.")

        while True:
            possui_animais = input("Possui Animais (s/n): ").lower()
            if possui_animais == "":
                possui_animais = None
                break
            elif possui_animais in ["s", "n"]:
                possui_animais = (possui_animais == "s")
                break
            print("Digite 's' para sim ou 'n' para não.")

        return {
            "cpf": cpf,
            "nome": nome if nome != "" else None,
            "endereco": endereco if endereco != "" else None,
            "tipo_habitacao": tipo_habitacao if tipo_habitacao != "" else None,
            "tamanho_habitacao": tamanho_habitacao if tamanho_habitacao != "" else None,
            "possui_animais": possui_animais
        }
