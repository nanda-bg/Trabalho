from DAO.cachorro_dao import CachorroDAO
from DAO.gato_dao import GatoDAO
from entidade.cachorro import Cachorro
from entidade.gato import Gato
from entidade.vacina import Vacina
from view.tela_animal import TelaAnimal
from limite.tela_vacina import TelaVacina


class ControladorAnimal:
    def __init__(self, controlador_sistema, root=None):
        self.__cachorro_DAO = CachorroDAO()
        self.__gato_DAO = GatoDAO()
        self.animais_disponiveis = []
        self.__tela_vacina = TelaVacina()
        self.__controlador_sistema = controlador_sistema
        self.__root = root
        self.__tela_animal = TelaAnimal(self.__root)

    def adicionar_animal(self, chip = None, nome = None, raca = None, vacinas = None, tipo_animal = None, porte = None):
        if chip is None:
            dados_animal = self.__tela_animal.pega_dados_animal("cachorro")
            
            chip = dados_animal["chip"]
            nome = dados_animal["nome"]
            raca = dados_animal["raca"]
            vacinas = [Vacina(vacina) for vacina in dados_animal["vacinas"]]
            tipo_animal = dados_animal["tipo_animal"]
            if tipo_animal == "cachorro":
                porte = dados_animal["porte"]
            
        existe = self.buscar_animal(chip)

        if existe != None:
            print()
            self.__tela_animal.mostrar_mensagem("Chip já cadastrado.")
            return
            
        if tipo_animal == "cachorro":
            animal = Cachorro(chip, nome, raca, porte, vacinas)
            self.__cachorro_DAO.add(animal)

        else:    
            print("Vacinas", vacinas)
            print("Vacinas são do tipo: ", type(vacinas[0]))
            animal = Gato(chip, nome, raca, vacinas)
            self.__gato_DAO.add(animal)

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

        if vacina in animal.vacinas:
            print("O animal já possui a vacina selecionada.")
        else:
            print()
            self.__tela_vacina.mostrar_mensagem(f"{vacina} adicionada.")
        
            animal.vacinas.append(vacina)

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
            self.__tela_animal.mostrar_mensagem("Nenhum animal cadastrado")
            return
        
        self.__tela_animal.exibir_dados_cachorro(self.__cachorro_DAO.get_all())

        return self.__doador_DAO.get_all()
    
    def listar_animais_disponiveis(self):
        if len(self.animais_disponiveis) < 1:
            self.__tela_animal.mostrar_mensagem("Nenhum animal disponível")
            return
        
        for animal in self.animais_disponiveis:
            self.__tela_animal.mostrar_mensagem(animal)
        
    def seleciona_animal(self):
        chip = self.__tela_animal.valida_chip()
        return chip

    def buscar_animal(self, chip = None):
        valor_inicial = chip

        if chip == None:
            chip = self.__tela_animal.seleciona_animal() 

        for cachorro in self.__cachorro_DAO.get_all():
            if cachorro.chip == chip:
                if valor_inicial == None:
                    dados_cachorro = {"porte": cachorro.porte, "nome":cachorro.nome, "chip": cachorro.chip, "raca": cachorro.raca, "vacinas": cachorro.vacinas} 
                    self.__tela_animal.mostrar_animal(dados_cachorro)
                return cachorro
            
        for gato in self.__gato_DAO.get_all():
            if gato.chip == chip:
                if valor_inicial == None:    
                    dados_gato = {"nome":gato.nome, "chip": gato.chip, "raca": gato.raca, "vacinas": gato.vacinas} 
                    self.__tela_animal.mostrar_animal(dados_gato)
                return gato    
              
        if valor_inicial == None:      
            self.__tela_animal.mostrar_mensagem("Animal não encontrado.")      
        return None
        
    def alterar_animal(self):
        dados = self.__tela_animal.pega_dados_alteração()

        chip_original = dados["chip_original"]
        animal = self.buscar_animal(chip_original)

        novo_nome = dados["nome"]
        novo_chip = dados["chip_novo"]

        if novo_nome != None:
            animal.nome = novo_nome

        if novo_chip != None:
            animal.chip = novo_chip    

        return animal    

    def abrir_tela(self):
        lista_opcoes = {1: self.listar_animais, 2: self.listar_animais_disponiveis, 3: self.buscar_animal, 
                        4: self.adicionar_vacina, 5: self.remover_animal, 6: self.retornar}

        while True:
            opcao_escolhida = self.__tela_animal.mostrar_tela()

            if opcao_escolhida == 5:
                chip = self.__tela_animal.valida_chip()
                print()
                animal = self.buscar_animal(chip)
                print()

                if animal == None:
                    self.__tela_animal.mostrar_mensagem("Animal não encontrado.")

                else:
                    confirmar = input("Tem certeza que deseja remover esse animal? (s/n)")

                    if confirmar == "s":
                        self.remover_animal(animal)
                        self.__tela_animal.mostrar_mensagem("Animal removido com sucesso.")

                    else:
                        self.__tela_animal.mostrar_mensagem("Operação cancelada.")

            else:
                funcao_escolhida = lista_opcoes[opcao_escolhida]
                funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()