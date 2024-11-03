from entidade.animal import Animal

class Gato(Animal):
    def __init__(self, chip, nome, raca, vacinas = None):
        super().__init__(chip, nome, raca, vacinas)

    def __str__(self):
        return f'Tipo: Gato, Chip: {self.chip}, Nome: {self.nome}, Raça: {self.raca}'                