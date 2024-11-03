from datetime import date
from entidade.adotante import Adotante
from entidade.adocao import Adocao
from entidade.animal import Animal
from entidade.cachorro import Cachorro
from entidade.doador import Doador
from entidade.doacao import Doacao
from entidade.vacina import Vacina


class ONG:
    def __init__(self):
        self.todos_animais = []
        self.animais_disponiveis = []
        self.adocoes = []
        self.doacoes = []

    def adicionar_animal(self, chip: int, nome: str, raca: str, vacinas=None):
        if not isinstance(chip, int):
            raise ValueError("O chip deve ser um número inteiro.")

        if not isinstance(nome, str):
            raise ValueError("O nome deve ser uma string.")

        if not isinstance(raca, str):
            raise ValueError("A raça deve ser uma string.")

        animal = Animal(chip, nome, raca, vacinas)

        self.todos_animais.append(animal)

        if animal.tem_vacinas_basicas():
            self.animais_disponiveis.append(animal)

        return animal

    def remover_animal(self, animal):
        if not isinstance(animal, Animal):
            raise ValueError("animal deve ser um objeto da classe Animal")

        if animal not in self.todos_animais:
            raise ValueError("animal não pertence a ONG")

        self.todos_animais.remove(animal)

        if animal in self.animais_disponiveis:
            self.animais_disponiveis.remove(animal)

    def adicionar_vacina(self, animal, vacina: Vacina):
        if not isinstance(vacina, Vacina):
            raise ValueError("A vacina deve ser um objeto da classe Vacina.")

        if not isinstance(animal, Animal):
            raise ValueError("animal deve ser um objeto da classe Animal")

        animal.nova_vacina(vacina)

        if animal.tem_vacinas_basicas() and animal not in self.animais_disponiveis:
            self.animais_disponiveis.append(animal)

    def listar_animais(self):
        if len(self.todos_animais) < 1:
            print("Nenhum animal")
            return

        return [animal.nome for animal in self.todos_animais]

    def listar_animais_disponiveis(self):
        if len(self.animais_disponiveis) < 1:
            print("Nenhum animal disponível.")
            return
        
        return [animal.nome for animal in self.animais_disponiveis]

    def emitir_relatorio_adocoes(self, inicio, fim):
        return [adocao for adocao in self.adocoes if inicio <= adocao.data <= fim]

    def emitir_relatorio_doacoes(self, inicio, fim):
        return [doacao for doacao in self.doacoes if inicio <= doacao.data <= fim]

    def doar(self, animal, doador, motivo_doacao):
        if not isinstance(animal, Animal):
            raise ValueError("animal deve ser um objeto da classe Animal")

        if not isinstance(doador, Doador):
            raise ValueError("doador deve ser um objeto da classe Doador")

        if not isinstance(motivo_doacao, str):
            raise ValueError("motivo_doacao deve ser uma string")

        doacao = Doacao(
            self, animal, doador, motivo_doacao, data=date.today().isoformat
        )

        self.doacoes.append(doacao)
        self.todos_animais.append(animal)

        return doacao

    def avaliar_adocao(self, animal, adotante):
        if not isinstance(adotante, Adotante):
            raise ValueError("adotante deve ser um objeto da classe adotante")

        if not isinstance(animal, Animal):
            print("animal deve ser um objeto da classe Animal")
            return

        if isinstance(animal, Cachorro):
            if animal.porte == "grande" and (
                adotante.tipo_habitacao == "apartamento"
                and adotante.tamanho_habitacao == "pequeno"
            ):
                return False

        if not animal.tem_vacinas_basicas():
            return False

        for doação in self.doacoes:
            if adotante.cpf == doação.doador.cpf:
                return False

        return True

    def adotar(self, adotante, animal):
        if not isinstance(adotante, Adotante):
            raise ValueError("adotante deve ser um objeto da classe Adotante")

        if animal not in self.todos_animais:
            print("Animal não pertence a ONG")
            return

        if self.avaliar_adocao(animal, adotante):
            print(f"Adoção do animal {animal.nome} aprovada.")

            adocao = Adocao(animal, adotante)

            if adocao.termo_assinado == False:
                assinar_termo = input("Deseja assinar o termo de adoção? (s/n)")

            if assinar_termo == "s" or adocao.termo_assinado:
                adocao = Adocao(self, animal, adotante, True)
                adocao.termo_assinado = True
                self.adocoes.append(adocao)
                self.remover_animal(animal)

            else:
                print(f"Processo de adoção do animal {animal.nome} não foi concluído.")
                return

            print(f"Adoção do animal {animal.nome} realizada com sucesso.")

        else:
            print(f"Adoção do animal {animal.nome} não foi aprovada.")

    def __str__(self):
        return f"ONG com {len(self.todos_animais)} animais cadastrados, {len(self.animais_disponiveis)} disponíveis para adoção, {len(self.adocoes)} adoções e {len(self.doacoes)} doações"
