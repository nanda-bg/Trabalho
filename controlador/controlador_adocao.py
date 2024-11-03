import datetime
from entidade.adotante import Adotante
from entidade.adocao import Adocao
from entidade.cachorro import Cachorro
from limite.tela_adocao import TelaAdocao


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    def emitir_relatorio_adocoes(self):
        print()
        datas = self.__tela_adocao.pega_datas_relatorio()
        formato_data = "%Y-%m-%d"

        # Converter as datas de string para datetime
        inicio = datetime.datetime.strptime(datas["inicio"], formato_data)
        fim = datetime.datetime.strptime(datas["fim"], formato_data)

        adocoes = [adocao for adocao in self.__adocoes if inicio <= datetime.datetime.strptime(adocao.data, formato_data) <= fim]
        if len(adocoes) == 0:
            self.__tela_adocao.mostrar_mensagem(
                "Nenhuma adoção realizada nesse período"
            )
            return

        print()
        self.__tela_adocao.mostrar_mensagem("-------- Relátorio ---------")
        for adocao in adocoes:
            self.__tela_adocao.mostrar_adocao(adocao)

        return adocoes

    def avaliar_adocao(self, animal, adotante):
        if isinstance(animal, Cachorro):
            if animal.porte == "grande" and (
                adotante.tipo_habitacao == "apartamento"
                and adotante.tamanho_habitacao == "pequeno"
            ):
                return False

        if not animal.tem_vacinas_basicas():
            return False

        return True

    def adotar(self):
        print()
        dados_adocao = self.__tela_adocao.pega_dados_adocao()

        cpf = dados_adocao["cpf_adotante"]
        chip = dados_adocao["chip_animal"]

        adotante = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(cpf)

        if adotante != None and not isinstance(adotante, Adotante):
            self.__tela_adocao.mostrar_mensagem("CPF já cadastrado para um doador")
            self.__tela_adocao.mostrar_mensagem("Doadores não podem adotar animais")
            return

        elif adotante == None:
            self.__tela_adocao.mostrar_mensagem("Adotante não encontrado")
            cadastrar = input("Deseja cadastrar um novo adotante? (s/n) ")

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
            print()
            self.__tela_adocao.mostrar_mensagem(
                f"Adoção do animal {animal.nome} aprovada."
            )

            adocao = Adocao(animal, adotante)

            if adocao.termo_assinado == False:
                assinar_termo = input("Deseja assinar o termo de adoção? (s/n)")

            if assinar_termo == "s" or adocao.termo_assinado:
                self.assinar_termo_adocao(adocao)
                adocao.termo_assinado = True

                self.__adocoes.append(adocao)

                self.__controlador_sistema.controlador_animal.remover_animal(animal)

            else:
                self.__tela_adocao.mostrar_mensagem(
                    f"Processo de adoção não foi concluído."
                )
                return

            self.__tela_adocao.mostrar_mensagem(f"Adoção realizada com sucesso.")

        else:
            self.__tela_adocao.mostrar_mensagem(f"Adoção não aprovada.")

    def buscar_adocao(self):
        chip = self.__tela_adocao.pega_chip()

        for adocao in self.__adocoes:
            if adocao.animal.chip == chip:
                return adocao

        return None

    def assinar_termo_adocao(self, adocao=None):
        if adocao == None:
            adocao = self.buscar_adocao()

            if adocao == None:
                self.__tela_adocao.mostrar_mensagem("Adoção não encontrada")
                return

        print()
        self.__tela_adocao.mostrar_mensagem(
            f"Eu, {adocao.adotante.nome}, portador do CPF {adocao.adotante.cpf},"
        )
        self.__tela_adocao.mostrar_mensagem(
            f"declaro que irei adotar o animal {adocao.animal.nome},"
        )
        self.__tela_adocao.mostrar_mensagem(f"portador do chip {adocao.animal.chip},")
        self.__tela_adocao.mostrar_mensagem(
            f"e me comprometo a cuidar dele com responsabilidade, amor e carinho."
        )
        print()
        assinar = input("Você concorda com o termo acima? (s/n) ")
        print()

        if assinar == "s":
            adocao.termo_assinado = True
            self.__tela_adocao.mostrar_mensagem("Termo de adoção assinado com sucesso")
            return

        self.__tela_adocao.mostrar_mensagem("Termo de adoção não foi assinado")
        return


    def excluir_adocao(self):
        chip_animal = self.__tela_adocao.pega_chip()

        for adocao in self.__adocoes:
            if adocao.animal.chip == chip_animal:
                print()
                self.__tela_adocao.mostrar_adocao(adocao)
                print()
                confirma = input("Tem certeza que deseja excluir a adoção? (s/n) ")

                if confirma.lower() == "s":
                    if hasattr(adocao.animal, "porte"):
                        self.__controlador_sistema.controlador_animal.adicionar_animal(adocao.animal.chip, adocao.animal.nome, adocao.animal.raca, adocao.animal.vacinas, "cachorro", adocao.animal.porte)
                    else:
                        self.__controlador_sistema.controlador_animal.adicionar_animal(adocao.animal.chip, adocao.animal.nome, adocao.animal.raca, adocao.animal.vacinas, "gato")
                    
                    self.__adocoes.remove(adocao)
                    print()
                    self.__tela_adocao.mostrar_mensagem(f"Adoção do animal com o chip {chip_animal} foi excluída.")
                
                else: 
                    self.__tela_adocao.mostrar_mensagem(f"Operação cancelada.")
                
                return

        print()
        self.__tela_adocao.mostrar_mensagem(f"Nenhuma adoção encontrada com o chip {chip_animal}.")
        return 

    def alterar_adocao(self):
        dados = self.__tela_adocao.pega_dados_alteracao()

        chip_animal = dados["chip_original"]

        adocao = self.buscar_adocao(chip_animal)

        if adocao is None:
            print()
            self.__tela_adocao.mostrar_mensagem("Adoção não encontrada.")
            return None

        cpf_adotante = dados["cpf"]

        if cpf_adotante is not None:
            adotante = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(cpf_adotante)
            if adotante is None:
                print()
                confirma = input("O novo adotante não existe, deseja cadastrar? (s/n) ")
                if confirma.lower() == "s":
                    print()
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

        print()
        self.__tela_adocao.mostrar_mensagem("Adoção alterada com sucesso.")
        print()
        self.__tela_adocao.mostrar_adocao(adocao)

        return adocao

    def buscar_adocao(self, chip_animal):
        for adocao in self.__adocoes:
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
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_adocao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
