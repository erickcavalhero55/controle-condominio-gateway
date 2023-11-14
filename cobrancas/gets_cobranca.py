import requests

url = 'http://54.167.214.72/cobrancas'

user_cobranca = {

}


def get(self):
    response = requests.get(url=url, json=user_cobranca)

    if response.status_code >= 200 and response.status_code <= 299:

        response.status_code
        response.reason
        (response.json())
    else:
        (response.status_code)
        (response.reason)

    response = requests.fetchone()


    return requests(response)

