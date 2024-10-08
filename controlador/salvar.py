def rodar(self):
        while True:
            opcao = self.tela_pessoa.tela_opcoes()

            if opcao == 1:  # Incluir Doador
                dados_doador = self.tela_pessoa.pega_dados_doador()
                try:
                    doador = self.controlador_pessoa.incluir_doador(dados_doador["cpf"], dados_doador["nome"], dados_doador["data_nascimento"], dados_doador["endereco"])
                    self.tela_pessoa.mostra_mensagem("Doador incluído com sucesso!")
                except ValueError as e:
                    self.tela_pessoa.mostra_mensagem(str(e))

            elif opcao == 2:  # Incluir Adotante
                dados_adotante = self.tela_pessoa.pega_dados_adotante()
                try:
                    adotante = self.controlador_pessoa.incluir_adotante(**dados_adotante)
                    self.tela_pessoa.mostra_mensagem("Adotante incluído com sucesso!")
                except ValueError as e:
                    self.tela_pessoa.mostra_mensagem(str(e))

            elif opcao == 3:  # Listar Doadores
                doadores = self.controlador_pessoa.listar_doadores()
                for doador in doadores:
                    self.tela_pessoa.mostra_pessoa(doador)

            elif opcao == 4:  # Listar Adotantes
                adotantes = self.controlador_pessoa.listar_adotantes()
                for adotante in adotantes:
                    self.tela_pessoa.mostra_pessoa(adotante)

            elif opcao == 5:  # Buscar Pessoa por CPF
                cpf = self.tela_pessoa.seleciona_pessoa()
                pessoa = self.controlador_pessoa.buscar_pessoa(cpf)
                if pessoa:
                    self.tela_pessoa.mostra_pessoa(pessoa)
                else:
                    self.tela_pessoa.mostra_mensagem("Pessoa não encontrada.")

            elif opcao == 0:  # Sair
                break

            else:
                self.tela_pessoa.mostra_mensagem("Opção inválida.")
