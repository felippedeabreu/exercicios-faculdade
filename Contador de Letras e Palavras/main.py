# LABORATÓRIO DE PROGRAMAÇÃO
# Atividade 2 - Exercicio 2
# Nome: Felippe de Abreu RA: 10482120920

# Professor, sendo sincero: o programa esta fazendo o que pede, mandei tirar ! ? , . para contar as palavras,
# porem itens como = - @ # $ continuam a contar como palavras...
# Não contente com a situação e um "tempo" sobrando, pesquisei um codigo que retira os simbolos e implementei.
# Deixei minha antiga lógica falha para que o Sr pudesse vizualiza-la ok?

# Funções
def contadordecaracteres(texto):
    #print(texto)
    texto = texto.lstrip()
    texto = texto.rstrip()
    #print(texto)

    tirar_espaco = texto.replace(' ','')
    #print('texto sem espaço: {}'.format(tirar_espaco))
    texto = tirar_espaco
    #print('texto sem espaço: {}'.format(texto))

    tamanhotexto = len(texto)
    #print(tamanhotexto)
    return (tamanhotexto)

def quantidadedepalavras(texto):


    # Se comentar esse bloco e 'descomentar' o de baixo, funciona com os errinhos que comentei


    nova_string = re.sub(r"[^a-zA-Z0-9<>^áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ-]", " ", texto)

    #print('aaaaaaaa {}'.format(nova_string))
    variavel = nova_string.split()
    #print('print variavel: {}'.format(variavel))
    tamanhovar = len(variavel)
    #print('tamanho variavel: {}'.format(tamanhovar))


    # Antiga logica "falha"... enquanto fazia pensei em fazer um while mas teria que colocar todos os simbolos
    # e percorrer letra por letra, dei uma viajada boa...

    # print('texto dentro da quantidade de palavras: {}'.format(texto))
    # tirar_virgula = texto.replace(',', '')
    # print('texto sem virgula: {}'.format(tirar_virgula))
    # texto = tirar_virgula
    # print('texto sem a virgula: {}'.format(texto))
    #
    # tirar_exclamacao = texto.replace('!', '')
    # print('texto sem exclamação: {}'.format(tirar_exclamacao))
    # texto = tirar_exclamacao
    # print('texto sem exclamação: {}'.format(texto))
    #
    # tirar_interrogacao = texto.replace('?', '')
    # print('texto sem interrogacao: {}'.format(tirar_interrogacao))
    # texto = tirar_interrogacao
    # print('texto sem interrogacao: {}'.format(texto))
    #
    # tirar_ponto = texto.replace('.','')
    # print('texto sem ponto: {}'.format(tirar_ponto))
    # texto = tirar_ponto
    # print('texto sem ponto: {}'.format(texto))
    # variavel = texto.split()
    # print('print variavel: {}'.format(variavel))
    # tamanhovar = len(variavel)
    # print('tamanho variavel: {}'.format(tamanhovar))




    return tamanhovar



# Inicio do Programa
import os
import re



caracteres = 0
tamanhotexto = 0
texto = 'a'

string = ' * * * Contador de texto! * * *'
print('Este programa remove pontos, vírgulas, pontos de exclamação e pontos de interrogação ')
print('{:^60}'.format(string))
while texto == 'a':
    texto = str(input('Digite um texto: '))
    #texto = 'Felippe de Abreu . , @ # $ % '
    if texto == '':
        print('Você não digitou nada...')
        texto = 'a'
    else:
        quantidade_caracteres = contadordecaracteres(texto)
        quantidade_palavras = quantidadedepalavras(texto)
print('\n')
string = '* * * Resultado * * *'
print('{:^60}'.format(string))

print('No total, o texto digitado tem {} caracteres e {} palavras'.format(quantidade_caracteres, quantidade_palavras))
print('\n')

os.system("pause")

