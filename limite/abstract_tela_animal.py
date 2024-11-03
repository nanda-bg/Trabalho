from abc import ABC
import re

from exception.chipInvalidoException import ChipInvalidoException
from exception.nomeInvalidoException import NomeInvalidoException
from exception.porteInvalidoException import PorteInvalidoException
from exception.raca_invalida_exception import RacaInvalidaException
from exception.tipoAnimalInvalidoException import TipoAnimalInvalidoException


class AbstractTelaAnimal(ABC):
    def __init__(self):
        super().__init__()

    def valida_chip(self):
        while True:
            try:
                chip = input("Chip do animal (7 dígitos): ")

                # Verifica se o chip tem apenas números (7 dígitos)
                if not re.match(r"^\d{7}$", chip):
                    raise ChipInvalidoException()

                return chip

            except ChipInvalidoException as e:
                self.mostrar_mensagem(e)

    def valida_nome_animal(self):
        while True:
            try:
                nome = input("Nome do animal: ")
                if len(nome.strip()) < 2:
                    raise NomeInvalidoException()

                return nome

            except NomeInvalidoException as e:
                self.mostrar_mensagem(e)

    def valida_raca_animal(self):
        while True:
            try:
                raca = input("Raça: ")
                if raca.isalpha() == False:
                    raise RacaInvalidaException()
                if len(raca.strip()) < 3:
                    raise RacaInvalidaException()

                return raca

            except RacaInvalidaException as e:
                self.mostrar_mensagem(e)

    def valida_tipo_animal(self):
        while True:
            try:
                tipo_animal = input("Tipo de Animal (cachorro/gato): ").lower()
                if tipo_animal not in ['cachorro', 'gato']:
                    raise TipoAnimalInvalidoException()
                
                return tipo_animal
            except TipoAnimalInvalidoException as e:
                self.mostrar_mensagem(e)            

    def valida_porte(self):
        while True:
            try:
                porte = input("Porte (pequeno/médio/grande): ").lower()
                if porte not in ['pequeno', 'médio', 'grande']:
                    raise PorteInvalidoException()

                return porte
            except PorteInvalidoException as e:
                self.mostrar_mensagem(e)