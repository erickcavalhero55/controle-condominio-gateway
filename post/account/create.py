import requests
from flask_restful import Resource, reqparse

from utils.validations import valida_cpf, validar_rg, limpa_caracteres, validar_nome, validar_sobrenome, validar_telefone, validar_celular, validar_email


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

    def post(self):
        dados = Usuario.argumentos.parse_args()
        url = 'http://54.167.214.72/usuario/-'

        try:
            dados['cpf'] = limpa_caracteres(dados['cpf'])
            if not valida_cpf(dados['cpf']):
                raise Exception("CPF inválido")

            dados['rg'] = limpa_caracteres(dados['rg'])
            if not validar_rg(dados['rg']):
                raise Exception("RG inválido")

            dados['nome'] = limpa_caracteres(dados['nome'])
            if not validar_nome(dados['nome']):
                raise Exception("Nome inválido")

            dados['sobrenome'] = limpa_caracteres(dados['sobrenome'])
            if not validar_sobrenome(dados['sobrenome']):
                raise Exception('Sobrenome inválido')

            dados['telefone'] = limpa_caracteres(dados['telefone'])
            if not  validar_telefone(dados['telefone']):
                raise Exception('Telefone inválido')

            dados['celular'] = limpa_caracteres(dados['celular'])
            if not validar_celular(dados['celular']):
                raise Exception('Celular inválido')

            dados['email'] = limpa_caracteres(dados['email'])
            if not validar_email(dados['email']):
                raise Exception('Email inválido')


        except Exception as e:
            return {
                "message": str(e),
                "code": "INVALID_DATA"
            }, 400

        response = requests.post(url=url, json=dados)

        if 200 <= response.status_code <= 299:
            return response.json(), response.status_code
        else:
            return response.json(), response.status_code
