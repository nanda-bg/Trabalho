from datetime import date
from entidade.adotante import Adotante
from entidade.doador import Doador
from limite.tela_pessoa import TelaPessoa


class ControladorPessoa():
    def __init__(self, controlador_sistema):
        self.__adotantes = []
        self.__doadores = []
        self.__tela_pessoa = TelaPessoa()
        self.__controloador_sistema = controlador_sistema

    @property
    def adotantes(self):
        return self.__adotantes
    
    @property
    def doadores(self):
        return self.__doadores
    
    def incluir_doador(self):
        dados_doador = self.__tela_pessoa.pega_dados_doador()
        cpf = dados_doador["cpf"]
        nome = dados_doador["nome"]
        data_nascimento = dados_doador["data_nascimento"]
        endereco = dados_doador["endereco"]

        if self.verificacoes_basicas(cpf, nome, data_nascimento, endereco):
            doador = Doador(cpf, nome, data_nascimento, endereco)

            self.__doadores.append(doador)

            return doador

    def incluir_adotante(self):
        dados_adotante = self.__tela_pessoa.pega_dados_adotante()
        cpf = dados_adotante["cpf"]
        nome = dados_adotante["nome"]
        data_nascimento = dados_adotante["data_nascimento"]
        endereco = dados_adotante["endereco"]
        tipo_habitacao = dados_adotante["tipo_habitacao"]
        tamanho_habitacao = dados_adotante["tamanho_habitacao"]
        possui_animais = dados_adotante["possui_animais"]

        if self.buscar_pessoa(cpf) != None:
            self.__tela_pessoa.mostra_mensagem("Pessoa já cadastrada")
            return
            
        if not isinstance(tipo_habitacao, str):
            self.__tela_pessoa.mostra_mensagem('O tipo de habitação deve ser uma string')
            return
            
        if not isinstance(tamanho_habitacao, str):
            self.__tela_pessoa.mostra_mensagem('O tamanho da habitação deve ser uma string')
            return
            
        if not isinstance(possui_animais, bool):
            self.__tela_pessoa.mostra_mensagem('O campo possui animais deve ser um booleano')
            return
            
        if not self.validar_idade(data_nascimento):
            self.__tela_pessoa.mostra_mensagem("O adotante precisa ser maior de 18 anos")
            return
                    
        if self.verificacoes_basicas(cpf, nome, data_nascimento, endereco):
            adotante = Adotante(cpf, nome, data_nascimento, endereco, tipo_habitacao, tamanho_habitacao, possui_animais)
            self.__adotantes.append(adotante)

            return adotante

    def listar_doadores(self):
        for doador in self.__doadores:
            self.__tela_pessoa.mostra_pessoa(doador)

        return self.__doadores
    
    def listar_adotantes(self):
        for adotante in self.__adotantes:
            self.__tela_pessoa.mostra_pessoa(adotante)

        return self.__adotantes

    def buscar_pessoa(self):
        cpf = self.__tela_pessoa.seleciona_pessoa()

        pessoas = self.__adotantes + self.__doadores

        for pessoa in pessoas:
            if pessoa.cpf == cpf:
                self.__tela_pessoa.mostra_pessoa(pessoa)
                return pessoa
        return None
    
    def validar_idade(self, data_nascimento):
        # Passa a data de nascimento para o formato de data
        nascimento = date.fromisoformat(data_nascimento)

        # Calcula a idade
        idade = date.today().year - nascimento.year

        # Retorna se a pessoa é maior de idade
        return idade >= 18    

    def verificacoes_basicas(self, cpf, nome, data_nascimento, endereco):
        if not isinstance(cpf, str):
            self.__tela_pessoa.mostra_mensagem('O CPF deve ser uma string')
            return False
        
        if not self.validar_cpf(cpf):
            self.__tela_pessoa.mostra_mensagem('CPF inválido')
            return False
        
        if not isinstance(nome, str):
            self.__tela_pessoa.mostra_mensagem('O nome deve ser uma string')
            return False
        
        if not isinstance(data_nascimento, str):
            self.__tela_pessoa.mostra_mensagem('A data de nascimento deve ser uma string')
            return False
        
        if not isinstance(endereco, str):
            self.__tela_pessoa.mostra_mensagem('O endereço deve ser uma string')
            return False
        
        return True
    

    def validar_cpf(self, cpf):
        cpf = cpf.replace('.','')
        cpf = cpf.replace('-', '')

        conjunto = set(list(cpf))

        if len(conjunto) > 1:
            multiplicador = len(cpf)-1
            parada = multiplicador-1
            comparador = -2
            valido = True

            while comparador < 0 and valido:
                i = 0
                soma = 0
                while i < parada:
                    soma += int(cpf[i]) * multiplicador
                    multiplicador -= 1
                    i += 1
                    
                resto = soma%11

                if  (resto <= 9 and int(cpf[comparador]) == 11-resto) or (resto > 9 and int(cpf[comparador]) == 0):
                    multiplicador = len(cpf)
                    parada = multiplicador-1
                    comparador += 1
                else:
                    valido = False
        
        else:
            valido = False
        
        return valido

    def abrir_tela(self):
        lista_opcoes = {1: self.incluir_doador, 2: self.incluir_adotante, 3: self.listar_doadores, 
                        4: self.listar_adotantes, 5: self.buscar_pessoa, 0: self.retornar}

        while True:
            opcao_escolhida = self.__tela_pessoa.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()

    def retornar(self):
        self.__controloador_sistema.abrir_tela_inicial()