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
            
            self.__tela_animal.mostrar_mensagem("Chip já cadastrado.")
            return
            
        if tipo_animal == "cachorro":
            animal = Cachorro(chip, nome, raca, porte, vacinas)
            self.__cachorro_DAO.add(animal)

        else:    
            animal = Gato(chip, nome, raca, vacinas)
            self.__gato_DAO.add(animal)

        return animal
    
    def remover_animal(self, animal = None):
        if animal in self.__cachorro_DAO.get_all():
            self.__cachorro_DAO.remove(animal.chip)
            
        elif animal in self.__gato_DAO.get_all():
            self.__gato_DAO.remove(animal.chip)

        else:
            self.__tela_animal.mostrar_mensagem("Animal não encontrado.")
        

    def adicionar_vacina(self, animal = None, vacinas = None):
        if animal == None:
            chip = self.__tela_animal.seleciona_animal()
            animal = self.buscar_animal(chip)

        if vacinas == None:
            vacinas = self.__tela_animal.pega_dados_vacina()    
            print("vacinas: ", vacinas)
        for vacina in vacinas["vacinas"]: 
            print("vacina: ", vacina)
            if vacina not in animal.vacinas:
                animal.vacinas.append(Vacina(vacina))
        
    def tem_vacinas_basicas(self, animal):
        vacinas_basicas = ['raiva', 'leptospirose', 'hepatite infecciosa']
        vacinas_dadas = [vacina.nome for vacina in animal.vacinas]

        for vacina in vacinas_basicas:
            if vacina not in vacinas_dadas:
                return False

        return True

    def listar_animais(self):
        todos_animais = list(self.__cachorro_DAO.get_all()) + list(self.__gato_DAO.get_all())
        if len(todos_animais) < 1:
            self.__tela_animal.mostrar_mensagem("Nenhum animal cadastrado")
            return
        
        self.__tela_animal.exibir_dados_animais(todos_animais)

        return todos_animais
    
    def listar_animais_disponiveis(self):
        animais_disponiveis = self.filtrar_animais_com_vacinas_basicas()

        if len(animais_disponiveis) < 1:
            self.__tela_animal.mostrar_mensagem("Nenhum animal disponível")
            return
        
        self.__tela_animal.exibir_dados_animais(animais_disponiveis)

        return animais_disponiveis

    def filtrar_animais_com_vacinas_basicas(self):
        todos_animais = list(self.__cachorro_DAO.get_all()) + list(self.__gato_DAO.get_all())
        return [animal for animal in todos_animais if animal.tem_vacinas_basicas]
        
        
    def seleciona_animal(self):
        chip = self.__tela_animal.valida_chip()
        return chip

    def buscar_animal(self, chip = None):
        valor_inicial = chip
        print("valor inicial", valor_inicial)

        if chip == None:
            chip = self.__tela_animal.seleciona_animal() 

        if chip != None:
            chip = int(chip)

            for cachorro in self.__cachorro_DAO.get_all():
                if cachorro.chip == chip:
                    if valor_inicial == None:
                        dados_cachorro = {"porte": cachorro.porte, "nome":cachorro.nome, "chip": str(cachorro.chip), "raca": cachorro.raca, "vacinas": cachorro.vacinas} 
                        self.__tela_animal.exibir_dados_animal(dados_cachorro, "cachorro")
                    return cachorro
                
            for gato in self.__gato_DAO.get_all():
                if gato.chip == chip:
                    if valor_inicial == None:    
                        dados_gato = {"nome":gato.nome, "chip": str(gato.chip), "raca": gato.raca, "vacinas": gato.vacinas} 
                        self.__tela_animal.exibir_dados_animal(dados_gato, "gato")
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
                
                animal = self.buscar_animal(chip)
                

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