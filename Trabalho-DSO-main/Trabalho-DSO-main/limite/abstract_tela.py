from abc import ABC, abstractmethod

class AbstractTela(ABC):
    def __init__(self):
        super().__init__()

    def le_numero_inteiro(self, mensagem: str, valores_validos: list):
        while True:
            try:
                valor = int(input(mensagem))

                if valor not in valores_validos:
                    raise ValueError
                
                return valor
            
            except ValueError:
                print(f"Valor incorreto. Digite um número inteiro da lista: {valores_validos}")    