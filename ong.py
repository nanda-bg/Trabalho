from animal import Animal
from vacina import Vacina


class ONG:
    def __init__(self):
        self.todos_animais = []
        self.animais_disponiveis = []
        self.adocoes = []
        self.doacoes = []

    def adicionar_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("animal deve ser um objeto da classe Animal")
        
        self.todos_animais.append(animal)

        if animal.tem_vacinas_basicas():
            self.animais_disponiveis.append(animal)

    def remover_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("animal deve ser um objeto da classe Animal")
        
        if animal not in self.animais_disponiveis:
            raise ValueError("animal não disponível para adoção")
        
        self.todos_animais.remove(animal)

        if animal in self.animais_disponiveis:
            self.animais_disponiveis.remove(animal)

    def adicionar_vacina(self, animal, vacina: Vacina):
        if not isinstance(vacina, Vacina):
            raise ValueError('A vacina deve ser um objeto da classe Vacina.')
        
        if not isinstance(animal, Animal):
            raise ValueError('animal deve ser um objeto da classe Animal')
        
        animal.nova_vacina(vacina)

        if animal.tem_vacinas_basicas() and animal not in self.animais_disponiveis:
            self.animais_disponiveis.append(animal)

        
    def listar_animais(self):
        return [animal.nome for animal in self.todos_animais]
    
    def listar_animais_disponiveis(self):
        return [animal.nome for animal in self.animais_disponiveis]

    def emitir_relatorio_adocoes(self, inicio, fim):
        return [adocao for adocao in self.adocoes if inicio <= adocao.data <= fim]

    def emitir_relatorio_doacoes(self, inicio, fim):
        return [doacao for doacao in self.doacoes if inicio <= doacao.data <= fim]
    

    def __str__(self):
        return f'ONG com {len(self.todos_animais)} animais cadastrados, {len(self.animais_disponiveis)} disponíveis para adoção, {len(self.adocoes)} adoções e {len(self.doacoes)} doações'