import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime
from view.tela_sistema import TelaSistema

class TelaDoador:
    def __init__(self, master):
        self.root = master
        self.root.title("Cadastro de Doador")
        self.root.geometry("400x600")
        self.root.configure(bg="#fdd9b9")
        self.create_widgets()

    def create_widgets(self):
        tk.Label(
            self.root,
            text="Cadastro de Doador",
            font=("Times New Roman", 14),
            bg="#fdd9b9"
        ).pack(pady=10)

        # CPF
        self.cpf_label = tk.Label(
            self.root, 
            text="CPF (somente números)", 
            font=("Times New Roman", 12), 
            bg="#fdd9b9"
        )
        self.cpf_label.pack(pady=5)
        self.cpf_entry = tk.Entry(self.root, font=("Times New Roman", 12))
        self.cpf_entry.pack(pady=5)

        # Nome
        self.nome_label = tk.Label(
            self.root, 
            text="Nome completo", 
            font=("Times New Roman", 12), 
            bg="#fdd9b9"
        )
        self.nome_label.pack(pady=5)
        self.nome_entry = tk.Entry(self.root, font=("Times New Roman", 12))
        self.nome_entry.pack(pady=5)

        # Data de nascimento
        self.data_nasc_label = tk.Label(
            self.root, 
            text="Data de nascimento (AAAA-MM-DD)", 
            font=("Times New Roman", 12), 
            bg="#fdd9b9"
        )
        self.data_nasc_label.pack(pady=5)
        self.data_nasc_entry = tk.Entry(self.root, font=("Times New Roman", 12))
        self.data_nasc_entry.pack(pady=5)

        # Endereço
        self.endereco_label = tk.Label(
            self.root, 
            text="Endereço", 
            font=("Times New Roman", 12), 
            bg="#fdd9b9"
        )
        self.endereco_label.pack(pady=5)
        self.endereco_entry = tk.Entry(self.root, font=("Times New Roman", 12))
        self.endereco_entry.pack(pady=5)

        # Botão de Salvar
        self.salvar_button = tk.Button(
            self.root,
            text="Salvar",
            command=self.pega_dados_doador,
            font=("Times New Roman", 12),
            bg="#ff7e0e",
            fg="white",
            width=30
        )
        self.salvar_button.pack(pady=20)

    def pega_dados_doador(self):
        cpf = self.valida_cpf()
        nome = self.valida_nome()
        data_nascimento = self.valida_data_nascimento()
        endereco = self.valida_endereco()

        # Se alguma validação falhar (ou seja, alguma variável for None), não exibe a mensagem de sucesso
        if None in [cpf, nome, data_nascimento, endereco]:
            return  # Impede a exibição da mensagem de sucesso se houver erro

        # Exibe os dados no console para fins de demonstração
        print({
            "cpf": cpf,
            "nome": nome,
            "data_nascimento": data_nascimento,
            "endereco": endereco,
        })

        # Exibe mensagem de sucesso
        messagebox.showinfo("Sucesso", "Dados do doador cadastrados com sucesso!")

        if self.voltar_callback:
            self.voltar_callback()

    def voltar_callback(self):
        self.limpar_tela()
        TelaSistema(self.root).set_opcao(1)

    def valida_cpf(self):
        cpf = self.cpf_entry.get()
        if re.match(r'^\d{11}$', cpf):
            return cpf
        else:
            messagebox.showerror("Erro", "CPF inválido. Digite um CPF válido com 11 números.")
            return None

    def valida_nome(self):
        nome = self.nome_entry.get()
        if len(nome.strip()) < 3:
            messagebox.showerror("Erro", "Nome inválido. O nome deve ter pelo menos 3 caracteres.")
            return None
        return nome

    def valida_data_nascimento(self):
        data_nascimento = self.data_nasc_entry.get()
        try:
            datetime.strptime(data_nascimento, "%Y-%m-%d")
            return data_nascimento
        except ValueError:
            messagebox.showerror("Erro", "Data inválida. O formato correto é AAAA-MM-DD.")
            return None

    def valida_endereco(self):
        endereco = self.endereco_entry.get()
        if len(endereco.strip()) < 3:
            messagebox.showerror("Erro", "Endereço inválido. O endereço deve ter pelo menos 3 caracteres.")
            return None
        return endereco

    def limpar_tela(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()    

    def mostrar_tela(self):
        self.limpar_tela()
        self.create_widgets()
        self.root.mainloop()
