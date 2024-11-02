from datetime import date


class Adocao:
    def __init__(self, animal, adotante, termo_assinado = False, data = date.today().isoformat()):
        self.__animal = animal
        self.__data = data
        self.__adotante = adotante
        self.__termo_assinado = termo_assinado

    @property
    def ong(self):
        return self.__ong
    
    @property
    def data(self):
        return self.__data

    @property
    def animal(self):
        return self.__animal

    @property
    def adotante(self):
        return self.__adotante

    @property
    def termo_assinado(self):
        return self.__termo_assinado
    
    @termo_assinado.setter
    def termo_assinado(self, termo_assinado):
        if not isinstance(termo_assinado, bool):
            print("termo_assinado deve ser um booleano")
            return
        
        self.__termo_assinado = termo_assinado

    def __str__(self):
        return f"Adoção do animal {self.animal.nome} realizada por {self.adotante.nome} em {self.data}"        