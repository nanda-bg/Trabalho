import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from exception.camposVaziosException import CampoVaziosException
from exception.chipInvalidoException import ChipInvalidoException

class TelaAnimal:
    def __init__(self, root):
        self.root = root
        self.opcao_selecionada = None
        self.root.title("Gerenciamento de Animais")
        self.root.geometry("500x700")
        self.root.configure(bg="#fdd9b9")

    def limpar_tela(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_widgets(self):
        tk.Label(self.root, text="Gerenciamento de Animais", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)
        tk.Label(self.root, text="Escolha uma operação:", font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)

        opcoes = [
            ("Listar todos os animais", 1),
            ("Listar animais disponíveis", 2),
            ("Buscar animal por chip", 3),
            ("Adicionar vacina", 4),
            ("Remover animal", 5),
            ("Retornar ao Menu Principal", 6)
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

    def pega_dados_animal(self, tipo='gato'):
        self.limpar_tela()
        dados = {}
        
        tk.Label(self.root, text=f"Cadastro de {tipo.capitalize()}", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        labels = ["Chip:", "Nome:", "Raça:", "Vacinas"]
        campos = ["chip", "nome", "raca", "vacinas"]

        if tipo == "cachorro":
            labels += ["Porte:"]
            campos += ["porte"]

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
            if campo == "porte":
                opcao_porte = tk.StringVar(self.root)
                opcao_porte.set("Escolha...")
                tamanho_porte = tk.OptionMenu(self.root, opcao_porte, "Grande", "Médio", "Pequeno")
                configurar_opcao(tamanho_porte)
                tamanho_porte.pack(pady=5)
                dados[campo] = opcao_porte
            
            elif campo == "vacinas":
                vacinas_selecionadas = []    
                vacinas_disponiveis = ["raiva", "leptospirose", "hepatite infecciosa", "cinomose", "parvovirose", "coronavirose"]
                for vacina in vacinas_disponiveis:
                    var = tk.BooleanVar()
                    checkbox = tk.Checkbutton(self.root, text=vacina, variable=var)
                    checkbox.pack(pady=3)
                    vacinas_selecionadas.append((vacina, var))
                dados[campo] = vacinas_selecionadas

            else:
                entrada = tk.Entry(self.root, font=("Times New Roman", 12))
                entrada.pack(pady=5)
                dados[campo] = entrada 

        def confirmar():
            try:
                campos_vazios = []

                for key, campo in dados.items():
                    valor = campo
                    if not valor:
                        campos_vazios.append(key)
                    dados[key] = valor

                if campos_vazios:
                    raise CampoVaziosException(campos_vazios)
                
                vacinas_selecionadas_lista = [vacina for vacina, var in vacinas_selecionadas if var]
                dados["vacinas"] = vacinas_selecionadas_lista
        
                for key, campo in dados.items():
                    if key != "vacinas":
                        dados[key] = campo.get()

                dados["tipo_animal"] = tipo        
                self.opcao_selecionada = dados
                self.root.quit()
            except Exception as e:
                self.mostrar_mensagem(e)    
            

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

    def seleciona_animal(self):
        self.limpar_tela()

        tk.Label(self.root, text="Digite o chip do animal:", font=("Times New Roman", 14), bg="#fdd9b9").pack(pady=10)
        entrada_chip = tk.Entry(self.root, font=("Times New Roman", 12))
        entrada_chip.pack(pady=10)

        def confirmar():
            try:
                chip = entrada_chip.get()

                if not chip.isdigit() or len(chip) != 7:
                    raise ChipInvalidoException()
                
                self.opcao_selecionada = int(entrada_chip.get())
                self.root.quit()
                
            except ChipInvalidoException as e:
                self.mostrar_mensagem(e)

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
    
    def alterar_cadastro(self):
        resposta = messagebox.askquestion("CPF já cadastrado para um adotante", "Doadores não podem ser adotantes, portanto ao alterar o cadastro para doador você não poderá mais adotar animais, deseja alterar seu cadastro?")
        if resposta == "yes":
            return "s"
        else:
            return "n"

    
    def exibir_dados_animal(self, dados_animal, tipo):
        self.limpar_tela()

        titulo = f"Dados do {tipo.capitalize()}"
        tk.Label(self.root, text=titulo, font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        vacinas = "\n".join(f"Vacina: {vacina}" for vacina in dados_animal["vacinas"]) if dados_animal["vacinas"] else "Nenhuma vacina registrada."

        dados = [
            "Chip: " + dados_animal["chip"],
            "Nome: " + dados_animal["nome"],
            "Raça: " + dados_animal["raca"],
            vacinas
        ]


        if tipo.lower() == "cachorro":
            dados += [
                "Porte: " + dados_animal["porte"],
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

    def exibir_dados_animais(self, lista_animais):
            self.limpar_tela()
            titulo = "Lista de Animais"
            tk.Label(self.root, text=titulo, font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

            # Criação do Treeview
            colunas = ("Chip", "Nome", "Raça", "Vacinas")
            tabela = ttk.Treeview(self.root, columns=colunas, show="headings", height=10)

            # Configurar cabeçalhos
            for coluna in colunas:
                tabela.heading(coluna, text=coluna)

                tabela.column(coluna, anchor="center", width=200)
            
            # Adicionar os dados à tabela
            for animal in lista_animais:
                tabela.insert("", "end", values=(
                    animal["Chip"], 
                    animal["Nome"], 
                    animal["Raça"], 
                    animal["Vacinas"]))

            tabela.pack(pady=10, padx=10)

            def voltar():
                self.root.quit()

            # Botão voltar
            tk.Button(
                self.root,
                text="Voltar",
                command= voltar,
                font=("Times New Roman", 12),
                bg="#ff7e0e",
                fg="white",
                width=30
            ).pack(pady=20)

            

            self.root.mainloop()


    def pega_dados_vacina(self):
        self.limpar_tela()
        dados = {}

        tk.Label(self.root, text=f"Vacinação", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        labels = ["Vacinas"]
        campos = ["vacinas"]

        for label, campo in zip(labels, campos):
            tk.Label(self.root, text=label, font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)

            vacinas_selecionadas = []    
            vacinas_disponiveis = ["raiva", "leptospirose", "hepatite infecciosa", "cinomose", "parvovirose", "coronavirose"]
            for vacina in vacinas_disponiveis:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(self.root, text=vacina, variable=var)
                checkbox.pack(pady=3)
                vacinas_selecionadas.append((vacina, var))
            dados[campo] = vacinas_selecionadas

        def confirmar():            
            vacinas_selecionadas_lista = [vacina for vacina, var in vacinas_selecionadas if var.get()]
       
            self.opcao_selecionada = vacinas_selecionadas_lista
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
        