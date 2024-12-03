<<<<<<< HEAD
from controlador.controlador_sistema import SistemaPessoas
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    sistema = SistemaPessoas(root)
=======
from controlador.controlador_sistema import Sistema


if __name__ == "__main__":
    sistema = Sistema()
>>>>>>> fe247162b184adc695bdcbc1f718b2acf5d14169
    sistema.inicializa_sistema()