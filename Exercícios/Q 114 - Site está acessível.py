import requests


def checkinternet():
    url = 'http://www.pudim.com.br/'
    timeout = 5
    try:
        requests.get(url, timeout=timeout)
        requests.get(url)
    except requests.exceptions.ConnectionError:
        print('Não foi possível acessar o site do Pudim!')
        return False
    else:
        print('Consegui acessar o site do Pudim!')
        return True


checkinternet()
