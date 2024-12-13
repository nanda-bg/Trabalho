from abc import ABC


class AbstractTela(ABC):
    def __init__(self):
        super().__init__()

    def validar_numeros_cpf(self, cpf):
        # Limpa o cpf para deixar apenas os números
        cpf = cpf.replace('.', '').replace('-', '')

        # Verifica se o CPF tem 11 dígitos
        if len(cpf) != 11 or not cpf.isdigit():
            return False

        # Verifica se todos os dígitos são iguais
        if len(set(cpf)) == 1:
            return False

        # Calcula o primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = soma % 11
        digito_1 = 0 if resto < 2 else 11 - resto

        # Verifica o primeiro dígito verificador
        if int(cpf[9]) != digito_1:
            return False

        # Calcula o segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = soma % 11
        digito_2 = 0 if resto < 2 else 11 - resto

        # Verifica o segundo dígito verificador
        if int(cpf[10]) != digito_2:
            return False
        
        return True             