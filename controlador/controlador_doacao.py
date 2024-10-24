from entidade.doação import Doacao
from limite.tela_doacao import TelaDoacao


class ControladorDoacao():
    def __init__(self, controlador_sistema):
        self.__doacoes = []
        self.__tela_doacao = TelaDoacao()
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pessoa = controlador_sistema.controlador_pessoa
        self.__controlador_animal = controlador_sistema.controlador_animal
        
    def doar(self):
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        doador = self.__controlador_pessoa.buscar_pessoa(dados_doacao["cpf_doador"])

        chip = dados_doacao["chip_animal"]
        nome = dados_doacao["nome_animal"]
        raca = dados_doacao["raca_animal"]
        vacinas = dados_doacao["vacinas_animal"]

        animal = self.__controlador_animal.adicionar_animal(chip, nome, raca, vacinas)

        motivo_doacao = dados_doacao["motivo_doacao"]

        doacao = Doacao(animal, doador, motivo_doacao)
        self.__doacoes.append(doacao)
        return doacao
    
    def emitir_relatorio_doacoes(self):
        datas = self.__tela_doacao.pega_datas_relatorio()

        inicio = datas["inicio"]
        fim = datas["fim"]

        doacoes = [doacao for doacao in self.__doacoes if inicio <= doacao.data <= fim]
        if len(doacoes) == 0:
            self.__tela_doacao.mostrar_mensagem("Nenhuma adoção realizada nesse período")
            return
        
        self.__tela_doacao.mostrar_mensagem("-------- Relátorio ---------")
        for doacao in doacoes:
            self.__tela_doacao.mostra_doacao(doacao)

        return doacoes

    def mostra_doacao(self, doacao):
        print(f"Nome do doador: {doacao.doador.nome}")
        print(f"CPF do doador: {doacao.doador.cpf}")

        print(f"Nome do animal: {doacao.animal.nome}")
        print(f"Chip do animal: {doacao.animal.chip}")

        print(f"Data da Doação: {doacao.data}")    

    def abrir_tela(self):
        lista_opcoes = {1: self.doar, 2: self.emitir_relatorio_doacoes, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_doacao.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()