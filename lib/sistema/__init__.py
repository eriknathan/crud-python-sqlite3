import database
from lib.interface import cabecalho
from lib.interface.menu import menu

from lib.sistema.casdastrar_pessoa import cadastrar_pessoa
from lib.sistema.listar_pessoa import listar_pessoa

import time


def sistema():
    database.connect_database()
    while True:
        opcao = menu([
            'Ver pessoas cadastradas',
            'Cadastrar Pessoas',
            'Editar Pessoas',
            'Excluir Pessoas',
            'Sair do Sistema'])

        if opcao == 1:
            listar_pessoa()
        elif opcao == 2:
            cadastrar_pessoa()
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            cabecalho("ATÉ LOGO!")
            print('Saindo do sistema...')
            time.sleep(1.5)
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
