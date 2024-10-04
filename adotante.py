from pessoa import Pessoa

class Adotante(Pessoa):
    def __init__(self, cpf, nome, data_nascimento, endereco, tipo_habitacao, tamanho_habitacao, possui_animais):
        super().__init__(cpf, nome, data_nascimento, endereco)
            
        self.__tipo_habitacao = tipo_habitacao
        self.__tamanho_habitacao = tamanho_habitacao
        self.__possui_animais = possui_animais

    @property
    def tipo_habitacao(self):
        return self.__tipo_habitacao

    @tipo_habitacao.setter
    def tipo_habitacao(self, tipo_habitacao):
        if not isinstance(tipo_habitacao, str):
            raise ValueError('O tipo de habitação deve ser uma string')
        self.__tipo_habitacao = tipo_habitacao

    @property
    def possui_animais(self):
        return self.__possui_animais

    @possui_animais.setter
    def possui_animais(self, possui_animais):
        if not isinstance(possui_animais, bool):
            raise ValueError('O campo possui animais deve ser um booleano')
        self.__possui_animais = possui_animais

    @property
    def tamanho_habitacao(self):
        if not isinstance(self.__tamanho_habitacao, str):
            raise ValueError('O tamanho da habitação deve ser uma string')
        return self.__tamanho_habitacao    

    @tamanho_habitacao.setter
    def tamanho_habitacao(self, tamanho_habitacao):
        if not isinstance(tamanho_habitacao, str):
            raise ValueError('O tamanho da habitação deve ser uma string')
        self.__tamanho_habitacao = tamanho_habitacao