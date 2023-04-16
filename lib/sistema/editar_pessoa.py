from lib.interface import cabecalho
from database.editar import editar


def editar_pessoa():
    cabecalho("EDITAR PESSOA")
    id = int(input("Digite o ID da pessoa que deseja editar: "))
    nome = input("Digite o novo nome da pessoa: ")
    idade = int(input("Digite a nova idade da pessoa: "))
    editar(id,nome, idade)
