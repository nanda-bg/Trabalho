from datetime import datetime
import re
from tkcalendar import Calendar
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from exception.camposVaziosException import CampoVaziosException
from exception.chipInvalidoException import ChipInvalidoException
from exception.cpfInvalidoException import CPFInvalidoException
from exception.dataFinalInvalidaException import DataFinalInvalida
from view.abstract_tela import AbstractTela

class TelaAdocao(AbstractTela):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.opcao_selecionada = None
        self.root.title("Gerenciamento de Doações")
        self.root.geometry("500x700")
        self.root.configure(bg="#fdd9b9")

    def limpar_tela(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def criar_widgets(self):
        tk.Label(self.root, text="Gerenciamento de Doações", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)
        tk.Label(self.root, text="Escolha uma operação:", font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)

        opcoes = [
            ("Adotar", 1),
            ("Emitir Relatório", 2),
            ("Assinar termo de adoção", 3),
            ("Alterar Adoção", 4),
            ("Excluir Adoção", 5),
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

    def pega_dados_adocao(self):
        self.limpar_tela()
        dados = {}

        # Configurar canvas e scroll
        canvas = tk.Canvas(self.root, bg="#fdd9b9")
        scroll_y = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        container = tk.Frame(canvas, bg="#fdd9b9")

        # Configurar canvas e ligação com a rolagem
        canvas.create_window((0, 0), window=container, anchor="nw")
        canvas.configure(yscrollcommand=scroll_y.set)

        canvas.pack(side="left", fill="both", expand=True)
        scroll_y.pack(side="right", fill="y")

        container.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        central_frame = tk.Frame(container, bg="#fdd9b9")
        central_frame.pack(expand=True)

        tk.Label(central_frame, text="Cadastro do Animal", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        labels = ["CPF do adotante:", "Chip do Animal:"]
        campos = ["cpf_adotante", "chip_animal"]

        for label, campo in zip(labels, campos):
            tk.Label(central_frame, text=label, font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)
            entrada = tk.Entry(central_frame, font=("Times New Roman", 12))
            entrada.pack(pady=5)
            dados[campo] = entrada

        def confirmar():
            try: 
                campos_vazios = []

                for key, campo in dados.items():
                    if not campo:
                        campos_vazios.append(key)
                    dados[key] = campo

                if campos_vazios:
                    raise CampoVaziosException(campos_vazios)
                
                if not dados["cpf_adotante"].get().isdigit() or len(dados["cpf_adotante"].get()) != 11 or not self.validar_numeros_cpf(dados["cpf_adotante"].get()):
                    raise CPFInvalidoException()
                
                if not dados["chip_animal"].get().isdigit() or len(dados["chip_animal"].get()) != 7:
                    raise ChipInvalidoException()
        
                for key, campo in dados.items():
                    dados[key] = campo.get()

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
            central_frame,
            text="Confirmar",
            command=confirmar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white"
        ).pack(pady=20)

        tk.Button(
            central_frame,
            text="Voltar",
            command=voltar,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white",
            width=30
        ).pack(pady=20)

        self.root.mainloop()
        return dados


    def pega_datas_relatorio(self):
        def abrir_calendario(entry):
            def confirmar_data():
                data_selecionada = calendario.get_date()
                entry.delete(0, tk.END)
                entry.insert(0, data_selecionada)
                janela_calendario.destroy()

            janela_calendario = tk.Toplevel()
            janela_calendario.title("Selecionar Data")
            calendario = Calendar(janela_calendario, date_pattern="yyyy-mm-dd")
            calendario.pack(pady=10)
            tk.Button(janela_calendario, text="Confirmar", command=confirmar_data).pack(pady=10)

        def confirmar():
            try:
                campos_vazios = []

                data_inicio = entrada_inicio.get()
                data_fim = entrada_fim.get()

                if not data_inicio:
                    campos_vazios.append("Data de Início")

                if not data_fim:
                    campos_vazios.append("Data de Fim")

                if campos_vazios:
                    raise CampoVaziosException(campos_vazios)

                data_inicio_obj = datetime.strptime(data_inicio, "%Y-%m-%d").date()
                data_fim_obj = datetime.strptime(data_fim, "%Y-%m-%d").date()

                if data_inicio_obj > data_fim_obj:      
                    raise DataFinalInvalida()
                    
                datas["inicio"] = data_inicio
                datas["fim"] = data_fim

                janela_relatorio.destroy()

            except Exception as e:
                self.mostrar_mensagem(e)



        datas = {}

        # Janela de seleção
        janela_relatorio = tk.Toplevel()
        janela_relatorio.title("Selecionar Datas")
        janela_relatorio.geometry("300x200")
        janela_relatorio.configure(bg="#fdd9b9")

        tk.Label(janela_relatorio, text="Data de Início:", bg="#fdd9b9").pack(pady=5)
        entrada_inicio = tk.Entry(janela_relatorio, font=("Arial", 12))
        entrada_inicio.pack(pady=5)
        entrada_inicio.bind("<Button-1>", lambda e: abrir_calendario(entrada_inicio))

        tk.Label(janela_relatorio, text="Data de Fim:", bg="#fdd9b9").pack(pady=5)
        entrada_fim = tk.Entry(janela_relatorio, font=("Arial", 12))
        entrada_fim.pack(pady=5)
        entrada_fim.bind("<Button-1>", lambda e: abrir_calendario(entrada_fim))

        tk.Button(janela_relatorio, text="Confirmar", command=confirmar, bg="#ff7e0e", fg="white").pack(pady=20)

        self.root.wait_window(janela_relatorio)  # Aguarda o fechamento da janela_relatorio
        return datas


    def seleciona_animal(self):
        self.limpar_tela()

        tk.Label(self.root, text="Digite o chip do animal envolvido na adoção:", font=("Times New Roman", 14), bg="#fdd9b9").pack(pady=10)
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
    
    def confirmar_exclusão(self, dados_adocao):
        resposta = messagebox.askquestion("Confirme a exclusão", f"Tem certeza que deseja excluir a adoção do animal {dados_adocao['nome_animal']}?", icon="warning")
        if resposta == "yes":
            return "s"
        else:
            return "n"
        
    def deseja_assinar_termo(self, dados_adocao):
        resposta = messagebox.askquestion("Finalize a adoção", f"Deseja ir para o termo de adoção do animal {dados_adocao['nome_animal']}?")
        if resposta == "yes":
            return "s"
        else:
            return "n"    
        
    def assinar_termo(self, dados_adocao):
        resposta = messagebox.askquestion("Assine o termo de adoção", 
                                          f"Eu, {dados_adocao['nome_adotante']}, portador do CPF {dados_adocao['cpf_adotante']}, "
                                          f"declaro que irei adotar o animal {dados_adocao['nome_animal']}, "
                                          f"portador do chip {dados_adocao['chip_animal']}, "
                                          f"e me comprometo a cuidar dele com responsabilidade, amor e carinho.")
        if resposta == "yes":
            return "s"
        else:
            return "n"        

    def deseja_cadastrar_adotante(self):
        resposta = messagebox.askquestion("Adotante não encontrado", "O adotante não existe, deseja cadastrar?")
        if resposta == "yes":
            return "s"
        else:
            return "n"

    def pega_dados_alteracao(self):     
        self.limpar_tela()
        dados = {}

        tk.Label(self.root, text=f"Alteração de Adoção", font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        labels = ["Alterar adotante (CPF): ", "Alterar animal (chip): "]
        campos = ["cpf", "animal"]

        for label, campo in zip(labels, campos):
            tk.Label(self.root, text=label, font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)
            entrada = tk.Entry(self.root, font=("Times New Roman", 12))
            entrada.pack(pady=5)
            dados[campo] = entrada 

        def confirmar():
            try: 
                for key, campo in dados.items():
                    valor = campo.get() if campo else None
                    dados[key] = valor

                if dados["cpf"] and (not dados["cpf"].isdigit() or len(dados["cpf"]) != 11) or not self.validar_numeros_cpf(dados["cpf"].get()):
                    raise CPFInvalidoException()
                
                if dados["animal"] and (not dados["animal"].isdigit() or len(dados["animal"]) != 7):
                    raise ChipInvalidoException()

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
    
    def exibir_dados_adocoes(self, lista_adocoes):
        self.limpar_tela()
        titulo = "Relatório de Adoções"
        tk.Label(self.root, text=titulo, font=("Times New Roman", 16), bg="#fdd9b9").pack(pady=10)

        # Criação do Treeview
        colunas = ("Data", "Animal", "Adotante", "Finalizado")
        tabela = ttk.Treeview(self.root, columns=colunas, show="headings", height=10)

        # Configurar cabeçalhos
        for coluna in colunas:
            tabela.heading(coluna, text=coluna)
            tabela.column(coluna, anchor="center", width=200)

        # Adicionar os dados à tabela
        for adocao in lista_adocoes:
            tabela.insert("", "end", values=(
                adocao["Data"],
                adocao["Animal"],
                adocao["Adotante"],
                "Sim" if adocao["Finalizado"] else "Não"))

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
