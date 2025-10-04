# Q6 - Conversor de Moedas
# Crie a função que converte reais para dólares e dólares para reais (arquivo conversor.py)
# real_para_dolar e dolar_para_real. Caso o usuário não passe o tipo (real_para_dolar ou dolar_para_real) o default deve ser real_para_dolar <- padrão

from conversor import conversorDeMoedas

print("Conversor entre dólares e reais\n")

tipo = int(input("Agora informe o tipo de conversão\n[1] - Real -> Dolar \n[2] - Dolar -> Real\n[3] - não inserir\nescolha: "))

match tipo:
    case 1:
        conversorDeMoedas(1) 
    case 2:
        conversorDeMoedas(2) 
    case _:
        conversorDeMoedas()        




