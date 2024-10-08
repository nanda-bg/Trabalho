class TelaSistema:
    def tela_opcoes(self):
        print("-------- TELA SISTEMA ---------")
        print("Escolha uma opcao")
        print("1 - Ir para tela de Pessoas")
        print("2 - Ir para tela de Animais")
        print("3 - Ir para tela de Adoção")
        print("4 - Ir para tela de Doação")
        print("0 - Finalizar sistema")

        opcao = int(input("Escolha a opcao:"))

        return opcao