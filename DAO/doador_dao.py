from DAO.dao import DAO
from entidade.doador import Doador

#cada entidade terá uma classe dessa, implementação bem simples.
class DoadorDAO(DAO):
    def __init__(self):
        super().__init__('doador.pkl')

    def add(self, doador: Doador):
        if((doador is not None) and isinstance(doador, Doador) and isinstance(doador.cpf, str)):
            super().add(doador.cpf, doador)

    def update(self, doador: Doador):
        if((doador is not None) and isinstance(doador, Doador) and isinstance(doador.cpf, str)):
            super().update(doador.cpf, doador)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key, str)):
            return super().remove(key)