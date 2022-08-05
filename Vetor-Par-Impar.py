# LABORATÓRIO DE PROGRAMAÇÃO
# Prova - Atividade 1
# Nome: Felippe de Abreu RA: 10482120920





# Funções

def geradordematriz(linha_total, coluna_total):
    matriz = []
    for numero_linha in range(linha_total):
        linha = []
        for numero_coluna in range(coluna_total):
            linha.append(0)
        matriz.append(linha)
    return matriz

def matriz_preenchida(matriz):
    for numero_linha in range(linha_total):
        for numero_coluna in range(coluna_total):
            matriz[numero_linha][numero_coluna] = random.randint(0, 1000)
    return matriz


def lista_de_par_e_impar(matriz):
    lista_par = []
    lista_impar = []
    par_impar = []
    for linhafor in range(len(matriz)):
        for colunafor in range(len(matriz[linhafor])):
            verifica = matriz[linhafor]
            linha = verifica[colunafor]
            teste = linha % 2
            if teste == 0:
                lista_par.append(linha)
                lista_par.sort()
            else:
                lista_impar.append(linha)
                lista_impar.sort()
            par_impar = lista_par + lista_impar
    return par_impar

def vetor_par_impar(vetor):
    lista_par = []
    lista_impar = []
    for i in range(len(vetor)):
        linha = vetor[i]
        teste = linha % 2
        if teste == 0:
            lista_par.append(linha)
            lista_par.sort()
        else:
            lista_impar.append(linha)
            lista_impar.sort()

    return lista_par, lista_impar

def temporizador():
    time.sleep(0.3)





# Inicio do Programa
import os
import random
import time


string = '\n * * * Vetor com pares e impares * * *'
print('{:^35}'.format(string))



continuar = True
while continuar == True:
    linha_total = input('Digite o número de linhas para a matriz: ')
    coluna_total = input('Digite o número de colunas para a matriz: ')
    # print('Tipo string linha total é: {}'.format(type(linha_total)))
    # print('Tipo string linha total é: {}'.format(type(coluna_total)))
    if linha_total.isnumeric() == True or coluna_total.isnumeric() == True:
        try:
            linha_total = int(linha_total)
            coluna_total = int(coluna_total)
            if linha_total == 0 or coluna_total == 0:
                print('Os números não podem ser zero!')
            else:
                continuar = False
                linha_total = int(linha_total)
                coluna_total = int(coluna_total)
                criar_matriz = geradordematriz(linha_total, coluna_total)
                preencher_matriz = matriz_preenchida(criar_matriz)

                vetor = lista_de_par_e_impar(preencher_matriz)
                vetor_par_impar = vetor_par_impar(vetor)
        except:
            print('Um dos números digitados contem letra!')

    else:
        print('Você não digitou números!')

temporizador()


string = '\n * * * Resultado * * *'
print('{:^35}'.format(string))


lista_vetor = str(vetor)[1:-1]
print('O vetor de retorno é: {}\n'.format(lista_vetor))


# Para os prints ficarem sem os colchetes do vetor =)
lista_num_par = str(vetor_par_impar[0])[1:-1]
lista_num_impar = str(vetor_par_impar[1])[1:-1]


if len(vetor_par_impar[0]) == 1:
    print('O número par do vetor é: {}'.format(lista_num_par))
if len(vetor_par_impar[0]) >= 2:
    print('Os números pares do vetor são: {}'.format(lista_num_par))
if len(vetor_par_impar[0]) == 0:
    print('Não há números pares.')

if len(vetor_par_impar[1]) == 1:
    print('O número ímpar do vetor é: {}'.format(lista_num_impar))
if len(vetor_par_impar[1]) >= 2:
    print('Os números ímpares do vetor são: {}'.format(lista_num_impar))
if len(vetor_par_impar[1]) == 0:
    print('Não há números ímpares.')

os.system("pause")