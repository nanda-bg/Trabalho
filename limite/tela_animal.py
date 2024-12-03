from limite.abstract_tela import AbstractTela
from limite.abstract_tela_animal import AbstractTelaAnimal
from limite.abstract_tela_vacina import AbstractTelaVacina


class TelaAnimal(AbstractTela, AbstractTelaAnimal, AbstractTelaVacina):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA ANIMAIS ----------")
        print("Escolha uma opção:")
        print("1 - Listar todos os animais")
        print("2 - Listar animais disponíveis para adoção")
        print("3 - Buscar animal por chip")
        print("4 - Adicionar vacina")
        print("5 - Remover animal")
        print("6 - Alterar animal")
        print("0 - Retornar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 6, 0])
    
    def mostrar_mensagem(self, msg):
        print(msg)

    def mostrar_animal(self, animal):
        if hasattr(animal, "porte"):
            print("Tipo: Cachorro")
            print(f"Porte: {animal.porte}")
        else:
            print("Tipo: Gato")    
        print(f"Nome: {animal.nome}")
        print(f"Chip: {animal.chip:}")
        print(f"Raça: {animal.raca}")
        print(f"Vacinas: {[str(vacina) for vacina in animal.vacinas]}")  

    def pega_dados_alteracao(self):
        chip_original = self.valida_chip()

        self.mostrar_mensagem("Digite os novos dados do animal. Para manter os dados antigos, apenas aperte Enter.")

        nome = input("Nome: ")
        if nome == "":
            nome = None

        chip_novo = input("Novo Chip (7 dígitos numéricos): ")
        if chip_novo:
            while not chip_novo.isdigit() or len(chip_novo) != 7:
                self.mostrar_mensagem("O chip deve ter 7 dígitos numéricos.")
                chip_novo = input("Novo Chip (7 dígitos numéricos): ")
        else:
            chip_novo = None

        return {"chip_original": chip_original, "chip_novo": chip_novo, "nome": nome}
    
    def pega_dados_animal(self):
        chip = self.valida_chip()
        nome = self.valida_nome_animal()
        raca = self.valida_raca_animal()
        vacinas = self.valida_vacinas()
        tipo_animal = self.valida_tipo_animal()

        if tipo_animal == "cachorro":
            porte = self.valida_porte()
            return {"chip": chip, "nome": nome, "raca": raca, "vacinas": vacinas, "tipo_animal": tipo_animal, "porte": porte}
        
        else:
            return {"chip": chip, "nome": nome, "raca": raca, "vacinas": vacinas, "tipo_animal": tipo_animal}

        