# LABORATÓRIO DE PROGRAMAÇÃO
# Atividade 2 - Exercicio 1
# Nome: Felippe de Abreu RA: 10482120920

import os

# Funções
def iniciasdonome(nome):
    nome = nome.upper()
    nome = nome.lstrip()
    nome = nome.rstrip()
    lista_nome = []
    lista_nome = nome.split()

    # mesmo nao concordando que o DE não faz parte do nome, terei de colocar

    i = 0
    while i in range(len(lista_nome)):
        if (lista_nome[i] == 'E') or (lista_nome[i] == 'DO') or (lista_nome[i] == 'DA') or (lista_nome[i] == 'DOS') or (lista_nome[i] == 'DAS') or (lista_nome[i] == 'DE') or (lista_nome[i] == 'DI') or (lista_nome[i] == 'DU'):
            lista_nome.remove(lista_nome[i])
        else:
            i += 1

    variavel = ''
    letrainicial = ''
    for i in range(len(lista_nome)):
        letra = lista_nome[i]
        for i in range(len(letra)):
            letrainicial = letra[0]
        variavel = variavel + letrainicial
    return variavel

# Começo do codigo

iniciais = ''
nome = 'a'


string = ' * * * Verificador de Letras Iniciais * * *'
print('{:^60}'.format(string))
print('Digite ''dione'' para preencher automaticamente com: Dione Jonathan Ferrari\nOu ''desenvolvedor'' para preencher automaticamente com: Felippe de Abreu')
print('Lembrando que ''"e do da dos das de di du"'' serão removidos pois são conectores')
while nome == 'a':
    nome = str(input('Digite seu nome completo: '))
    if nome == '':
        print('Você não digitou nada...')
        nome = 'a'
    if nome.isnumeric() == True:
        print('Você digitou números!')
        nome = 'a'
    if nome == 'dione':
        print('Preenchendo automaticamente com: Dione Jonathan Ferrari')
        nome = 'Dione Jonathan Ferrari'
        iniciais = iniciasdonome(nome)
    if nome == 'desenvolvedor':
        print('Preenchendo automaticamente com: Felippe de Abreu')
        nome = 'Felippe de Abreu'
        iniciais = iniciasdonome(nome)
    else:
        iniciais = iniciasdonome(nome)
print('\n')
string = '* * * Resultado * * *'
print('{:^60}'.format(string))

print('As iniciais do seu nome são: {}'.format(iniciais))
print('\n')

os.system("pause")