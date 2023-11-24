import requests
from flask_restful import Resource, reqparse

from utils.validations import valida_cpf, validar_rg, limpa_caracteres


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
