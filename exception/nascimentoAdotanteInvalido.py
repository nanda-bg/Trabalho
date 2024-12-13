class NascimentoAdotanteInvalidoException(Exception):
    def __init__(self):
        super().__init__("Adotantes devem ter pelo menos 18 anos.")