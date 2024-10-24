from entidade.animal import Animal
from entidade.vacina import Vacina
from limite.tela_animal import TelaAnimal


class ControladorAnimal:
    def __init__(self, controlador_sistema):
        self.todos_animais = []
        self.animais_disponiveis = []
        self.__tela_animal = TelaAnimal()
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

    def adicionar_vacina(self, animal, vacina: Vacina):
        if not isinstance(vacina, Vacina):
            raise ValueError('A vacina deve ser um objeto da classe Vacina.')
        
        if not isinstance(animal, Animal):
            raise ValueError('animal deve ser um objeto da classe Animal')
        
        animal.nova_vacina(vacina)

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
            print("Nenhum animal")
            return
        
        for animal in self.todos_animais:
            self.__tela_animal.mostrar_mensagem(animal)
    
    def listar_animais_disponiveis(self):
        if len(self.todos_animais) < 1:
            print("Nenhum animal")
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
            chip = self.__tela_animal.seleciona_animal() 

        animais = self.todos_animais

        for animal in animais:
            if animal.chip == chip:
                self.__tela_animal.mostra_animal(animal)
                return animal
        return None  





# REGRAS:
# NÃO PODE TER 2 ANIMAIS COM O MSM CHIP
# TEM Q TER AS 3 VACINAS BASICAS (RAIVA, LEPTOSPIROSE, HEPATITE INFECCIOSA) PARA PODER SER ADOTADO


# VAI PRECISAR DE UM MÉTODO DE "BUSCAR ANIMAL" PRA PODER ADOTAR, DE PREFERENCIA PELO CHIP

# Tenta fazer 2 listas no init, uma com todos os animais ou só com os que não tem as vacinas basicas, 
# e outra com os que já podem ser adotados


# FAZER PRIMEIRO SÓ COM AS VACINAS NORMAL, 
# DEPOIS QUE ESTIVER TUDO PRONTO, SE DER TEMPO,
# TENTAR FAZER A PARTE DE ADD O DIA DA VACINAÇÃO (FORA DO OBJETO VACINA)
# POSSIVELMENTE COM UM DICIONÁRIO

