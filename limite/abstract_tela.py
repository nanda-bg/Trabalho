from abc import ABC, abstractmethod

class AbstractTela(ABC):
    def __init__(self):
        super().__init__()

    def le_numero_inteiro(self, mensagem: str):
        while True:
            try:
                valor = int(input(mensagem))
                return valor
            except ValueError:
                print("Valor incorreto. Digite um número inteiro")    