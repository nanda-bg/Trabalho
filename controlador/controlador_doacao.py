import datetime
from entidade.doacao import Doacao
from limite.tela_doacao import TelaDoacao


class ControladorDoacao:
    def __init__(self, controlador_sistema):
        self.__doacoes = []
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pessoa = controlador_sistema.controlador_pessoa
        self.__controlador_animal = controlador_sistema.controlador_animal

    def doar(self):
        print()
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        doador = self.__controlador_pessoa.buscar_pessoa(dados_doacao["cpf_doador"])

        if doador is None:
            print()
            self.__tela_doacao.mostrar_mensagem("Doador não encontrado, cadastre o doador:")
            doador = self.__controlador_sistema.controlador_pessoa.incluir_doador()

        chip = dados_doacao["chip_animal"]
        nome = dados_doacao["nome_animal"]
        raca = dados_doacao["raca_animal"]
        vacinas = dados_doacao["vacinas_animal"]
        tipo_animal = dados_doacao["tipo_animal"]

        if tipo_animal == "cachorro":
            porte = dados_doacao["porte"]
            animal = self.__controlador_animal.adicionar_animal(chip, nome, raca, vacinas, tipo_animal, porte)

        else:
            animal = self.__controlador_animal.adicionar_animal(chip, nome, raca, vacinas, tipo_animal)

        motivo_doacao = dados_doacao["motivo_doacao"]

        doacao = Doacao(animal, doador, motivo_doacao)
        self.__doacoes.append(doacao)
        print()
        self.__tela_doacao.mostrar_mensagem("Doação realizada com sucesso.")
        return doacao

    def emitir_relatorio_doacoes(self):
        print()
        datas = self.__tela_doacao.pega_datas_relatorio()

        formato_data = "%Y-%m-%d"

        # Converter as datas de string para datetime
        inicio = datetime.datetime.strptime(datas["inicio"], formato_data)
        fim = datetime.datetime.strptime(datas["fim"], formato_data)

        doacoes = [doacao for doacao in self.__doacoes if inicio <= datetime.datetime.strptime(doacao.data, formato_data) <= fim]
        if len(doacoes) == 0:
            print()
            self.__tela_doacao.mostrar_mensagem(
                "Nenhuma doação realizada nesse período"
            )
            return
        
        print()
        self.__tela_doacao.mostrar_mensagem("-------- RELATÓRIO ---------")
        for doacao in doacoes:
            self.__tela_doacao.mostrar_doacao(doacao)
            print()

        return doacoes
    
    def excluir_doacao(self):
        chip_animal = self.__tela_doacao.pega_chip()

        for doacao in self.__doacoes:
            if doacao.animal.chip == chip_animal:
                print()
                self.__tela_doacao.mostrar_doacao(doacao)
                print()
                confirma = input("Tem certeza que deseja excluir a doação? (s/n) ")

                if confirma.lower() == "s":
                    self.__doacoes.remove(doacao)
                    print()
                    self.__tela_doacao.mostrar_mensagem(f"Doação do animal com o chip {chip_animal} foi excluída.")

                else:
                    self.__tela_doacao.mostrar_mensagem("Operação cancelada.")

                return

        print()
        self.__tela_doacao.mostrar_mensagem(f"Nenhuma doação encontrada com o chip {chip_animal}.")
        return
    
    def alterar_doacao(self):
        dados = self.__tela_doacao.pega_dados_alteracao()

        chip_animal = dados["chip_original"]


        doacao = self.buscar_doacao(chip_animal)
        if doacao is None:
            print()
            self.__tela_doacao.mostrar_mensagem("Doação não encontrada.")
            return None

        cpf_doador = dados["cpf"]


        if cpf_doador is not None:
            doador = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(cpf_doador)

            if doador is None:
                print()
                confirma = input("O novo doador não existe, deseja cadastrar? (s/n) ")

                if confirma.lower() == "s":
                    doador = self.__controlador_sistema.controlador_pessoa.incluir_doador()

                else:
                    self.__tela_doacao.mostrar_mensagem("Operação cancelada.")
                    return None
        else:
            doador = None

        novo_animal = dados["animal"]    

        if novo_animal is not None:
            novo_animal = self.__controlador_sistema.controlador_animal.buscar_animal(novo_animal)

            if novo_animal is None:
                print()
                confirma = input("O novo animal não existe, deseja cadastrar? (s/n) ")

                if confirma.lower() == "s":
                    novo_animal = self.__controlador_sistema.controlador_animal.adicionar_animal()

                else:
                    self.__tela_doacao.mostrar_mensagem("Operação cancelada.")

                    return None
            
            doacao.animal = novo_animal

        if doador is not None:
            doacao.doador = doador

        novo_motivo = dados["motivo_doacao"]
        if novo_motivo is not None:
            doacao.motivo_doacao = novo_motivo

        print()
        self.__tela_doacao.mostrar_mensagem("Doação alterada com sucesso.")
        return doacao


    def buscar_doacao(self, chip_animal):
        for doacao in self.__doacoes:
            if doacao.animal.chip == chip_animal:
                return doacao

        return None

    def abrir_tela(self):
        lista_opcoes = {
            1: self.doar,
            2: self.emitir_relatorio_doacoes,
            3: self.excluir_doacao,
            4: self.alterar_doacao,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
