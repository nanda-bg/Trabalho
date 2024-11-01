from datetime import date


class Adocao:
    def __init__(self, animal, adotante, termo_assinado = False, data = date.today().isoformat()):
        self._animal = animal
        self._data = data
        self._adotante = adotante
        self._termo_assinado = termo_assinado

    @property
    def ong(self):
        return self._ong
    
    @property
    def data(self):
        return self._data

    @property
    def animal(self):
        return self._animal

    @property
    def adotante(self):
        return self._adotante

    @property
    def termo_assinado(self):
        return self._termo_assinado
    
    @termo_assinado.setter
    def termo_assinado(self, termo_assinado):
        if not isinstance(termo_assinado, bool):
            print("termo_assinado deve ser um booleano")
            return
        
        self._termo_assinado = termo_assinado

    def __str__(self):
        return f"Adoção do animal {self.animal.nome} realizada por {self.adotante.nome} em {self.data}"        