# Atividade 4 - Manipulação de arquivos
# Nome: Felippe de Abreu RA: 10482120920

import time
import os


# Funções

def criartxt():
    arquivo = open('notas_estudantes.dat', 'w')
    arquivo.write('jose 10 5 2 3 4\n')
    arquivo.write('pedro 3 6 9 2\n')
    arquivo.write('suzana 8 2 7 4 3 7 4 1 2 9 1 7\n')
    arquivo.write('gisela 2 8 2 5 6 7\n')
    arquivo.write('joao 4 3 5 7 6\n')
    arquivo.close()

def temporizador():
    time.sleep(0.3)

def temporizador2():
    time.sleep(3)

def aluno_cinco_notas(tamlista, nome):
    lista_5notas = []
    for i in range(len(notas)):
        linha_notas = notas[i] #aqui pega a linha do aluno ex jose 10 5 2 3 4 - posição 0
        aluno = linha_notas.split(' ') #separa cada item da linha na lista
        total_notas = len(aluno) -1 # tira o nome do aluno que esta na posição zero, pensei em colocar um pop() mas dai nao teria o nome do aluno =(
        if total_notas > 5:
            lista_5notas.append(aluno[0])
    nome = ', '.join(lista_5notas)
    tamlista = len(lista_5notas)
    return (tamlista, nome)


def media():
    nomealuno = []
    notaaluno = []
    nome = ''
    for i in range(len(notas)):
        linha = notas[i] # pega a linha inteira ex jose 10 5 2 3 4 - posição 0

        #print('linha {}'.format(linha))

        media = linha.split(' ') # separa a linha
        for i in range(len(media)):
            if i == 0:
                nomealuno.append(media[i])
                nome = ''.join(nomealuno)
            if i > 0:
                variavel = media[i]
                notaaluno.append(int(variavel))
                #print(notaaluno)
        media = sum(notaaluno) / len(notaaluno)
        conta = sum(notaaluno) % len(notaaluno)
        #print('media',media)
        #print('conta', conta)
        if conta == 0:
            print('{} teve média de {:.0f}'.format(nome, media))
        else:
            print('{} teve média de {:.1f}'.format(nome, media))
            #print('media é ')

        #print(contador)
        #print(aluno)
        notaaluno.clear()
        nomealuno.clear()
        temporizador()


def notamaior(): #basicamente um control c da função media
    nomealuno = []
    notaaluno = []
    nome = 'nada'
    for i in range(len(notas)):
        linha = notas[i]
        media = linha.split(' ')
        for i in range(len(media)):
            if i == 0:
                nomealuno.append(media[i])
                nome = ''.join(nomealuno)
            if i > 0:
                notaaluno.append(int(media[i]))
        #print(notaaluno)
        print('A maior nota de {} foi {}'.format(nome, (max(notaaluno))))
        notaaluno.clear()
        nomealuno.clear()
        temporizador()


def abrirarquivo():
    arquivodenotas = open('notas_estudantes.dat', 'r', encoding='utf-8')
    notas = arquivodenotas.readlines()
    # print(notas) # ok
    return (notas)




# Começo do código

atividade = 'Atividade 4 - Manipulação de arquivos'
print('*-*'* 23)
print('{:^59}'.format(atividade))
print('*-*'* 23)


try:
    arquivo = open("notas_estudantes.dat","r")
    print('Arquivo encontrado! Carregando para a memória. Aguarde.\n')
    temporizador()
except IOError:
    continuar = True
    while continuar == True:
        criararquivo = input(str('O arquivo não existe, deseja cria-lo? Digite S / N > '))
        criararquivo = criararquivo.upper()
        if criararquivo == 'S':
            criartxt()
            print('Criando o arquivo... aguarde!')
            temporizador()
            print('Arquivo criado!')
            continuar = False
        if criararquivo == 'N':
            print('\n')
            saindo = 'Fechando o sistema.'
            print('*-*' * 20)
            print('{:^59}'.format(saindo))
            print('*-*' * 20)
            temporizador2()
            break



notas = abrirarquivo()
nomes = ''
tamlista = 0
teste = aluno_cinco_notas(tamlista, nomes) # aquela gambiarra pra retornar 2 variaveis =)

if teste[0] == 1:
    print('Aluno com mais de cinco notas foi: {}\n'.format(teste[1]))
    # eu sei que isso aqui nunca será usado, porque no arquivo de exemplo sempre haverá 2 nomes, mas foi legal entender como é o
    #                                                                                     retorno de 2 variaveis da função
else:
        print('Alunos com mais de cinco notas foram: {}\n'.format(teste[1]))
        temporizador()

strmedia = ' * * * Médias * * *'
print('{:^20}'.format(strmedia))
media()

strmaior = '\n * * * Maiores notas * * *'
print('{:^35}'.format(strmaior))
notamaior()

os.system("pause")
