from lib.interface import cabecalho, linha
from database.listar import listar
import os


def listar_pessoa():
    cabecalho("PESSOAS CADASTRADAS")
    pessoas = listar()
    for pessoa in pessoas:
        print(f"ID: {pessoa[0]}{os.linesep}Nome: {pessoa[1]}{os.linesep}Idade: {pessoa[2]}{os.linesep}{linha()}")
