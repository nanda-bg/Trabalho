import tkinter as tk
from tkinter import messagebox

class TelaSistema:
    def __init__(self, root):
        self.root = root
        self.root.title("Tela Sistema")
        self.root.geometry("400x600")
        self.root.configure(bg="#fdd9b9") 
        self.opcao_selecionada = None
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="TELA SISTEMA", font=("Times New Roman", 14), bg="#fdd9b9").pack(pady=10)
        tk.Label(self.root, text="Escolha uma opção:", font=("Times New Roman", 12), bg="#fdd9b9").pack(pady=5)

        options = [
            ("Ir para tela de Pessoas", 1),
            ("Ir para tela de Animais", 2),
            ("Ir para tela de Adoção", 3),
            ("Ir para tela de Doação", 4),
            ("Finalizar sistema", 0)
        ]

        for text, value in options:
            button = tk.Button(
                self.root,
                text=text,
                command=lambda v=value: self.set_opcao(v),
                font=("Times New Roman", 10),
                bg="#ff7e0e",
                fg="white",
                width=30
            )

            button.bind("<Enter>", lambda event, b=button: b.config(bg="#eb6c00"))
            button.bind("<Leave>", lambda event, b=button: b.config(bg="#eb6c00")) 
            button.pack(pady=5)

    def set_opcao(self, opcao):
        self.opcao_selecionada = opcao
        self.root.quit()

    def limpar_tela(self):
        """Remove todos os widgets da janela."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def mostra_tela(self):
        self.limpar_tela()
        self.create_widgets()
        self.opcao_selecionada = None
        self.root.mainloop()
        return self.opcao_selecionada
