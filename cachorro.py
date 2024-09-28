from animal import Animal

class Cachorro(Animal):
    def __init__(self, chip, nome, raca, porte):
        super().__init__(chip, nome, raca)

        if not isinstance(porte, str):
            raise ValueError('O porte deve ser uma string.')
        
        self.__porte = porte

    @property
    def porte(self):
        return self.__porte

    @porte.setter
    def porte(self, porte):
        if not isinstance(porte, str):
            raise ValueError('O porte deve ser uma string.')
        
        self.__porte = porte