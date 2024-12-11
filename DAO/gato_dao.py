from DAO.dao import DAO
from entidade.gato import Gato


class GatoDAO(DAO):
    def __init__(self):
        super().__init__('gato.pkl')

    def add(self, gato: Gato):
        if((gato is not None) and isinstance(gato, Gato) and isinstance(gato.chip, int)):
            super().add(gato.chip, gato)

    def update(self, gato: Gato):
        if((gato is not None) and isinstance(gato, Gato) and isinstance(gato.chip, int)):
            super().update(gato.chip, gato)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key,int)):
            return super().remove(key)