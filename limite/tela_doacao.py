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
        print("3 - Excluir doação")
        print("4 - Alterar doação")
        print("0 - Voltar")

        print()

        return self.le_numero_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 0])

    def pega_dados_doacao(self):
        print("-------- DADOS DOAÇÃO ----------")

        cpf_doador = self.valida_cpf()
        tipo_animal = self.valida_tipo_animal()

        nome_animal = self.valida_nome_animal()
        chip_animal = self.valida_chip()
        raca_animal = self.valida_raca_animal()

        vacinas_animal = self.valida_vacinas()

        motivo_doacao = self.valida_motivo_doacao()

        if tipo_animal == "cachorro":
            porte = self.valida_porte()
            return {
                "cpf_doador": cpf_doador,
                "nome_animal": nome_animal,
                "chip_animal": chip_animal,
                "raca_animal": raca_animal,
                "vacinas_animal": vacinas_animal,
                "porte": porte,
                "motivo_doacao": motivo_doacao,
                "tipo_animal": tipo_animal,
            }

        return {
            "cpf_doador": cpf_doador,
            "nome_animal": nome_animal,
            "chip_animal": chip_animal,
            "raca_animal": raca_animal,
            "vacinas_animal": vacinas_animal,
            "motivo_doacao": motivo_doacao,
            "tipo_animal": tipo_animal
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

    def pega_chip(self):
        chip = self.valida_chip()

        return chip

    def pega_dados_alteracao(self):
        self.mostrar_mensagem("Informações para buscar a doação")
        chip_original = self.valida_chip()

        print()
        self.mostrar_mensagem("Digite os novos dados da doação. Para manter os dados antigos, apenas aperte Enter.")

        cpf = input("Novo doador (CPF): ")
        
        if cpf == "":
            cpf = None

        else:    
            cpf_esta_correto = self.validar_numeros_cpf(cpf)

            while not cpf_esta_correto:
                self.mostrar_mensagem("CPF inválido, tente novamente")
                cpf = input("Novo doador (CPF): ")
                if cpf == "":
                    cpf = None
                    break
                cpf_esta_correto = self.validar_numeros_cpf

        animal = input("Novo animal (Chip): ")
        if animal == "":
            animal = None
        else:
            while not ( len(animal) == 7 and animal.isdigit() ):
                self.mostrar_mensagem("O chip deve ter 7 dígitos numéricos.")
                animal = input("Novo animal (Chip): ")
                if animal == "":
                    animal = None
                    break

        motivo_doacao = input("Novo motivo da doação: ")

        if motivo_doacao == "":
            motivo_doacao = None
        else:
            while not len(motivo_doacao) >= 3:
                motivo_doacao = input("Novo motivo da doação (mínimo 3 caracteres): ")

                if motivo_doacao == "":
                    motivo_doacao = None
                    break

        return {"chip_original": chip_original, "cpf": cpf , "animal": animal, "motivo_doacao": motivo_doacao}            