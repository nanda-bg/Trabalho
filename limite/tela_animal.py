from limite.abstract_tela import AbstractTela
from limite.abstract_tela_animal import AbstractTelaAnimal


class TelaAnimal(AbstractTela, AbstractTelaAnimal):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA ANIMAIS ----------")
        print("Escolha uma opção")
        print("1 - Listar todos os animais")
        print("2 - Listar animais disponíveis para adoção")
        print("3 - Buscar animal por chip")
        print("4 - Adicionar vacina")
        print("0 - Retornar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 0])
    
    def mostrar_mensagem(self, msg):
        print(msg)

    def mostrar_animal(self, animal):
        print(f"Nome: {animal.nome}")
        print(f"Chip: {animal.chip}")
        print(f"Raça: {animal.raca}")
        print(f"Vacinas: {animal.vacinas}")    
    