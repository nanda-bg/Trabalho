from datetime import date
from entidade.adotante import Adotante
from entidade.doador import Doador
from limite.tela_pessoa import TelaPessoa


class ControladorPessoa():
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__doadores = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_sistema = controlador_sistema

    @property
    def adotantes(self):
        return self.__adotantes
    
    @property
    def doadores(self):
        return self.__doadores
    
    def incluir_doador(self):
        print()
        dados_doador = self.__tela_pessoa.pega_dados_doador()
        cpf = dados_doador["cpf"]
        nome = dados_doador["nome"]
        data_nascimento = dados_doador["data_nascimento"]
        endereco = dados_doador["endereco"]

        if not self.validar_cpf(cpf):
            self.__tela_pessoa.mostrar_mensagem("CPF inválido")
            return
        
        if self.buscar_pessoa(cpf) != None:
            if isinstance(self.buscar_pessoa(cpf), Adotante):
                self.__tela_pessoa.mostrar_mensagem("CPF já cadastrado para um adotante")
                self.__tela_pessoa.mostrar_mensagem("Doadores não podem ser adotantes, portanto ao alterar o cadastro para doador você não poderá mais adotar animais")
                alterar = input("Deseja alterar o cadastro para doador? (s/n) ")

                if alterar == 's':
                    self.__adotantes.remove(self.buscar_pessoa(cpf))

                    doador = Doador(cpf, nome, data_nascimento, endereco)
                    self.__doadores.append(doador)

                    self.__tela_pessoa.mostrar_mensagem("Cadastro alterado com sucesso")

                    return doador

                return

            self.__tela_pessoa.mostrar_mensagem("Doador já cadastrado")
            return
        
        doador = Doador(cpf, nome, data_nascimento, endereco)

        self.__doadores.append(doador)

        print()
        self.__tela_pessoa.mostrar_mensagem("Doador cadastrado com sucesso.")

        return doador

    def incluir_adotante(self):
        print()
        dados_adotante = self.__tela_pessoa.pega_dados_adotante()
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

            self.__tela_pessoa.mostrar_mensagem("CPF já cadastrado para um adotante")
            return
            
        if not self.validar_idade(data_nascimento):
            self.__tela_pessoa.mostrar_mensagem("O adotante precisa ser maior de 18 anos")
            return

        adotante = Adotante(cpf, nome, data_nascimento, endereco, tipo_habitacao, tamanho_habitacao, possui_animais)
        self.__adotantes.append(adotante)

        self.__tela_pessoa.mostrar_mensagem("Adotante cadastrado com sucesso")

        return adotante

    def listar_doadores(self):
        if len(self.__doadores) == 0:
            self.__tela_pessoa.mostrar_mensagem("Nenhum doador cadastrado")
            return
        
        for doador in self.__doadores:
            self.__tela_pessoa.mostrar_pessoa(doador)

        return self.__doadores
    
    def listar_adotantes(self):
        if len(self.__adotantes) == 0:
            self.__tela_pessoa.mostrar_mensagem("Nenhum adotante cadastrado")
            return
        
        for adotante in self.__adotantes:
            self.__tela_pessoa.mostrar_pessoa(adotante)

        return self.__adotantes

    def buscar_pessoa(self, cpf = None):
        if cpf == None:
            cpf = self.__tela_pessoa.seleciona_pessoa()

        pessoas = self.__adotantes + self.__doadores

        for pessoa in pessoas:
            if pessoa.cpf == cpf:
                self.__tela_pessoa.mostrar_pessoa(pessoa)
                return pessoa
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


    def abrir_tela(self):
        lista_opcoes = {1: self.incluir_doador, 2: self.incluir_adotante, 3: self.listar_doadores, 
                        4: self.listar_adotantes, 5: self.buscar_pessoa, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controlador_sistema.abrir_tela_inicial()