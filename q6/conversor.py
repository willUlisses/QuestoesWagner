def real_para_dolar():
    valor = float(input("Digite o valor em reais: "))
    cotacao = float(input("Informe a cotação: "))
    print(f"R${valor} em reais equivalem a U${(valor / cotacao):.2f} em dólares")

def dolar_para_real():
    valor = float(input("Digite o valor em dólar: "))
    cotacao = float(input("Informe a cotação: "))
    print(f"U${valor} dólares equivalem a R${(valor * cotacao):.2f} em reais")




