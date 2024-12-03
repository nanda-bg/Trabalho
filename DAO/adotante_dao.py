from DAO.dao import DAO
from entidade.adotante import Adotante

#cada entidade terá uma classe dessa, implementação bem simples.
class AdotanteDAO(DAO):
    def __init__(self):
        super().__init__('adotante.pkl')

    def add(self, adotante: Adotante):
        if((adotante is not None) and isinstance(adotante, Adotante) and isinstance(adotante.cpf, str)):
            super().add(adotante.cpf, adotante)

    def update(self, adotante: Adotante):
        if((adotante is not None) and isinstance(adotante, Adotante) and isinstance(adotante.cpf, str)):
            super().update(adotante.cpf, adotante)

    def get(self, key:str):
        if isinstance(key, str):
            return super().get(key)

    def remove(selfself, key:str):
        if(isinstance(key,str)):
            return super().remove(key)