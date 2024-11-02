from exception.motivo_invalido_exception import MotivoInvalidoException
from limite.abstract_tela import AbstractTela
from limite.abstract_tela_acao import AbstractTelaAcao
from limite.abstract_tela_animal import AbstractTelaAnimal
from limite.abstract_tela_pessoa import AbstractTelaPessoa
from limite.abstract_tela_vacina import AbstractTelaVacina


class TelaDoacao(
    AbstractTela,
    AbstractTelaPessoa,
    AbstractTelaAnimal,
    AbstractTelaAcao,
    AbstractTelaVacina,
):
    def __init__(self):
        super().__init__()

    def tela_opcoes(self):
        print()
        print("-------- TELA DOAÇÃO ---------")
        print("Escolha uma opção:")
        print("1 - Doar")
        print("2 - Emitir relatório de doações")
        print("0 - Voltar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 0])

    def pega_dados_doacao(self):
        print("-------- DADOS DOAÇÃO ----------")

        cpf_doador = self.valida_cpf()
        nome_animal = self.valida_nome_animal()
        chip_animal = self.valida_chip()
        raca_animal = self.valida_raca_animal()

        vacinas_animal = self.valida_vacinas()

        motivo_doacao = self.valida_motivo_doacao()

        return {
            "cpf_doador": cpf_doador,
            "nome_animal": nome_animal,
            "chip_animal": chip_animal,
            "raca_animal": raca_animal,
            "vacinas_animal": vacinas_animal,
            "motivo_doacao": motivo_doacao,
        }

    def valida_motivo_doacao(self):
        while True:
            try:
                motivo_doacao = input("Motivo da doação: ")
                if len(motivo_doacao.strip()) < 4:
                    raise MotivoInvalidoException()

                return motivo_doacao

            except MotivoInvalidoException as e:
                self.mostrar_mensagem(e)

    def mostrar_mensagem(self, msg):
        print(msg)
        
    def mostrar_doacao(self, doacao):
        print(f"Nome do doador: {doacao.doador.nome}")
        print(f"CPF do doador: {doacao.doador.cpf}")

        print(f"Nome do animal: {doacao.animal.nome}")
        print(f"Chip do animal: {doacao.animal.chip}")

        print(f"Data da doação: {doacao.data}")    
    