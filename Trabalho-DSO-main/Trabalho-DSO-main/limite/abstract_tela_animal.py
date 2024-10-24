from abc import ABC, abstractmethod
import re

from entidade.vacina import Vacina
from exception.chipInvalidoException import ChipInvalidoException
from exception.nomeInvalidoException import NomeInvalidoException
from exception.raca_invalida_exception import RacaInvalidaException
from exception.vacina_invalida_exception import VacinaInvalidaException

class AbstractTelaAnimal(ABC):
    def __init__(self):
        super().__init__()
        
    def valida_chip(self):
        while True:
            try:
                chip = input("Chip do animal (7 dígitos): ")

                # Verifica se o chip tem apenas números (7 dígitos)
                if not re.match(r'^\d{7}$', chip):
                    raise ChipInvalidoException()
                
                return chip
            
            except ChipInvalidoException as e:
                self.mostrar_mensagem(e)          

    def valida_nome_animal(self):
        while True:
            try:
                nome = input("Nome: ")
                if len(nome.strip()) < 3:
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
                   
    def valida_vacinas(self):
        while True:
            try:
                vacinas = input("Vacinas do animal (separadas por vírgula): ").split(',')
                for vacina in vacinas:
                    if not isinstance(vacina, Vacina):
                        raise VacinaInvalidaException   
                          
                return vacinas
            
            except VacinaInvalidaException as e:
                self.mostrar_mensagem(e)                                             