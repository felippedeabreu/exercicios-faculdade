# # Parte 01
# lista = [22,'Algoritmos',1.89,"EAD"]
# print(lista)
# lista2 = list(range(5,20,3)) # (valor inicial inclusive, valor final excluso, incremento)
# print(lista2[2:])
# for elem in lista2: # a variável elem se torna um elemento da lista2
#     print(elem, end=' - ') # para exibir todos os elementos na mesma linha
# # OU
# print('')
# #for i in range(0,len(lista2),1): # a variável i se torna apenas um índice da lista2
# for i in range(len(lista2)):
#     print(lista2[i], end=' - ')

# Parte 2 - usar métodos com listas
# l_alunos = []
# l_alunos.append('Giovanni')
# l_alunos.append('Mirella')
# l_alunos.append('Gustavo')
# l_alunos.append('Thabata')
# l_alunos.insert(1,'João Marcelo')
# l_alunos.extend(['Alexandre', 'Felippe', 'Cristina'])
# #l_alunos.sort()
# print(l_alunos)
# # comando para proteger o nosso programa de travar!!
# l_alunos.pop(2)
# try:
#     l_alunos.remove('Mirella')
#     l_alunos.remove('Maria')
# except:
#     print('O aluno não foi encontrado na lista!! Não foi possível excluir...')
# print(l_alunos)
# print('A aluna Thabata está na posição de índice: ',
#             l_alunos.index('Thabata'))
# if 'Alexandre' in l_alunos:
#     print('Alexandre está na lista!!')
# else:
#     print('Alexandre não está na lista!!')

# Parte 3 - Tuplas
# meses = ('janeiro', 'fevereiro', 'março', 'abril')
# # meses.append('abril')  --> gera um erro!!
# print(meses[2])

# # Parte 4 - Dicionários
# amigo = {} # criou um dicionário vazio
# amigo['nome'] = 'Maurício'
# amigo['idade'] = 33
# amigo['sexo'] = 'M'
# print(amigo)
# l_amigos = []
# l_amigos.append(amigo)
# print(l_amigos)
# amigo2 = {}
# amigo2['nome'] = 'Aran'
# amigo2['idade'] = 21
# amigo2['sexo'] = 'M'
# l_amigos.append(amigo2)
# l_amigos.append({'nome':'João','idade':19,'sexo':'M'})
# print(l_amigos)
# print(amigo.values())
# for elem in l_amigos:
#     print(elem['nome'], 'tem', elem['idade'], 'anos!!')


# Parte 5 - Matrizes
lin = 3 # primeiro item de índice
col = 4 # segundo item de índice
matriz = [] # é uma lista normal, que em cada posição terá uma nova lista
for l in range(lin):
    linMatriz = [] # criando uma nova lista para representar as colunas da matriz
    for c in range(col):
        linMatriz.append((c+1)*l)
    matriz.append(linMatriz)
print(matriz)
print(matriz[1][2]) # Exibir o número 3
matriz[2][2] = 66
for linMatriz in matriz:
    print(linMatriz)