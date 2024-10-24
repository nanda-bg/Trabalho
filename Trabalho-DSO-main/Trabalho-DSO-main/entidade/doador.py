from entidade.pessoa import Pessoa


class Doador(Pessoa):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(cpf, nome, data_nascimento, endereco)
