from DAO.dao import DAO
from entidade.adocao import Adocao


class AdocaoDAO(DAO):
    def __init__(self):
        super().__init__('adocao.pkl')

    def add(self, adocao: Adocao):
        if((adocao is not None) and isinstance(adocao, Adocao) and isinstance(adocao.animal.chip, int)):
            super().add(adocao.animal.chip, adocao)

    def update(self, adocao: Adocao):
        if((adocao is not None) and isinstance(adocao, Adocao) and isinstance(adocao.animal.chip, int)):
            super().update(adocao.animal.chip, adocao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key,int)):
            return super().remove(key)