import random
import os
import time

def temporizador():
    print('Aguarde... Rolando os dados.')
    time.sleep(0.5)
    print('Aguarde... Rolando os dados..')
    time.sleep(0.5)
    print('Aguarde... Rolando os dados...')
    time.sleep(0.5)

def rolar_dado():
    return random.randint(1, 6) + random.randint(1, 6)

def craps():
    print()
    jogada = 2
    ponto = 0
    num_dado = rolar_dado()
    temporizador()
    print("Soma dos dados lançados na 1ª jogada foi:",num_dado)
    if num_dado == 7 or num_dado == 11:
        print('Número natural, você ganhou!')
    elif num_dado == 2 or num_dado == 3 or num_dado == 12:
        print('CRAPS! você perdeu!')
    else:
        ponto = num_dado
        print('*'*43)
        if ponto != 0 and jogada >= 2:
            while num_dado != 7:
                temporizador()
                num_dado = rolar_dado()
                print('Soma dos dados lançados na {}ª jogada foi: {}'.format(jogada,num_dado))
                if num_dado != 7:
                    print('Seu ponto é: {}'.format(ponto))
                if num_dado == 7:
                    print('O número jogado foi 7, então você perdeu')
                    break
                if num_dado == ponto:
                    print('Parabéns! Você venceu!')
                    break
                jogada += 1
                ponto = num_dado

                print('*'*43)
print('-=' * 50)
print('O jogo consiste em jogar 2 dados simultâneos. Caso na primeira jogada o valor dos dados for 7 ou 11,\n'
      'você ganha já na primeira rodada! Caso você tire 2, 3 ou 12, dará CRAPS, e você perderá o jogo.\n')
print('Caso você tire 4, 5, 6, 8, 9 ou 10, você estará no "ponto". Seu objetivo agora, da segunda rodada em\n'
      'diante, é acertar duas vezes seguidas o mesmo número...')
print('Mas, caso você tire um número 7 neste percurso, você perderá!')
print('-=' * 50)
craps()
print()
print()
print()
os.system("pause")