gostando = 'xyz'
sexo = 'sd'
mulher_gostando = 0
mulher_nao_gostando = 0
homem_gostando = 0
homem_nao_gostando = 0
gostando_sim = 0
gostando_nao = 0
homem_disse_nao = 0
idade = 0
indiferente_f = 0
indiferente_m = 0

qt_entrevistado = 0
resp = 'C'
while resp == 'C':
    print("\n" * 20)
    print('----------------------------------------------------------')
    print('|      Sirius Game - Pesquisa de satisfação              |')
    print('----------------------------------------------------------')
    while sexo != 'F' and sexo != 'M':
        sexo = str(input('Digite seu sexo (F/M): ')).upper()
        if sexo == 'F' or sexo == 'M':
            while True:
                try:
                    idade = int(input("Qual sua idade? "))
                    break
                except ValueError:
                    print("Somente número!")
                    continue
        if sexo == 'F':
            while gostando != 'S' and gostando != 'N' and gostando != "I":
                gostando = str(input('Você está gostando dos nossos produtos? (S/N ou I para indiferente): ')).upper()
                if gostando == 'I':
                    indiferente_f = indiferente_f + 1
                    break
                if gostando == 'S':
                    mulher_gostando = mulher_gostando + 1
                    gostando_sim = gostando_sim + 1
                if gostando == 'N':
                    mulher_nao_gostando = mulher_nao_gostando + 1
                    gostando_nao = gostando_nao + 1
        if sexo == 'M':
            while gostando != 'S' and gostando != 'N' and gostando != 'I':
                gostando = str(input('Você está gostando dos nossos produtos? (S/N ou I para indiferente): ')).upper()
                if gostando == 'I':
                    indiferente_m = indiferente_m + 1
                    break
                if gostando == 'S':
                    homem_gostando = homem_gostando + 1
                    gostando_sim = gostando_sim + 1
                if gostando == 'N':
                    homem_nao_gostando = homem_nao_gostando + 1
                    gostando_nao = gostando_nao + 1

    sexo = 'sd'
    gostando = 'qualquercoisa'
    qt_entrevistado = qt_entrevistado+1
    resp = input('>>> Para continuar, aperte a tecla C \n>>> para parar, aperte qualquer tecla <<<')
    resp = resp.upper()
print("\n" * 20)
print('----------------------------------------------------------')
print('|      Sirius Game - Resultado da Pesquisa               |')
print('----------------------------------------------------------')
print('   Quantidade de pessoas entrevistadas foi: ', qt_entrevistado)
print('   A quantidade de pessoas gostando é de: ', gostando_sim)
print('   A quantidade de pessoas que NÃO estão gostando é de: ', gostando_nao)
total = gostando_nao*(100/qt_entrevistado)
string = "   {:.2f}%  disseram não gostar" . format(total)
print(string)
if mulher_gostando == 1:
    print('   ', mulher_gostando, 'mulher disse ter gostado')
else:
    print('   ', mulher_gostando, 'mulheres disseram ter gostado')
if homem_nao_gostando == 1:
    print('   ', homem_nao_gostando, 'homem disse ter gostado')
else:
    print('   ', homem_nao_gostando, 'homens disseram não ter gostado')
print('----------------------------------------------------------')
input("Pressione enter para encerrar...")
