import time

from lib.interface import cabecalho, linha, limpa_tela
from database.editar import editar, editar_nome, editar_idade
from lib.interface.menu import menu


def editar_pessoa():

    cabecalho("EDITAR PESSOA")
    id = int(input("Digite o ID da pessoa que deseja editar: "))
    linha()
    print('Você deseja editar: ')
    opcao = menu([
        'Nome',
        'Idade',
        'Ambos'])
    linha()

    if opcao == 1:
        nome = str(input('Digite o nome nome: '))
        editar_nome(id, nome)
        time.sleep(1)
        print('Nome atualizado com sucesso! ')
        time.sleep(2)
        limpa_tela()
    elif opcao == 2:
        idade = input('Digite a nova idade: ')
        editar_idade(id, idade)
        time.sleep(1)
        print('Idade atualizada com sucesso! ')
        time.sleep(2)
        limpa_tela()
    elif opcao == 3:
        nome = input("Digite o novo nome da pessoa: ")
        idade = int(input("Digite a nova idade da pessoa: "))
        editar(id,nome, idade)
        time.sleep(1)
        print('Pessoa atualizada com sucesso! ')
        time.sleep(2)
        limpa_tela()
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
