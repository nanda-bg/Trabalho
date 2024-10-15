from limite.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA SISTEMA ---------")
        print("Escolha uma opcao")
        print("1 - Ir para tela de Pessoas")
        print("2 - Ir para tela de Animais")
        print("3 - Ir para tela de Adoção")
        print("4 - Ir para tela de Doação")
        print("0 - Finalizar sistema")

        return self.le_numero_inteiro("Escolha uma opção: ")