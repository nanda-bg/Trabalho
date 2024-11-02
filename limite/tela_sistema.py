from limite.abstract_tela import AbstractTela


class TelaSistema(AbstractTela):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA SISTEMA ---------")
        print("Escolha uma opção:")
        print("1 - Ir para tela de Pessoas")
        print("2 - Ir para tela de Animais")
        print("3 - Ir para tela de Adoção")
        print("4 - Ir para tela de Doação")
        print("5 - Ir para tela de Vacinas")
        print("0 - Finalizar sistema")

        print()
        
        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])