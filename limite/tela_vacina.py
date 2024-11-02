from limite.abstract_tela import AbstractTela
from limite.abstract_tela_animal import AbstractTelaAnimal


class TelaVacina(AbstractTela, AbstractTelaAnimal):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA VACINAS ----------")
        print("Escolha uma opção:")
        print("1 - Incluir vacina de raiva")
        print("2 - Incluir vacina de leptospirose")
        print("3 - Incluir vacina de hepatite infecciosa")
        print("4 - Incluir vacina de cinomose")
        print("5 - Incluir vacina de parvovirose")
        print("6 - Incluir vacina de coronavirose")
        print("0 - Retornar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 6, 0])
    
    def pega_dados_vacina(self):
        print("-------- DADOS VACINA ----------")
        chip_animal = self.valida_chip()

        return {"chip_animal": chip_animal}
    
    def mostrar_mensagem(self, mensagem):
        print(mensagem)
    
    


#Criar tela contendo as vacinas disponíveis(controlador vacinas)
# escolher umas 6 (3 das basicas e mais 3 do resto)

# concluir controlador vacina