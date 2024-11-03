from entidade.animal import Animal

class Cachorro(Animal):
    def __init__(self, chip, nome, raca, porte, vacinas = None):
        super().__init__(chip, nome, raca, vacinas)

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

    def __str__(self):
        return f'Tipo: Cachorro, Chip: {self.chip}, Nome: {self.nome}, Raça: {self.raca}, Porte: {self.__porte}'        