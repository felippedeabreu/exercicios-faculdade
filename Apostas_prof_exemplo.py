
import random

def lerInteiroPositivo():
    num = 0
    while num <= 0:
        try:
            num = int(input('Digite um valor inteiro positivo:'))
        except:
            print('Valor digitado é inválido.')
    return num


def estaNoVetor(numero, vetor):
    achou = False
    for i in range(len(vetor)):
        if numero == vetor[i]:
            achou = True
    return achou


def geraAposta(qtde):
    aposta = []
    for i in range(qtde):
        while True:
            numSorteado = random.randint(1, 60)
            if numSorteado not in aposta:
                aposta.append(numSorteado)
                break
    return sorted(aposta)

# Método retorna vetor com 6 números vencedores da Megasena
def geraMegasena():
    numVencedores = geraAposta(6)
    return numVencedores

def mostraMegasena(vetor):
    print('\nNúmeros sorteados na Megasena:')
    for i in range(len(vetor)):
        print('[', vetor[i], '] ', end='')

def mostraAposta(vetor):
    print('\nNúmeros da Aposta:')
    for i in range(len(vetor)):
        print('(', vetor[i], ') ', end='')

def verificaAposta(aposta, numMegasena):
    Acertos = []
    for i in range(len(aposta)):
        if aposta[i] in numMegasena:
            Acertos.append(aposta[i])
    return Acertos

# Código principal

print('Digite o número de apostas:')
qtdeApostas = lerInteiroPositivo()

print('Digite a quantidade de números por aposta')
qtdeNumAposta = lerInteiroPositivo()

print('Você vai fazer', qtdeApostas, 'jogos de', qtdeNumAposta, 'números por jogo')

numPremiados = geraMegasena()
vetorApostas = []
for i in range(qtdeApostas):
    umaAposta = geraAposta(qtdeNumAposta)
    vetorApostas.append(umaAposta)

for i in range(len(vetorApostas)):
    umaAposta = vetorApostas[i]
    mostraAposta(umaAposta)
    acertos = verificaAposta(umaAposta, numPremiados)
    print('Número de acertos: ', len(acertos))
    if (len(acertos) > 0):
        print('Número premiados da Aposta: ', acertos)


#valor = lerInteiroPositivo()
#print(valor)
#print('\n')
#aposta1 = geraAposta(10)
#mostraAposta(aposta1)
#print('\n')
#numMegasena = geraMegasena()
#mostraMegasena(numMegasena)

#acertos = verificaAposta(aposta1, numMegasena)
