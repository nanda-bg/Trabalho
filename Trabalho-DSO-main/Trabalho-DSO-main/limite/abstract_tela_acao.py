from abc import ABC
from datetime import datetime

from exception.dataFinalInvalidaException import DataFinalInvalida


class AbstractTelaAcao(ABC):
    def __init__(self):
        super().__init__()

    def pega_datas_relatorio(self):
        while True:
            try:
                inicio = input("Data de início (aaaa-mm-dd): ")
                datetime.strptime(inicio, "%Y-%m-%d")
                break 
            except ValueError:
                self.mostrar_mensagem("A data deve estar no formato aaaa-mm-dd. Tente novamente.")
        
        while True:
            try:
                fim = input("Data de fim (aaaa-mm-dd): ")
                datetime.strptime(fim, "%Y-%m-%d")
                if fim > inicio:
                    break
                
                raise DataFinalInvalida()

            except ValueError:
                self.mostrar_mensagem("A data deve estar no formato aaaa-mm-dd. Tente novamente.")

            except DataFinalInvalida as e:
                self.mostrar_mensagem(e)    
        
        return {"inicio": inicio, "fim": fim}