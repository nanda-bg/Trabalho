from controlador.controlador_adocao import ControladorAdocao
from controlador.controlador_animal import ControladorAnimal
from controlador.controlador_doacao import ControladorDoacao
from controlador.controlador_pessoa import ControladorPessoa
from controlador.controlador_vacina import ControladorVacina
from limite.tela_sistema import TelaSistema

class SistemaPessoas():
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_vacina = ControladorVacina(self)
        self.__tela_sistema = TelaSistema()


    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa
    
    @property
    def controlador_animal(self):
        return self.__controlador_animal
    
    @property
    def controlador_adocao(self):
        return self.__controlador_adocao
    
    @property
    def controlador_vacina(self):
        return self.__controlador_vacina


    def inicializa_sistema(self):
        self.abrir_tela_inicial()

    def ir_para_pessoas(self):
        self.__controlador_pessoa.abrir_tela()

    def ir_para_animais(self):
        self.__controlador_animal.abrir_tela()

    def ir_para_adocao(self):
        self.__controlador_adocao.abrir_tela()

    def ir_para_doacao(self):
        self.__controlador_doacao.abrir_tela()    

    def ir_para_vacina(self):
        self.__controlador_vacina.abrir_tela()

    def encerra_sistema(self):
        exit(0)

    def abrir_tela_inicial(self):
        lista_opcoes = {1: self.ir_para_pessoas, 2: self.ir_para_animais, 3: self.ir_para_adocao, 4: self.ir_para_doacao, 5: self.ir_para_vacina, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
