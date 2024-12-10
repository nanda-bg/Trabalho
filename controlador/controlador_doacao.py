import datetime
from DAO.doacao_dao import DoacaoDAO
from entidade.doacao import Doacao
from entidade.vacina import Vacina
from view.tela_doacao import TelaDoacao


class ControladorDoacao:
    def __init__(self, controlador_sistema, root):
        self.__doacoes_DAO = DoacaoDAO()
        self.__root = root
        self.__controlador_sistema = controlador_sistema
        self.__controlador_pessoa = controlador_sistema.controlador_pessoa
        self.__controlador_animal = controlador_sistema.controlador_animal

    def doar(self):
        dados_doacao = self.__tela_doacao.pega_dados_doacao()
        print("cpf do doador", dados_doacao["cpf_doador"])
        if dados_doacao["cpf_doador"] is None:
            return
        
        doador = self.__controlador_pessoa.buscar_pessoa(dados_doacao["cpf_doador"])

        if doador is None:
            self.__tela_doacao.mostrar_mensagem("Doador não encontrado, faça o cadastro.")
            doador = self.__controlador_sistema.controlador_pessoa.incluir_doador()

        chip = dados_doacao["chip_animal"]
        nome = dados_doacao["nome_animal"]
        raca = dados_doacao["raca_animal"]
        vacinas = [Vacina(vacina) for vacina in dados_doacao["vacinas_animal"]]
        tipo_animal = dados_doacao["tipo_animal"]

        if tipo_animal == "cachorro":
            porte = dados_doacao["porte"]
            animal = self.__controlador_animal.adicionar_animal(chip, nome, raca, vacinas, tipo_animal, porte)

        else:
            animal = self.__controlador_animal.adicionar_animal(chip, nome, raca, vacinas, tipo_animal)

        motivo_doacao = dados_doacao["motivo_doacao"]

        doacao = Doacao(animal, doador, motivo_doacao)
        self.__doacoes_DAO.add(doacao)
        self.__tela_doacao.mostrar_mensagem("Doação realizada com sucesso.")
        return doacao

    def emitir_relatorio_doacoes(self):
        datas = self.__tela_doacao.pega_datas_relatorio()
        print("datas", datas)

        formato_data = "%Y-%m-%d"

        # Converter as datas de string para datetime
        inicio = datetime.datetime.strptime(datas["inicio"], formato_data)
        fim = datetime.datetime.strptime(datas["fim"], formato_data)

        doacoes = [doacao for doacao in self.__doacoes if inicio <= datetime.datetime.strptime(doacao.data, formato_data) <= fim]
        if len(doacoes) == 0:
            self.__tela_doacao.mostrar_mensagem(
                "Nenhuma doação realizada nesse período"
            )
            return
        
        self.__tela_doacao.mostrar_mensagem("-------- RELATÓRIO ---------")
        for doacao in doacoes:
            dados_doacao = {"nome_doador": doacao.doador.nome, "cpf": doacao.doador.cpf, "nome_animal": doacao.animal.nome, "chip": doacao.animal.chip, "data": doacao.data}
            self.__tela_doacao.mostrar_doacao(dados_doacao)

        return doacoes
    
    def excluir_doacao(self):
        chip_animal = self.__tela_doacao.pega_chip()

        for doacao in self.__doacoes:
            if doacao.animal.chip == chip_animal:
                self.__tela_doacao.mostrar_doacao(doacao)
                confirma = input("Tem certeza que deseja excluir a doação? (s/n) ")

                if confirma.lower() == "s":
                    self.__doacoes.remove(doacao)
                    self.__tela_doacao.mostrar_mensagem(f"Doação do animal com o chip {chip_animal} foi excluída.")

                else:
                    self.__tela_doacao.mostrar_mensagem("Operação cancelada.")

                return
        
        self.__tela_doacao.mostrar_mensagem(f"Nenhuma doação encontrada com o chip {chip_animal}.")
        return
    
    def alterar_doacao(self):
        dados = self.__tela_doacao.pega_dados_alteracao()

        chip_animal = dados["chip_original"]


        doacao = self.buscar_doacao(chip_animal)
        if doacao is None:
            self.__tela_doacao.mostrar_mensagem("Doação não encontrada.")
            return None

        cpf_doador = dados["cpf"]


        if cpf_doador is not None:
            doador = self.__controlador_sistema.controlador_pessoa.buscar_pessoa(cpf_doador)

            if doador is None:
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
        
        self.__tela_doacao.mostrar_mensagem("Doação alterada com sucesso.")
        return doacao


    def buscar_doacao(self, chip_animal):
        for doacao in self.__doacoes:
            if doacao.animal.chip == chip_animal:
                return doacao

        return None

    def abrir_tela(self):
        self.__tela_doacao = TelaDoacao(self.__root)

        lista_opcoes = {
            1: self.doar,
            2: self.emitir_relatorio_doacoes,
            3: self.excluir_doacao,
            4: self.alterar_doacao,
            5: self.retornar,
        }

        while True:
            opcao_escolhida = self.__tela_doacao.mostrar_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
