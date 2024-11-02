from entidade.animal import Animal
from entidade.vacina import Vacina
from limite.tela_animal import TelaAnimal
from limite.tela_vacina import TelaVacina


class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.todos_animais = []
        self.animais_disponiveis = []
        self.__tela_animal = TelaAnimal()
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistema = controlador_sistema

    def adicionar_animal(self, chip = None, nome = None, raca = None, vacinas = None):
        if chip is None:
            dados_animal = self.__tela_doacao.pega_dados_animal()
            chip = dados_animal["chip"]
            nome = dados_animal["nome"]
            raca = dados_animal["raca"]
            vacinas = dados_animal["vacinas"] #LISTA
            
        animal = Animal(chip, nome, raca, vacinas)
        
        self.todos_animais.append(animal)

        if animal.tem_vacinas_basicas():
            self.animais_disponiveis.append(animal)

        return animal    
    
    def remover_animal(self, animal):
        if animal not in self.todos_animais:
            raise ValueError("animal não pertence a ONG")

        self.todos_animais.remove(animal)

        if animal in self.animais_disponiveis:
            self.animais_disponiveis.remove(animal)

    def adicionar_vacina(self, animal = None, vacina = None):
        if animal == None:
            opcoes = {1: "raiva", 2: "leptospirose", 3: "hepatite infecciosa", 
                        4: "cinomose", 5: "parvovirose", 6: "coronavirose"}
            
            self.__controlador_sistema.controlador_vacina.abrir_tela()

        self.__tela_vacina.mostrar_mensagem(f"Vacina {vacina} selecionada")
       
        animal.vacinas.append(vacina)
        self.__tela_animal.mostrar_animal(animal)

        if animal.tem_vacinas_basicas() and animal not in self.animais_disponiveis:
            self.animais_disponiveis.append(animal)
        
    def tem_vacinas_basicas(self, animal):
        vacinas_basicas = ['raiva', 'leptospirose', 'hepatite infecciosa']
        vacinas_dadas = [vacina.nome for vacina in animal.vacinas]

        for vacina in vacinas_basicas:
            if vacina not in vacinas_dadas:
                return False

        return True

    def listar_animais(self):
        if len(self.todos_animais) < 1:
            self.__tela_animal.mostrar_mensagem("Nenhum animal")
            return
        
        for animal in self.todos_animais:
            self.__tela_animal.mostrar_mensagem(animal)
    
    def listar_animais_disponiveis(self):
        if len(self.todos_animais) < 1:
            self.__tela_animal.mostrar_mensagem("Nenhum animal")
            return
        
        for animal in self.animais_disponiveis:
            self.__tela_animal.mostrar_mensagem(animal)

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_animais, 2: self.listar_animais_disponiveis, 3: self.buscar_animal, 
                        4: self.adicionar_vacina, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_animal.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
        
    def seleciona_animal(self):
        chip = self.__tela_animal.valida_chip()
        return chip

    def buscar_animal(self, chip = None):
        if chip == None:
            chip = self.seleciona_animal() 

        animais = self.todos_animais

        for animal in animais:
            if animal.chip == chip:
                self.__tela_animal.mostrar_animal(animal)
                return animal
        return None  
