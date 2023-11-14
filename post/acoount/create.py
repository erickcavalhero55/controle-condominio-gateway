import requests
from flask_restful import Resource, reqparse

class Usuario(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument('nome')
    argumentos.add_argument('sobrenome')
    argumentos.add_argument('rg')
    argumentos.add_argument('cpf')
    argumentos.add_argument('telefone')
    argumentos.add_argument('celular')
    argumentos.add_argument('email')
    argumentos.add_argument('genero')

def post(self, id):

  #  dados = Usuario.argumentos.parse_args()
  #  url = 'http://54.167.214.72/usuario/3'

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

    # Exemplo de uso:
    cpf = "123.456.789-09"
    if valida_cpf(cpf):
        print("CPF válido")
    else:
        print("CPF inválido")
    import re


    def validar_rg(rg):

        padrao = r'^\d{2}\.\d{3}\.\d{3}-\d{1}$'

        if re.match(padrao, rg):

            return True
        else:
            return False

    # Exemplo de uso
    rg = "12.345.678-9"
    if validar_rg(rg):
        print(f"RG {rg} é válido.")
    else:
        print(f"RG {rg} não é válido.")



#response = requests.post(url=url, dados=dados)

    #if response.status_code >= 200 and response.status_code <= 299:

        #return (response.status_code, response.json())

    #else:
        #return (response.status_code)
