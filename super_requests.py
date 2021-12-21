import requests
token = 'sdfsdfsdfs'

def post_ia(dados):
    urlzao = ''
    header = {'Authorization':f'Bearer {token}'}

    r = requests.post(urlzao, dados, headers=header)

    return r