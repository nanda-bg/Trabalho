class CampoVaziosException(Exception):
    def __init__(self, campos):
        super().__init__(f"Os seguintes campos são obrigatórios: {', '.join(campos)}.")