from exception.chipInvalidoException import ChipInvalidoException
import re

from limite.abstract_tela import AbstractTela
from limite.abstract_tela_acao import AbstractTelaAcao
from limite.abstract_tela_animal import AbstractTelaAnimal
from limite.abstract_tela_pessoa import AbstractTelaPessoa


class TelaAdocao(AbstractTela, AbstractTelaPessoa, AbstractTelaAnimal, AbstractTelaAcao):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA ADOÇÃO ---------")
        print("Escolha uma opção:")
        print("1 - Adotar")
        print("2 - Emitir relatório de adoções")
        print("3 - Assinar termo de adoção")
        print("4 - Alterar adoção")
        print("5 - Excluir adoção")
        print("0 - Voltar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 5, 0])
    
    def mostrar_mensagem(self, msg):
        print(msg)

    def mostrar_adocao(self, adocao):
        print(f"Nome do adotante: {adocao.adotante.nome}")
        print(f"CPF do adotante: {adocao.adotante.cpf}")

        print(f"Nome do animal: {adocao.animal.nome}")
        print(f"Chip do animal: {adocao.animal.chip}")

        print(f"Data da adoção: {adocao.data}")    

    def pega_dados_adocao(self):
        print("-------- DADOS ADOÇÃO ----------")
        
        cpf_adotante = self.valida_cpf()
        chip_animal = self.valida_chip()

        return {"cpf_adotante": cpf_adotante, "chip_animal": chip_animal}
    
    def pega_chip(self):
        chip = self.valida_chip()

        return chip

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


    def pega_dados_alteracao(self):
        chip_original = self.valida_chip()

        self.mostrar_mensagem("Digite os novos dados da adoção. Para manter os dados antigos, apenas aperte Enter.")

        cpf = input("Novo adotante (CPF): ")
        
        if cpf == "":
            cpf = None

        else:    
            cpf_esta_correto = self.validar_numeros_cpf(cpf)

            while not cpf_esta_correto:
                self.mostrar_mensagem("CPF inválido, tente novamente")
                cpf = input("Novo adotante (CPF): ")
                if cpf == "":
                    cpf = None
                    break
                cpf_esta_correto = self.validar_numeros_cpf

        animal = input("Novo animal (Chip): ")
        if animal == "":
            animal = None
        else:
            while not ( len(animal.strip()) == 7 and animal.isdigit() ):
                self.mostrar_mensagem("O chip deve ter 7 dígitos numéricos.")
                animal = input("Novo animal (Chip): ")
                if animal == "":
                    animal = None
                    break    

        return {"chip_original": chip_original, "cpf": cpf , "animal": animal}                        
                               