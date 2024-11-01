from entidade.adotante import Adotante
from entidade.adocao import Adocao
from entidade.animal import Animal
from entidade.cachorro import Cachorro
from limite.tela_adocao import TelaAdocao


class ControladorAdocao:
    def __init__(self, controlador_sistema):
        self.__adocoes = []
        self.__tela_adocao = TelaAdocao()
        self.__controlador_sistema = controlador_sistema

    def emitir_relatorio_adocoes(self):
        datas = self.__tela_adocao.pega_datas_relatorio()

        inicio = datas["inicio"]
        fim = datas["fim"]

        adocoes = [adocao for adocao in self.__adocoes if inicio <= adocao.data <= fim]
        if len(adocoes) == 0:
            self.__tela_adocao.mostrar_mensagem(
                "Nenhuma adoção realizada nesse período"
            )
            return

        self.__tela_adocao.mostrar_mensagem("-------- Relátorio ---------")
        for adocao in adocoes:
            self.__tela_adocao.mostra_adocao(adocao)

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

        if assinar == "s":
            adocao.termo_assinado = True
            self.__tela_adocao.mostrar_mensagem("Termo de adoção assinado com sucesso")
            return

        self.__tela_adocao.mostrar_mensagem("Termo de adoção não foi assinado")
        return

    def abrir_tela(self):
        lista_opcoes = {
            1: self.adotar,
            2: self.emitir_relatorio_adocoes,
            3: self.assinar_termo_adocao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_adocao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
