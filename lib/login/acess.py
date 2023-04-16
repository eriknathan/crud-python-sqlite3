from lib.interface import cabecalho, linha
from getpass import getpass
from lib.sistema import sistema
import time


usuario_correto = 'admin'
senha_correta = 'admin'


def fazerLogin():
    cabecalho('ENTRAR NO SISETEMA')
    login = str(input('- Login: '))
    password = getpass('- Senha: ')
    if login == usuario_correto and password == senha_correta:
        linha()
        print('Acessando sistema...')
        time.sleep(2)
        sistema()
    else:
        print('Acesso Negado!')
        return fazerLogin()
