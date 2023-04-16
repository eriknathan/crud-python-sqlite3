from lib.interface import cabecalho
from database.cadastro import cadastro


def cadastrar_pessoa():
    cabecalho("CADASTRAR DE PESSOA")
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade: "))
    cadastro(nome, idade)
