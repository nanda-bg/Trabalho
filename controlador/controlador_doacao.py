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

    def abrir_tela(self):
        lista_opcoes = {
            1: self.doar,
            2: self.emitir_relatorio_doacoes,
            0: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
