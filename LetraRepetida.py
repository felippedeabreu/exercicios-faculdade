# LABORATÓRIO DE PROGRAMAÇÃO
# Prova - Atividade 1
# Nome: Felippe de Abreu RA: 10482120920

# Funções
def verificar_duplicada(texto):
    dicionario = {}
    for char in texto:
        dicionario.setdefault(char, 0)
        dicionario[char] += 1
        if dicionario[char] == 2:
            return True
    return False

# Inicio do programa
import os

continuar = True
while continuar == True:
    texto = input('Escreva algo para verificar se há caracteres repetidos: ')
    texto = texto.lstrip()
    texto = texto.rstrip()
    if texto != '':
        if verificar_duplicada(texto) == True:
            continuar = False
            string = '\n * * * Resultado * * *'
            print('{:^35}'.format(string))
            print('Existem caracteres repetidos no texto que você escreveu!')
            # No PyCharm a cor do print abaixo funciona
            # Executando o py direto, não =(
            #print('{}Existem{} caracteres repetidos no texto que você escreveu!'.format('\033[32m','\033[0;0m'))
        else:
            continuar = False
            string = '\n * * * Resultado * * *'
            print('{:^35}'.format(string))
            print('Não existe caracter repetido no texto que você escreveu!')

            # No PyCharm a cor do print abaixo funciona
            # Executando o py direto, não =(
            #print('{}Não{} existe caracter repetido no texto que você escreveu!'.format('\033[31m','\033[0;0m'))
print('\n')
os.system("pause")

