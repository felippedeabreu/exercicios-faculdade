dolar = float(input("Qual o preço do dolar hoje? "))
grana = float(input("Quanto tu tens em Reais? "))
valor = dolar*grana;

if valor > 1000:
    conta = valor * 8 / 100;
    print("Você deverá doar R$ {:.2f}".format(conta))
else:
    print("O valor não foi suficiente para doação")
input('Pressione enter para encerrar')