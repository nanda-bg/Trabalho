from entidade.cachorro import Cachorro
from controlador.controlador_pessoa import ControladorPessoa
from entidade.gato import Gato
from controlador.ong import ONG
from entidade.vacina import Vacina

def main():
    # Criando a ONG
    ong = ONG()
    
    # Criando vacinas
    vacina1 = Vacina("raiva")
    vacina2 = Vacina("leptospirose")
    vacina3 = Vacina("hepatite infecciosa")
    
    # Criando animais
    cachorro1 = Cachorro(chip=12345, nome="Rex", raca="Labrador", porte="grande")
    ong.adicionar_vacina(cachorro1, vacina1)
    ong.adicionar_vacina(cachorro1, vacina2)
    print(cachorro1)
    print("Vacinas cachorro 1: ", cachorro1.vacinas.__str__())
    print("Tem todas as vacinas básicas? ", cachorro1.tem_vacinas_basicas())
    
    gato1 = Gato(chip=67890, nome="Miau", raca="Siamês")
    ong.adicionar_vacina(gato1, vacina3)
    print(gato1)
    print("Vacinas gato 1: ", gato1.vacinas.__str__())
    print("Tem todas as vacinas básicas? ", gato1.tem_vacinas_basicas())
    print()
    print()
    
    #Deve ter 0
    print("Animais da Ong antes da doação: ", ong.todos_animais)
    # Deve ser 0 
    print("Animais dísponiveis antes da doação: ", ong.animais_disponiveis)
    print()

    # Criando doador
    cp = ControladorPessoa()
    doador = cp.incluir_doador(cpf=10542543974, nome="João", data_nascimento="1980-05-15", endereco="Rua A, 123")
    print(doador)
    # O doador doa um animal
    doacao = ong.doar(cachorro1, doador, "Animal não pode mais ser cuidado")
    print(doacao)
    print("Doações: ", ong.doacoes)
    print()

    #Deve ter 1 pois o cachorro1 foi doado
    print("Animais da Ong: ", ong.listar_animais())
    # Deve ser 0 pois o cachorrro1 não tem todas as vacinas básicas
    print("Animais dísponiveis: ", ong.listar_animais_disponiveis())
    print()

    # Criando adotante
    adotante = cp.incluir_adotante(cpf=81815434244, nome="Maria", data_nascimento="2000-03-10", endereco="Rua B, 456", 
                        tipo_habitacao="casa", tamanho_habitacao="grande", possui_animais=False)
    
    print(adotante)

    # Criando adoção
    print("Animal da ONG:", ong.todos_animais[0])
    print("Cachorro1: ", cachorro1)
    adocao = ong.adotar(adotante, cachorro1)
    print(adocao)
    print()
    print()

    ong.adicionar_vacina(cachorro1, vacina3)

    print("Vacinas cachorro 1: ", cachorro1.vacinas)
    print("Tem todas as vacinas básicas? ", cachorro1.tem_vacinas_basicas())
    print()
    print("Animais:", ong.listar_animais)
    print("Animais Disponíveis:", ong.listar_animais_disponiveis)
    print()

    adocao2 = ong.adotar(adotante, cachorro1)

    print("Adoções: ", ong.adocoes)
    print("Animais da Ong: ", ong.todos_animais)
    print("Animais dísponiveis: ", ong.animais_disponiveis)

if __name__ == "__main__":
    main()
