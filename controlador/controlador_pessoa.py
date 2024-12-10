from datetime import date
from DAO.adotante_dao import AdotanteDAO
from DAO.doador_dao import DoadorDAO
from entidade.adotante import Adotante
from entidade.doador import Doador
from view.tela_pessoa import TelaPessoa


class ControladorPessoa():
    def __init__(self, controlador_sistema, root):
        self.__adotante_DAO = AdotanteDAO()
        self.__doador_DAO = DoadorDAO()
        self.__root = root
        self.__controlador_sistema = controlador_sistema
        self.__tela_pessoa = TelaPessoa(self.__root)

    @property
    def adotantes(self):
        return self.__adotantes
    
    @property
    def doadores(self):
        return self.__doadores
    
    def incluir_doador(self):
        dados_doador = self.__tela_pessoa.pega_dados_pessoa("doador")
        if dados_doador["cpf"] is None:
            return
        
        cpf = dados_doador["cpf"]
        nome = dados_doador["nome"]
        data_nascimento = dados_doador["data_nascimento"]
        endereco = dados_doador["endereco"]

        if not self.validar_cpf(cpf):
            print("cpf invalido")
            self.__tela_pessoa.mostrar_mensagem("CPF inválido")
            return
        
        if self.buscar_pessoa(cpf) != None:
            if isinstance(self.buscar_pessoa(cpf), Adotante):
                alterar = self.__tela_pessoa.alterar_cadastro()

                if alterar == 's':
                    self.__adotante_DAO.remove(self.buscar_pessoa(cpf))

                    doador = Doador(cpf, nome, data_nascimento, endereco)
                    self.__doador_DAO.add(doador)

                    self.__tela_pessoa.mostrar_mensagem("Cadastro alterado com sucesso")

                    return doador

                return

            self.__tela_pessoa.mostrar_mensagem("Doador já cadastrado")
            return
        
        doador = Doador(cpf, nome, data_nascimento, endereco)

        self.__doador_DAO.add(doador)

        print()
        self.__tela_pessoa.mostrar_mensagem("Doador cadastrado com sucesso.")

        return doador

    def incluir_adotante(self):
        dados_adotante = self.__tela_pessoa.pega_dados_pessoa("adotante")
        if dados_adotante["cpf"] is None:
            return
        
        cpf = dados_adotante["cpf"]
        nome = dados_adotante["nome"]
        data_nascimento = dados_adotante["data_nascimento"]
        endereco = dados_adotante["endereco"]
        tipo_habitacao = dados_adotante["tipo_habitacao"]
        tamanho_habitacao = dados_adotante["tamanho_habitacao"]
        possui_animais = dados_adotante["possui_animais"]

        if not self.validar_cpf(cpf):
            self.__tela_pessoa.mostrar_mensagem("CPF inválido")
            return
        
        if self.buscar_pessoa(cpf) != None:
            if isinstance(self.buscar_pessoa(cpf), Doador):
                self.__tela_pessoa.mostrar_mensagem("CPF já cadastrado para um doador, portanto não pode ser de um adotante")

            else:
                self.__tela_pessoa.mostrar_mensagem("CPF já cadastrado para um adotante")
            return
            
        if not self.validar_idade(data_nascimento):
            self.__tela_pessoa.mostrar_mensagem("O adotante precisa ser maior de 18 anos")
            return

        adotante = Adotante(cpf, nome, data_nascimento, endereco, tipo_habitacao, tamanho_habitacao, possui_animais)
        self.__adotante_DAO.add(adotante)

        self.__tela_pessoa.mostrar_mensagem("Adotante cadastrado com sucesso")

        return adotante

    def listar_doadores(self):
        if len(self.__doador_DAO.get_all()) == 0:
            self.__tela_pessoa.mostrar_mensagem("Nenhum doador cadastrado")
            return
        
        self.__tela_pessoa.exibir_dados_doadores(self.__doador_DAO.get_all())
        
        print("acabou")

        return self.__doador_DAO.get_all()
    
    def listar_adotantes(self):
        if len(self.__adotante_DAO.get_all()) == 0:
            self.__tela_pessoa.mostrar_mensagem("Nenhum adotante cadastrado")
            return
        
        self.__tela_pessoa.exibir_dados_adotantes(self.__adotante_DAO.get_all())

        return self.__adotante_DAO.get_all()

    def buscar_pessoa(self, cpf = None):
        valor_inicial = cpf
        cpf = self.__tela_pessoa.seleciona_pessoa() if cpf is None else cpf

        if cpf is not None:
            for doador in self.__doador_DAO.get_all():    
                 if doador.cpf == cpf:
                    if valor_inicial == None:
                        dados_doador = {"nome": doador.nome, "cpf": doador.cpf, "data_nascimento": doador.data_nascimento, "endereco": doador.endereco}
                        self.__tela_pessoa.exibir_dados_pessoa(dados_doador, "doador")
                    return doador

            for adotante in self.__adotante_DAO.get_all():
                if adotante.cpf == cpf:
                    if valor_inicial == None:
                        dados_adotante = {"nome": adotante.nome, "cpf": adotante.cpf, "data_nascimento": adotante.data_nascimento, "endereco": adotante.endereco, "tipo_habitacao": adotante.tipo_habitacao, "tamanho_habitacao":adotante.tamanho_habitacao, "possui_animais": adotante.possui_animais}
                        self.__tela_pessoa.exibir_dados_pessoa(dados_adotante, "adotante")
                    return adotante

            if valor_inicial == None:    
                self.__tela_pessoa.mostrar_mensagem("Pessoa não encontrada.")    

        return None 
    
    def validar_idade(self, data_nascimento):
        # Passa a data de nascimento para o formato de data
        nascimento = date.fromisoformat(data_nascimento)

        # Calcula a idade
        idade = date.today().year - nascimento.year

        # Retorna se a pessoa é maior de idade
        return idade >= 18    

    def validar_cpf(self, cpf):
        # Limpa o cpf para deixar apenas os números
        cpf = cpf.replace('.', '').replace('-', '')

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11 or not cpf.isdigit():
            return False

        # Verifica se todos os dígitos são iguais
        if len(set(cpf)) == 1:
            return False

        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito_1 = 0 if resto < 2 else 11 - resto

        # Verifica o primeiro dígito verificador
        if int(cpf[9]) != digito_1:
            return False

        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito_2 = 0 if resto < 2 else 11 - resto

        # Verifica o segundo dígito verificador
        if int(cpf[10]) != digito_2:
            return False
        
        return True

    def alterar_doador(self):
        dados = self.__tela_pessoa.pega_dados_alteracao("doador")

        cpf = dados["cpf"]
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is None:
            self.__tela_pessoa.mostrar_mensagem("Pessoa não encontrada.")
            return None

        if not isinstance(pessoa, Doador):
            self.__tela_pessoa.mostrar_mensagem("Essa pessoa não é um doador.")
            return None

        novo_nome = dados["nome"]
        novo_endereco = dados["endereco"]

        if novo_nome is not None:
            pessoa.nome = novo_nome

        if novo_endereco is not None:
            pessoa.endereco = novo_endereco

        self.__tela_pessoa.mostrar_mensagem("Dados do doador alterados com sucesso.")
        self.__doador_DAO.update(pessoa)
        return pessoa

    def alterar_adotante(self):
        dados = self.__tela_pessoa.pega_dados_alteracao("adotante")
        print("cpf", dados["cpf"])
        print("nome", dados["nome"])
        print("endereco", dados["endereco"])
        print("tipo_habitacao", dados["tipo_habitacao"])
        print("tamanho_habitacao", dados["tamanho_habitacao"])
        print("possui_animais", dados["possui_animais"])



        cpf = dados["cpf"]
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is None:
            self.__tela_pessoa.mostrar_mensagem("Pessoa não encontrada.")
            return None

        if not isinstance(pessoa, Adotante):
            self.__tela_pessoa.mostrar_mensagem("Essa pessoa não é um adotante.")
            return None

        novo_nome = dados["nome"]
        novo_endereco = dados["endereco"]
        novo_tipo_habitacao = dados["tipo_habitacao"]
        novo_tamanho_habitacao = dados["tamanho_habitacao"]
        possui_animais = dados["possui_animais"]

        if novo_nome is not None:
            pessoa.nome = novo_nome

        if novo_endereco is not None:
            pessoa.endereco = novo_endereco

        if novo_tipo_habitacao is not None:
            pessoa.tipo_habitacao = novo_tipo_habitacao

        if novo_tamanho_habitacao is not None:
            pessoa.tamanho_habitacao = novo_tamanho_habitacao

        if possui_animais is not None:
            pessoa.possui_animais = True if possui_animais == "Sim" else False

        print()
        self.__tela_pessoa.mostrar_mensagem("Dados do adotante alterados com sucesso.")
        self.__adotante_DAO.update(pessoa)
        return pessoa
    
    def excluir_doador(self):
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is None:
            print()
            self.__tela_pessoa.mostrar_mensagem("Pessoa não encontrada.")
            return None

        if not isinstance(pessoa, Doador):
            print()
            self.__tela_pessoa.mostrar_mensagem("Essa pessoa não é um doador.")
            return None

        self.__doador_DAO.remove(pessoa.cpf)
        print()
        self.__tela_pessoa.mostrar_mensagem("Doador removido com sucesso.")
        return pessoa
    
    def excluir_adotante(self):
        cpf = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.buscar_pessoa(cpf)

        if pessoa is None:
            print()
            self.__tela_pessoa.mostrar_mensagem("Pessoa não encontrada.")
            return None

        if not isinstance(pessoa, Adotante):
            print()
            self.__tela_pessoa.mostrar_mensagem("Essa pessoa não é um adotante.")
            return None

        self.__adotante_DAO.remove(pessoa.cpf)
        print()
        self.__tela_pessoa.mostrar_mensagem("Adotante removido com sucesso.")
        return pessoa

    def abrir_tela(self):
        lista_opcoes = {1: self.incluir_doador, 2: self.incluir_adotante, 3: self.listar_doadores, 
                        4: self.listar_adotantes, 5: self.buscar_pessoa, 6:self.alterar_doador, 
                        7: self.alterar_adotante, 8: self.excluir_doador, 9: self.excluir_adotante, 
                        10: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pessoa.mostrar_tela()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.inicializa_sistema()