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


def exibirPorcentagem(matriz):
    par = 0
    impar = 0
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            verifica = matriz[l]
            linha = verifica[c]
            teste = linha % 2
            if teste == 0:
                par += 1
            else:
                impar += 1
            if (par + impar) == len(matriz[l]):
                print('\nLinha {}: {} números PARES e {} números ÍMPARES.'.format(l, par, impar))
                print('Linha {}: {:.0f}% de PARES e {:.0f}% de ÍMPARES\n'.format(l, (par / (par + impar) * 100), (impar / (par + impar) * 100)))
                par = 0
                impar = 0

                                            
l = int(input('Informe o número de linhas: '))   # Recebe dados do usuário.
c = int(input('Informe o número de colunas: '))
matVazia = geraMatriz(l, c)                      # Modulo de gerar matriz com dados do usuário.

matPreenchida = preencherMatriz(matVazia)        # Preenche a matriz com dados aleatórios
print('\nMatriz gerada:', matPreenchida)

exibirPorcentagem(matPreenchida)                 # Chama o modulo de exibir números pares e impares e porcentagem.




