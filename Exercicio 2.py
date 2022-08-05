def geraMatriz(lin, col):
    matriz = []
    for l in range(lin):
        linha = []
        for c in range(col):
            linha.append(0)
        matriz.append(linha)
    return matriz


def preencherMatriz(matriz):
    from random import randint
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            matriz[l][c] = randint(0, 100)
    return matriz


def geraListaParImpar(matriz):
    par = []
    impar = []
    parimpar = []
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            verifica = matriz[l]
            linha = verifica[c]
            teste = linha % 2
            if teste == 0:
                par.append(linha)
                par.sort()
            else:
                impar.append(linha)
                impar.sort()
            parimpar = par + impar
    return parimpar


l = int(input('Informe o número de linhas: '))   # Recebe dados do usuário.
c = int(input('Informe o número de colunas: '))
matVazia = geraMatriz(l, c)                      # Modulo de gerar matriz com dados do usuário.

matPreenchida = preencherMatriz(matVazia)        # Preenche a matriz com dados aleatórios.
print('\nMatriz gerada:', matPreenchida)

vetor = geraListaParImpar(matPreenchida)         # Gera lista de números pares e impares.
print('\nVetor de retorno: {}'.format(vetor))
input('Aperte ENTER para finalizar...')
