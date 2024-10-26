from entidade.vacina import Vacina
from limite.tela_vacina import TelaVacina


class ControladorVacina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_vacina = TelaVacina()
        self.__vacinas = []


    def vacinas_disponiveis(self):
        vacinas = ['raiva', 'leptospirose', 'hepatite infecciosa', 'cinomose', 'parvovirose', 'coronavirose']

        for vacina in vacinas:
            vacina = Vacina(vacina)
            self.__vacinas.append(vacina)

    def abrir_tela(self):
        lista_opcoes = {1: "raiva", 2: "leptospirose", 3: "hepatite infecciosa", 
                        4: "cinomose", 5: "parvovirose", 6: "coronavirose", 0: self.retornar()}

        while True:
            opcao_escolhida = self.__tela_vacina.tela_opcoes()
            if opcao_escolhida == 0:
                self.retornar()
            else:
                self.add_vacina(chip_animal, vacina_escolhida) 
                

    def add_vacina(vacina):
        chip_animal = self.__tela_vacina.pega_dados_vacina()
        animal = self.__controlador_sistema.controlador_animal.buscar_animal(dados_vacina["chip_animal"])
        animal.vacinas.append(vacina)

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()
        