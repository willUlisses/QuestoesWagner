def contador_palavra(frase, palavra):
    palavras_frase = frase.split()
    contador = 0

    for p in palavras_frase:
        if palavra.lower() == p.lower():
            contador += 1

    return contador;
