import datetime
from DAO.adocao_dao import AdocaoDAO
from entidade.adotante import Adotante
from entidade.adocao import Adocao
from entidade.cachorro import Cachorro
from view.tela_adocao import TelaAdocao


class ControladorAdocao:
    def __init__(self, controlador_sistema, root):
        self.__adocoes_DAO = AdocaoDAO()
        self.__root = root
        self.__tela_adocao = TelaAdocao(self.__root)
        self.__controlador_sistema = controlador_sistema

    def emitir_relatorio_adocoes(self):
        datas = self.__tela_adocao.pega_datas_relatorio()

        formato_data = "%Y-%m-%d"

        # Converter as datas de string para datetime
        inicio = datetime.datetime.strptime(datas["inicio"], formato_data)
        fim = datetime.datetime.strptime(datas["fim"], formato_data)

        adocoes = [adocao for adocao in self.__adocoes_DAO.get_all() if inicio <= datetime.datetime.strptime(adocao.data, formato_data) <= fim]
        if len(adocoes) == 0:
            self.__tela_adocao.mostrar_mensagem(
                "Nenhuma adoção realizada nesse período"
            )
            return

        self.__tela_adocao.exibir_dados_adocoes(adocoes)

        return adocoes

    def avaliar_adocao(self, animal, adotante):
        print("animal adocao", animal)
        print("adotante adocao", adotante)
        print("isinstance", isinstance(animal, Cachorro))


        if isinstance(animal, Cachorro):
            if animal.porte == "grande" and (
                adotante.tipo_habitacao == "apartamento"
                and adotante.tamanho_habitacao == "pequeno"
            ):
                return False

        vacinas_basicas = ['raiva', 'leptospirose', 'hepatite infecciosa']
        vacinas_dadas = [vacina.nome.lower() for vacina in animal.vacinas]

        print("vacinas_dadas", vacinas_dadas)

        for vacina in vacinas_basicas:
            if vacina not in vacinas_dadas:
                print("vacina não dada: ", vacina)
                return False

        return True

    def adotar(self):
        
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        cpf = dados_adocao["cpf_adotante"]
        chip = dados_adocao["chip_animal"]

        adotante = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(cpf)

        if adotante != None and not isinstance(adotante, Adotante):
            self.__tela_adocao.mostrar_mensagem("CPF já cadastrado para um doador e não pode ser utilizado para adoção")
            return

        elif adotante == None:
            cadastrar = self.__tela_adocao.deseja_cadastrar_adotante()

            if cadastrar == "s":
                adotante = (
                    self.__controlador_sistema.controlador_pessoa.incluir_adotante()
                )

            else:
                self.__tela_adocao.mostrar_mensagem(
                    "O processo de adoção não foi concluído"
                )
                return

        animal = self.__controlador_sistema.controlador_animal.buscar_animal(chip)

        if animal == None:
            self.__tela_adocao.mostrar_mensagem("Animal não encontrado")
            return

        if self.avaliar_adocao(animal, adotante):
            
            self.__tela_adocao.mostrar_mensagem(
                f"Adoção do animal {animal.nome} aprovada."
            )

            adocao = Adocao(animal, adotante)
            self.__adocoes_DAO.add(adocao)

            if adocao.termo_assinado == False:
                assinar_termo = self.__tela_adocao.deseja_assinar_termo(adocao)

            if assinar_termo == "s" or adocao.termo_assinado:
                self.assinar_termo_adocao(adocao)
                
            else:
                self.__tela_adocao.mostrar_mensagem(
                    f"Processo de adoção não foi concluído."
                )
                return

            self.__tela_adocao.mostrar_mensagem(f"Adoção realizada com sucesso.")

        else:
            self.__tela_adocao.mostrar_mensagem(f"Adoção não aprovada.")


    def assinar_termo_adocao(self, adocao=None):
        if adocao == None:
            adocao = self.buscar_adocao()

            if adocao == None:
                self.__tela_adocao.mostrar_mensagem("Adoção não encontrada")
                return
        
        assinar = self.__tela_adocao.assinar_termo(adocao)
        

        if assinar == "s":
            adocao.termo_assinado = True
            self.__adocoes_DAO.update(adocao)
            self.__controlador_sistema.controlador_animal.remover_animal(adocao.animal)
            self.__tela_adocao.mostrar_mensagem("Termo de adoção assinado com sucesso")
            return

        self.__tela_adocao.mostrar_mensagem("Termo de adoção não foi assinado")
        return


    def excluir_adocao(self):
        chip_animal = self.__tela_adocao.seleciona_animal()

        for adocao in self.__adocoes_DAO.get_all():
            if adocao.animal.chip == chip_animal:
                
                dados_adocao = {"nome_adotante": adocao.adotante.nome, "cpf_adotante": adocao.adotante.cpf, "nome_animal": adocao.animal.nome, "chip_animal": adocao.animal.chip, "data_adocao": adocao.data}
                
                confirma = self.__tela_adocao.confirmar_exclusão(dados_adocao)

                if confirma.lower() == "s":
                    if hasattr(adocao.animal, "porte"):
                        self.__controlador_sistema.controlador_animal.adicionar_animal(adocao.animal.chip, adocao.animal.nome, adocao.animal.raca, adocao.animal.vacinas, "cachorro", adocao.animal.porte)
                    else:
                        self.__controlador_sistema.controlador_animal.adicionar_animal(adocao.animal.chip, adocao.animal.nome, adocao.animal.raca, adocao.animal.vacinas, "gato")
                    
                    self.__adocoes_DAO.remove(adocao.animal.chip)
                    
                    self.__tela_adocao.mostrar_mensagem(f"Adoção do animal com o chip {chip_animal} foi excluída.")
                
                else: 
                    self.__tela_adocao.mostrar_mensagem(f"Operação cancelada.")
                
                return

        
        self.__tela_adocao.mostrar_mensagem(f"Nenhuma adoção encontrada com o chip {chip_animal}.")
        return 

    def alterar_adocao(self):
        dados = self.__tela_adocao.pega_dados_alteracao()

        chip_animal = dados["chip_original"]

        adocao = self.buscar_adocao(chip_animal)

        if adocao is None:
            
            self.__tela_adocao.mostrar_mensagem("Adoção não encontrada.")
            return None

        cpf_adotante = dados["cpf"]

        if cpf_adotante is not None:
            adotante = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(cpf_adotante)
            if adotante is None:
                
                confirma = input("O novo adotante não existe, deseja cadastrar? (s/n) ")
                if confirma.lower() == "s":
                    
                    adotante = self.__controlador_sistema.controlador_pessoa.incluir_adotante()
                else:
                    self.__tela_adocao.mostrar_mensagem("Operação cancelada.")
                    return None
        else:
            adotante = None

        animal = self.__controlador_sistema.controlador_animal.buscar_animal(dados["animal"])

        if animal is not None:
            adocao.animal = animal

        if adotante is not None:
            adocao.adotante = adotante

        
        self.__tela_adocao.mostrar_mensagem("Adoção alterada com sucesso.")
        
        self.__tela_adocao.mostrar_adocao(adocao)

        return adocao

    def buscar_adocao(self, chip_animal = None):
        if chip_animal == None:
            chip_animal = self.__tela_adocao.seleciona_animal()

        for adocao in self.__adocoes_DAO.get_all():
            if adocao.animal.chip == chip_animal:
                return adocao

        return None


    def abrir_tela(self):
        lista_opcoes = {
            1: self.adotar,
            2: self.emitir_relatorio_adocoes,
            3: self.assinar_termo_adocao,
            4: self.alterar_adocao,
            5: self.excluir_adocao,
            6: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_adocao.mostrar_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
