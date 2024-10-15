from datetime import datetime
from exception.chipInvalidoException import ChipInvalidoException
from exception.cpfInvalidoException import CPFInvalidoException
from exception.dataFinalInvalidaException import DataFinalInvalida
from limite.abstract_tela import AbstractTela
import re


class TelaAdocao(AbstractTela):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA ADOCAO ---------")
        print("Escolha uma opcao")
        print("1 - Adotar")
        print("2 - Emitir relatório de adoções")
        print("3 - Assinar termo de adoção")
        print("0 - Voltar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 0])
    
    def mostrar_mensagem(self, msg):
        print(msg)

    def mostra_adocao(self, adocao):
        print(f"Nome do adotante: {adocao.adotante.nome}")
        print(f"CPF do adotante: {adocao.adotante.cpf}")

        print(f"Nome do animal: {adocao.animal.nome}")
        print(f"Chip do animal: {adocao.animal.chip}")

        print(f"Data da Adoção: {adocao.data}")    

    def pega_dados_adocao(self):
        print("-------- DADOS ADOCAO ----------")
        
        cpf_adotante = self.valida_cpf()
        chip_animal = self.valida_chip()

        return {"cpf_adotante": cpf_adotante, "chip_animal": chip_animal}
    
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
    
    def pega_chip(self):
        chip = self.valida_chip()

        return chip

    def valida_cpf(self):
        while True:
            try:
                cpf = input("CPF: ")

                # Verifica se o CPF tem apenas números (11 dígitos)
                if re.match(r'^\d{11}$', cpf):
                    # Formata o CPF para NNN.NNN.NNN-NN
                    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
                    return cpf_formatado
                
                # Verifica se o CPF já está no formato NNN.NNN.NNN-NN
                elif re.match(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$', cpf):
                    return cpf
                
                else:
                    raise CPFInvalidoException()

            except CPFInvalidoException as e:
                self.mostrar_mensagem(e)       

    def valida_chip(self):
        while True:
            try:
                chip = input("Chip do animal (7 dígitos): ")

                # Verifica se o chip tem apenas números (7 dígitos)
                if not re.match(r'^\d{7}$', chip):
                    raise ChipInvalidoException()
                
                return chip
            
            except ChipInvalidoException as e:
                self.mostrar_mensagem(e)  
                               