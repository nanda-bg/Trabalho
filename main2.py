from controlador.controlador_sistema import SistemaPessoas
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    sistema = SistemaPessoas(root)
    sistema.inicializa_sistema()