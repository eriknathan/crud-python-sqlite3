from lib.interface import cabecalho
from getpass import getpass
import time

usuario_correto = 'admin'
senha_correta = 'admin'


def fazerLogin():
    cabecalho('ENTRAR NO SISETEMA')
    login = str(input('- Login: '))
    password = getpass('- Senha: ')
    if login == usuario_correto and password == senha_correta:
        print('Acessando sistema...')
        time.sleep(2)
        print('AQUI CHAMA O SISTEMA!!!!')
    else:
        print('Acesso Negado!')
        return fazerLogin()
