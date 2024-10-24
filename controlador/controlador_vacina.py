from entidade.vacina import Vacina
from limite.tela_vacina import TelaVacina


class ControladorVacina:
    def __init__(self, controlador_sistema):
        self.__controlador_sistema = controlador_sistema
        self.__tela_vacina = TelaVacina()
        self.__vacinas = []


    def vacinas_disponiveis(self):
        vacinas = ['raiva', 'leptospirose', 'hepatite infecciosa', 'cinomose', 'parvovirose', 'coronavirose', 'traqueobronquite infecciosa', 'gripe canina', 'leishmaniose', 'calicivirose', 'rinotraqueite', 'panleucopenia', 'quadrivalente felina', 'trivalente felina', 'rabica', 'tosse dos canis', 'giardia', 'leucemia felina', 'rinotraqueite', 'calicivirose', 'panleucopenia', 'quadrivalente felina', 'trivalente felina', 'rabica', 'tosse dos canis', 'giardia', 'leucemia felina']

        for vacina in vacinas:
            vacina = Vacina(vacina)
            self.__vacinas.append(vacina)

        