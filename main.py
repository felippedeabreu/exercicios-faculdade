km_rodado = 5.50
custo_fixo = 5

lista_kilometro = []

lista_valor = []

for i in range(4):
    var = i+1
    km = float(input('Quantos KM o cliente ' + str(var) + " andou?: "))
    lista_kilometro.append(km)

for i in range(4):
    valor = lista_kilometro[i] * km_rodado + custo_fixo

for i in range(4):
    variavel = lista_kilometro[i] * km_rodado + custo_fixo
    lista_valor.append(variavel)

print("\n" * 40)
print('=====================================================')
print()

for i in range(4):
    print("O cliente",i+1,"pagará R$ {:.2f}".format(lista_valor[i]))
    print()

input("Pressione enter para finalizar!")