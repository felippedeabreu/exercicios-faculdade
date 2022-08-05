# FELIPPE DE ABREU
# RA 10482120920

import random
import os

#Funções
def sortear_palavra(lista_palavras):
    # PARA TESTE
    #num_sorteio = random.randint(0, 0)
    # FIM DO TESTE
    num_sorteio = random.randint(0,22)
    palavra_sorteada = lista_palavras[num_sorteio]
    #print('-------- Numero sorteado da lista foi: {}'.format(num_sorteio))
    #print('A palavra sorteada foi: {}'.format(palavra_sorteada))
    return palavra_sorteada

def embaralhar(palavra):
    palavra_embaralhada = random.sample(palavra, len(palavra))
    #print('A palavra embaralhada é: {}'.format(palavra_embaralhada))
    palavra_embaralhada_arrumada = ' - '.join(palavra_embaralhada)

    return palavra_embaralhada_arrumada

def jogada(palavra_certa):
    #teste
    #print('a palavra é: {}'.format(palavra_certa))
    print('Agora você terá seis tentativas para acertar a palavra!\n')

    tentativa = 1
    while tentativa <= 6:
        palavra = input(str('{}ª tentativa - Digite a palavra que você acredita que seja a correta: '.format(tentativa)))

        if palavra == palavra_certa:
            #print('Boa! Tu acertou na {}ª tentativa!'.format(tentativa))
            return (True)
        if tentativa == 5:
            print('Você errou a palavra... você ainda tem mais uma tentiva!\n')
            tentativa += 1
        else:
            if tentativa != 6:
                print('Você errou a palavra... você ainda tem mais {} tentivas!\n'.format(6 - tentativa))
                tentativa += 1
            else:
                tentativa += 1
                return False


#Começo do código
msg_inicial = 'Jogo de palavras embaralhadas!'
print('*=' * 24)
print('{:^40}'.format(msg_inicial))
print('*=' * 24)
lista_palavras = ['teclado', 'mouse', 'camiseta', 'monitor', 'cobertor', 'estabilizador', 'caneta', 'calça', 'travesseiro',
            'ventilador', 'impressora', 'porta', 'bandeira', 'banheiro', 'jogador', 'armário', 'espelho', 'creme', 'gaveta', 'almoço', 'notebook', 'festa', 'prateleira']

# PARA TESTE DE DESENVOLVIMENTO
#lista_palavras = ['café']
# FIM DO TESTE

palavra = sortear_palavra(lista_palavras)
palavra_embaralhada = embaralhar(palavra)

print('A palavra embaralhada que você deve descobrir é:\n\n >>>{:^40}<<<\n'.format(palavra_embaralhada))
print('*=' * 24)

#resultado retornará true ou false
resultado = jogada(palavra)


if resultado != True:
    ruim = 'Acabaram suas chances... Você perdeu!'
    pala = 'A palavra correta era: {}'.format(palavra)
    print('*=' * 24)
    print('\n')
    print('{:^48}'.format(ruim))
    print('{:^48}'.format(pala))
    print('\n')
    print('*=' * 24)
else:
    print('*=' * 24)
    print('\n')
    boa = 'Boa! Você acertou!'
    print('{:^48}'.format(boa))
    print('\n')
    print('*=' * 24)
os.system("pause")
