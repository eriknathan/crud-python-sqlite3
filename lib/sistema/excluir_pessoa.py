import time

from lib.interface import cabecalho
from database.excluir import excluir


def excluir_pessoa():
    cabecalho("EXCLUIR PESSOA")

    id = int(input("Digite o ID da pessoa que deseja editar: "))
    excluir(id)

    time.sleep(1)
    print(f'A pessoa excluída com sucesso!')
