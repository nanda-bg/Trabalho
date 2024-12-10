from DAO.dao import DAO
from entidade.cachorro import Cachorro

#cada entidade terá uma classe dessa, implementação bem simples.
class CachorroDAO(DAO):
    def __init__(self):
        super().__init__('cachorro.pkl')

    def add(self, cachorro: Cachorro):
        if((cachorro is not None) and isinstance(cachorro, Cachorro) and isinstance(cachorro.chip, int)):
            super().add(cachorro.chip, cachorro)

    def update(self, cachorro: Cachorro):
        if((cachorro is not None) and isinstance(cachorro, Cachorro) and isinstance(cachorro.chip, int)):
            super().update(cachorro.chip, cachorro)

    def get(self, key:int):
        if isinstance(key, int):
            return super().get(key)

    def remove(selfself, key:int):
        if(isinstance(key,int)):
            return super().remove(key)