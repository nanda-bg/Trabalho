from datetime import date
from adotante import Adotante
from animal import Animal
from cachorro import Cachorro
from ong import ONG


class Adocao:
    def __init__(self, ong, animal, adotante, termo_assinado = False, data = date.today().isoformat()):
        if not isinstance(ong, ONG):
            print("ong deve ser um objeto da classe ONG")
            return
        
        if not isinstance(animal, Animal):
            print("animal deve ser um objeto da classe Animal")
            return
        
        if animal not in ong.animais_disponiveis:
            print("animal não disponível para adoção")
            return
        
        if not isinstance(adotante, Adotante):
            print("adotante deve ser um objeto da classe Adotante")
            return
        
        if not isinstance(termo_assinado, bool):
            print("termo_assinado deve ser um booleano")
            return

        
        self._ong = ong
        self._animal = animal
        self._data = data
        self._adotante = adotante
        self._termo_assinado = termo_assinado

        self.adotar()

    @property
    def ong(self):
        return self._ong
    
    @property
    def data(self):
        return self._data

    @property
    def animal(self):
        return self._animal

    @property
    def adotante(self):
        return self._adotante

    @property
    def termo_assinado(self):
        return self._termo_assinado
    
    @termo_assinado.setter
    def termo_assinado(self, termo_assinado):
        if not isinstance(termo_assinado, bool):
            print("termo_assinado deve ser um booleano")
            return
        
        self._termo_assinado = termo_assinado

    def avaliar_adocao(self, animal, ong):
        if not isinstance(ong, ONG):
            print("ong deve ser um objeto da classe ONG")
            return
        
        if not isinstance(animal, Animal):
            print("animal deve ser um objeto da classe Animal")
            return
        
        if isinstance(animal, Cachorro):
            if (animal.porte == 'grande' and 
                (self.adotante.tipo_habitacao == 'apartamento' and 
                 self.adotante.tamanho_habitacao == 'pequeno'
                )
            ):
                return False
            
        if not animal.tem_vacinas_basicas:
            return False
            
        for doação in ong.doacoes:
            if self.adotante.cpf == doação.doador.cpf:
                return False
                
        return True    
    
    def adotar(self):
        if not isinstance(self.ong, ONG):
            print("ong deve ser um objeto da classe ONG")
            return
        
        if self.animal not in self.ong.todos_animais:
            print("Animal não pertence a essa ONG")
            return
        
        if self.avaliar_adocao(self.animal, self.ong):
            print(f"Adoção aprovada para o animal {self.animal.nome}.")

            if not self.termo_assinado:
                assinar_termo = input("Deseja assinar o termo de adoção? (s/n)")

                if assinar_termo == 's':
                    self.termo_assinado = True

                else:
                    print(f'Processo de adoção para o animal {self.animal.nome} não foi concluído.')
                    return

            self.ong.adocoes.append(self)
            self.ong.remover_animal(self.animal)
            print(f"Adoção realizada com sucesso para o animal {self.animal.nome}.")

        else:
            print(f"Adoção para o animal {self.animal.nome} não foi aprovada.")

    def __str__(self):
        return f"Adoção do animal {self.animal.nome} realizada por {self.adotante.nome} em {self.data}"        