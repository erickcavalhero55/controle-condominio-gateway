import re
from validate_email_address import validate_email


def limpa_caracteres(str):
    return re.sub(r'\W', '', str)

def valida_cpf(cpf):
    # Remove caracteres não numéricos
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    # Calcula o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    # Calcula o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto

    # Verifica se os dígitos verificadores são iguais aos dígitos fornecidos
    if int(cpf[9]) == digito1 and int(cpf[10]) == digito2:
        return True
    else:
        return False


def validar_rg(rg):
    # Remove caracteres não alfanuméricos
    rg_alnum = re.sub(r'\W', '', rg)

    # Verifica se o RG tem o formato esperado
    if not re.match(r'^\d{8}[A-Za-z0-9]$', rg_alnum):
        return False

    # Obtém os oito primeiros dígitos
    digitos_rg = [int(digito) if digito.isdigit() else ord(digito.upper()) - ord('A') + 10 for digito in rg_alnum[:-1]]

    # Obtém o dígito verificador fornecido
    digito_verificador_fornecido = rg_alnum[-1].upper()

    # Calcula o dígito verificador esperado
    soma = sum(d * (9 - i) for i, d in enumerate(digitos_rg))
    resto = soma % 11
    digito_verificador_esperado = 'X' if resto == 10 else str(resto)

    # Verifica se o dígito verificador fornecido é válido
    return digito_verificador_fornecido == digito_verificador_esperado


def validar_nome(nome):
    # Verifica se o nome tem pelo menos 2 caracteres
    if len(nome) < 2:
        return False

    # Verifica se o nome contém apenas letras e espaços
    if not re.match("^[a-zA-Z\s]*$", nome):
        return False

    # Se todas as condições forem atendidas, o nome é válido
    return True


def validar_sobrenome(sobrenome):
    # Verifica se o sobrenome tem pelo menos 2 caracteres
    if len(sobrenome) < 2:
        return False

    # Verifica se o sobrenome contém apenas letras e espaços
    if not re.match("^[a-zA-Z\s]*$", sobrenome):
        return False

    # Se todas as condições forem atendidas, o sobrenome é válido
    return True


def validar_telefone(numero):
    # Remove todos os caracteres que não são dígitos
    numero = re.sub(r'\D', '', numero)

    # Verifica se o número tem 11 dígitos (formato típico de um número de telefone brasileiro)
    if len(numero) != 11:
        return False

    # Se todas as condições forem atendidas, o número de telefone é válido
    return True


def validar_celular(numero):
    # Remove todos os caracteres que não são dígitos
    numero = re.sub(r'\D', '', numero)

    # Verifica se o número tem 11 dígitos (formato típico de um número de celular brasileiro)
    if len(numero) != 11:
        return False

    # Verifica se o número começa com 9 (indicativo de número de celular no Brasil)
    if not re.match(r'^11', numero):
        return False

    # Se todas as condições forem atendidas, o número de celular é válido
    return True


def validar_email(email):
    try:
        validate_email(email, verify=True)
        return True
    except ValueError:
        return False

def validar_genero(genero):
    generos_validos = ['masculino', 'feminino']

    # Converte para minúsculas para facilitar a comparação
    genero = genero.lower()

    # Verifica se o gênero está na lista de gêneros válidos
    if genero in generos_validos:
        return True
    else:
        return False

