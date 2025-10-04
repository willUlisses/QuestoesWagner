def real_para_dolar():
    valor = float(input("Digite o valor em reais: "))
    cotacao = float(input("Informe a cotação: "))
    print(f"R${valor:.2f} em reais equivalem a U${(valor / cotacao):.2f} em dólares")

def dolar_para_real():
    valor = float(input("Digite o valor em dólar: "))
    cotacao = float(input("Informe a cotação: "))
    print(f"U${valor:.2f} dólares equivalem a R${(valor * cotacao):.2f} em reais")


def conversorDeMoedas(tipo=1):
    if tipo == 1:
        real_para_dolar()
    else:
        dolar_para_real()
