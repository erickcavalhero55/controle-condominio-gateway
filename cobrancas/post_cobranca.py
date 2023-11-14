import requests

url = 'http://54.167.214.72/cobranca/2'

user_cobranca = {

    "cod_barras": "3200000",
    "data_vencimento": "2013-05-15",
    "data_pagamento": "2013-05-15",
    "valor": "90",
    "titulo": "320",
    "observacao": "2013-01-22",
    "juros": "150",
    "multa": "90",
    "desconto": "150",
    "total": "90",
    "id_usuarios": "1"

}

response = requests.post(url=url, json=user_cobranca)


if response.status_code >= 200 and response.status_code <= 299:

    print(response.status_code)
    print(response.reason)
    print(response.json())
else:
    print(response.status_code)
    print(response.reason)







