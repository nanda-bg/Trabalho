import tkinter as tk
from tkinter import messagebox

class TelaPessoa:
    def __init__(self, root):
        self.root = root
        self.opcao_selecionada = None
        self.root.title("Gerenciamento de Pessoas")
        self.root.geometry("500x700")
        self.root.configure(bg="#fdd9b9")

    def limpar_tela(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_widgets(self):
        tk.Label(self.root, text="Gerenciamento de Pessoas", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)
        tk.Label(self.root, text="Escolha uma operação:", font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)

        opcoes = [
            ("Incluir Doador", 1),
            ("Incluir Adotante", 2),
            ("Listar Doadores", 3),
            ("Listar Adotantes", 4),
            ("Buscar Pessoa", 5),
            ("Alterar Doador", 6),
            ("Alterar Adotante", 7),
            ("Excluir Doador", 8),
            ("Excluir Adotante", 9),
            ("Retornar ao Menu Principal", 0)
        ]

        for i, (texto, valor) in enumerate(opcoes, start=1):  # 'i' é o número da opção
            botao = tk.Button(
                self.root,
                text=texto,
                command=lambda v=valor, num=i: self.set_opcao(num),  # Passa o valor e o número
                font=("Times New Roman", 12),
                bg="#ff7e0e",
                fg="white",
                width=30
            )
            botao.bind("<Enter>", lambda event, b=botao: b.config(bg="#eb6c00"))
            botao.bind("<Leave>", lambda event, b=botao: b.config(bg="#ff7e0e"))
            botao.pack(pady=5)

    def set_opcao(self, opcao):
        self.opcao_selecionada = opcao
        self.root.quit()

    def mostrar_tela(self):
        self.limpar_tela()
        self.criar_widgets()
        self.opcao_selecionada = None
        self.root.mainloop()
        return self.opcao_selecionada

    def mostrar_mensagem(self, mensagem):
        messagebox.showinfo("Informação", mensagem)

    def pega_dados_pessoa(self, tipo="doador"):
        self.limpar_tela()
        dados = {}

        tk.Label(self.root, text=f"Cadastro de {tipo.capitalize()}", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        labels = ["CPF:", "Nome:", "Data de Nascimento (AAAA-MM-DD):", "Endereço:"]
        campos = ["cpf", "nome", "data_nascimento", "endereco"]

        if tipo == "adotante":
            labels += ["Tipo de Habitação:", "Tamanho da Habitação:", "Possui Animais? (Sim/Não):"]
            campos += ["tipo_habitacao", "tamanho_habitacao", "possui_animais"]

        def configurar_opcao(opcao):
            opcao.config(
                font=("Times New Roman", 12),   # Fonte Times New Roman, tamanho 12
                bg="white",                     # Cor de fundo branco
                fg="black",                     # Cor do texto preta
                relief="solid",                 # Borda de contorno (opcional)
                width=15                        # Largura do menu (ajuste conforme necessário)
            )   

        for label, campo in zip(labels, campos):
            tk.Label(self.root, text=label, font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)
            if campo == "tipo_habitacao":
                opcao_habitacao = tk.StringVar(self.root)
                opcao_habitacao.set("Escolha...")  # Valor padrão
                tipo_habitacao = tk.OptionMenu(self.root, opcao_habitacao, "Casa", "Apartamento")
                configurar_opcao(tipo_habitacao)        
                tipo_habitacao.pack(pady=5)
                dados[campo] = opcao_habitacao

            elif campo == "tamanho_habitacao":
                opcao_habitacao = tk.StringVar(self.root)
                opcao_habitacao.set("Escolha...")
                tamanho_habitacao = tk.OptionMenu(self.root, opcao_habitacao, "Grande", "Pequeno")
                configurar_opcao(tamanho_habitacao)
                tamanho_habitacao.pack(pady=5)
                dados[campo] = opcao_habitacao

            elif campo == "possui_animais":
                opcao_animal = tk.StringVar(self.root)
                opcao_animal.set("Escolha...")
                tem_animal = tk.OptionMenu(self.root, opcao_animal, "Sim", "Não")
                configurar_opcao(tem_animal)
                tem_animal.pack(pady=5)
                dados[campo] = opcao_animal
                  
            else:
                entrada = tk.Entry(self.root, font=("Times New Roman", 12))
                entrada.pack(pady=5)
            dados[campo] = entrada 

        def confirmar():
            campos_vazios = []

            for key, campo in dados.items():
                valor = campo
                if not valor:
                    campos_vazios.append(key)
                dados[key] = valor

            if campos_vazios:
                messagebox.showerror("Erro", f"Os seguintes campos são obrigatórios: {', '.join(campos_vazios)}.")
                return
    
            for key, campo in dados.items():
                dados[key] = campo.get()
            self.opcao_selecionada = dados
            self.root.quit()

        def voltar():
            for key in dados:
                dados[key] = None
            self.opcao_selecionada = None
            self.root.quit()

        tk.Button(
            self.root,
            text="Confirmar",
            command=confirmar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white"
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Voltar",
            command=voltar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white",
            width=30
        ).pack(pady=20)


        self.root.mainloop()
        return dados

    def seleciona_pessoa(self):
        self.limpar_tela()

        tk.Label(self.root, text="Digite o CPF da Pessoa:", font=("Times New Roman", 14), bg="#fdd9b9").pack(pady=10)
        entrada_cpf = tk.Entry(self.root, font=("Times New Roman", 12))
        entrada_cpf.pack(pady=10)

        def confirmar():
            self.opcao_selecionada = entrada_cpf.get()
            self.root.quit()

        def voltar():
            self.opcao_selecionada = None
            self.root.quit()    

        tk.Button(
            self.root,
            text="Confirmar",
            command=confirmar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white"
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Voltar",
            command=voltar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white",
            width=30
        ).pack(pady=20)

        self.root.mainloop()
        return self.opcao_selecionada
    
    def exibir_dados_pessoa(self, dados_pessoa, tipo):
        self.limpar_tela()

        titulo = f"Dados do {tipo.capitalize()}"
        tk.Label(self.root, text=titulo, font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        # Exibe os dados básicos
        dados = [
            "CPF: " + dados_pessoa["cpf"],
            "Nome: " + dados_pessoa["nome"],
            "Data de Nascimento: " + dados_pessoa["data_nascimento"],
            "Endereço:  " + dados_pessoa["endereco"]
        ]

        # Se for um adotante, exibe os dados adicionais
        if tipo.lower() == "adotante":
            possui_animais = "Sim" if dados_pessoa["possui_animais"] == True else "Não"
            dados += [
                "Tipo de Habitação: " + dados_pessoa["tipo_habitacao"],
                "Tamanho da Habitação:  " + dados_pessoa["tamanho_habitacao"],
                "Possui Animais:  " + possui_animais
            ]

        self.mostrar_mensagem("\n".join(dados))

        tk.Button(
            self.root,
            text="Voltar",
            command=None,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white",
            width=30
        ).pack(pady=20)

    def pega_dados_alteracao(self, tipo="doador"):     
        self.limpar_tela()
        dados = {}

        tk.Label(self.root, text=f"Alteração de {tipo.capitalize()}", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        labels = ["CPF: ", "Nome:", "Endereço:"]
        campos = ["cpf", "nome", "endereco"]

        if tipo == "adotante":
            labels += ["Tipo de Habitação:", "Tamanho da Habitação:", "Possui Animais?:"]
            campos += ["tipo_habitacao", "tamanho_habitacao", "possui_animais"]

        def configurar_opcao(opcao):
            opcao.config(
                font=("Times New Roman", 12),   
                bg="white",                
                fg="black",                  
                relief="solid",                 
                width=15                       
            )   

        for label, campo in zip(labels, campos):
            tk.Label(self.root, text=label, font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)
            if campo == "tipo_habitacao":
                opcao_habitacao = tk.StringVar(self.root)
                opcao_habitacao.set("Escolha...") 
                tipo_habitacao = tk.OptionMenu(self.root, opcao_habitacao, "Casa", "Apartamento")
                configurar_opcao(tipo_habitacao)        
                tipo_habitacao.pack(pady=5)
                dados[campo] = opcao_habitacao
                print("tipo_habitacao", opcao_habitacao)

            elif campo == "tamanho_habitacao":
                opcao_habitacao = tk.StringVar(self.root)
                opcao_habitacao.set("Escolha...")
                tamanho_habitacao = tk.OptionMenu(self.root, opcao_habitacao, "Grande", "Pequeno")
                configurar_opcao(tamanho_habitacao)
                tamanho_habitacao.pack(pady=5)
                dados[campo] = opcao_habitacao.get()
                print("tamanho_habitacao", opcao_habitacao)

            elif campo == "possui_animais":
                opcao_animal = tk.StringVar(self.root)
                opcao_animal.set("Escolha...")
                tem_animal = tk.OptionMenu(self.root, opcao_animal, "Sim", "Não")
                configurar_opcao(tem_animal)
                tem_animal.pack(pady=5)
                dados[campo] = opcao_animal.get()
                print("possui animais campo get:", opcao_animal.get())
                  
            else:
                entrada = tk.Entry(self.root, font=("Times New Roman", 12))
                entrada.pack(pady=5)
            dados[campo] = entrada 

        def confirmar():
            campos_vazios = []

            for key, campo in dados.items():
                valor = campo if campo else None
                print("valor:", valor)
                dados[key] = valor
    
            for key, campo in dados.items():
                print("key:", key)
                print("campo:", campo)
                dados[key] = campo.get()
            self.opcao_selecionada = dados
            self.root.quit()

        def voltar():
            for key in dados:
                dados[key] = None
            self.opcao_selecionada = None
            self.root.quit()

        tk.Button(
            self.root,
            text="Confirmar",
            command=confirmar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white"
        ).pack(pady=20)

        tk.Button(
            self.root,
            text="Voltar",
            command=voltar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white",
            width=30
        ).pack(pady=20)


        self.root.mainloop()
        return dados