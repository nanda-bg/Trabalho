from abc import ABC, abstractmethod
import re

from entidade.vacina import Vacina
from exception.chipInvalidoException import ChipInvalidoException
from exception.nomeInvalidoException import NomeInvalidoException
from exception.raca_invalida_exception import RacaInvalidaException
from exception.vacina_invalida_exception import VacinaInvalidaException

# from limite.tela_vacina import TelaVacina


class AbstractTelaVacina(ABC):
    def __init__(self):
        super().__init__()

    def incluir_vacina(self):
        # add dicionario de vacinas
        vacinas = {
            1: Vacina("raiva"),
            2: Vacina("leptospirose"),
            3: Vacina("hepatite infecciosa"),
            4: Vacina("cinomose"),
            5: Vacina("parvovirose"),
            6: Vacina("coronavirose"),
        }
        print()
        print("-------- TELA VACINAS ----------")
        print("Escolha uma opção")
        print("1 - Incluir vacina de raiva")
        print("2 - Incluir vacina de leptospirose")
        print("3 - Incluir vacina de hepatite infecciosa")
        print("4 - Incluir vacina de cinomose")
        print("5 - Incluir vacina de parvovirose")
        print("6 - Incluir vacina de coronavirose")
        print("0 - Retornar")

        print()

        vacina = self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 6, 0])
        return vacinas[vacina]

    def valida_vacinas(self):
        while True:
            try:
                vacinas = []
                tem_vacina = input("O animal já foi vacinado?(s/n) ")
                if tem_vacina != "s" and tem_vacina != "n":
                    print("Insira um valor válido. (s/n)")
                elif tem_vacina == "n":
                    vacinas = []
                elif tem_vacina == "s":
                    # looping to add multiple vacinas
                    while True:
                        vacina = self.incluir_vacina()
                        vacinas.append(vacina)
                        if (
                            self.le_numero_inteiro(
                                "Deseja adicionar mais uma vacina? (1 - Sim, 0 - Não): ",
                                [0, 1],
                            )
                            == 0
                        ):
                            break

                for vacina in vacinas:
                    if not isinstance(vacina, Vacina):
                        raise VacinaInvalidaException

                return vacinas

            except VacinaInvalidaException as e:
                self.mostrar_mensagem(e)
