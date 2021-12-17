import requests


def post_ia(dados):
    urlzao = ''
    header = {'ver':'qual e'}

    r = requests.post(urlzao, dados, headers=header)

    return r