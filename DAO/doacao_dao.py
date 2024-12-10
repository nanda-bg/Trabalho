from DAO.dao import DAO
from entidade.doacao import Doacao

#cada entidade terá uma classe dessa, implementação bem simples.
class DoacaoDAO(DAO):
    def __init__(self):
        super().__init__('doacao.pkl')

    def add(self, doacao: Doacao):
        if((doacao is not None) and isinstance(doacao, Doacao) and isinstance(doacao.animal.chip, int)):
            super().add(doacao.animal.chip, doacao)

    def update(self, doacao: Doacao):
        if((doacao is not None) and isinstance(doacao, Doacao) and isinstance(doacao.animal.chip, int)):
            super().update(doacao.animal.chip, doacao)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key,int)):
            return super().remove(key)