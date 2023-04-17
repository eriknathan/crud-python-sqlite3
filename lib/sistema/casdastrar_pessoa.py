import time

from lib.interface import cabecalho, linha
from database.cadastro import cadastro


def cadastrar_pessoa():
    cabecalho("CADASTRAR DE PESSOA")
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    cadastro(nome, idade)
    linha()
    time.sleep(1)
    print('Pessoa cadastrada com sucesso!')
    time.sleep(2)
