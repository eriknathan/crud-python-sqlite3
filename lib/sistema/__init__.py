import database
import time

from lib.interface import cabecalho, limpa_tela
from lib.interface.menu import menu

from lib.sistema.casdastrar_pessoa import cadastrar_pessoa
from lib.sistema.excluir_pessoa import excluir_pessoa
from lib.sistema.listar_pessoa import listar_pessoa
from lib.sistema.editar_pessoa import editar_pessoa


def sistema():
    database.connect_database()
    while True:
        cabecalho('MENU PRINCIPAL')
        opcao = menu([
            'Ver pessoas cadastradas',
            'Cadastrar Pessoas',
            'Editar Pessoas',
            'Excluir Pessoas',
            'Sair do Sistema'])

        if opcao == 1:
            limpa_tela()
            listar_pessoa()
        elif opcao == 2:
            limpa_tela()
            cadastrar_pessoa()
        elif opcao == 3:
            limpa_tela()
            listar_pessoa()
            editar_pessoa()
        elif opcao == 4:
            limpa_tela()
            listar_pessoa()
            excluir_pessoa()
        elif opcao == 5:
            limpa_tela()
            cabecalho("ATÉ LOGO!")
            print('Saindo do sistema...')
            time.sleep(1.5)
            break
        else:
            print('\033[31mERRO! Digite uma opção válida!\033[m')
