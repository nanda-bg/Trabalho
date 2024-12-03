from controlador.controlador_adocao import ControladorAdocao
from controlador.controlador_animal import ControladorAnimal
from controlador.controlador_doacao import ControladorDoacao
from controlador.controlador_pessoa import ControladorPessoa
from controlador.controlador_vacina import ControladorVacina
# from limite.tela_sistema import TelaSistema
from view.tela_sistema import TelaSistema


<<<<<<< HEAD
class SistemaPessoas:
    def __init__(self, root):
        self.__controlador_pessoa = ControladorPessoa(self, root)
=======
class Sistema:
    def __init__(self):
        self.__controlador_pessoa = ControladorPessoa(self)
>>>>>>> fe247162b184adc695bdcbc1f718b2acf5d14169
        self.__controlador_adocao = ControladorAdocao(self)
        self.__controlador_animal = ControladorAnimal(self)
        self.__controlador_doacao = ControladorDoacao(self)
        self.__controlador_vacina = ControladorVacina(self)
        self.__tela_sistema = TelaSistema(root)
        self.__root = root

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

    @property
    def controlador_doacao(self):
        return self.__controlador_doacao

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

    def ir_para_vacinas(self):
        self.__controlador_vacina.abrir_tela()

    def encerra_sistema(self):
        exit(0)

    def abrir_tela_inicial(self):
        lista_opcoes = {
            1: self.ir_para_pessoas,
            2: self.ir_para_animais,
            3: self.ir_para_adocao,
            4: self.ir_para_doacao,
            5: self.ir_para_vacinas,
            0: self.encerra_sistema,
        }

        while True:
            opcao_escolhida = self.__tela_sistema.mostra_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()
