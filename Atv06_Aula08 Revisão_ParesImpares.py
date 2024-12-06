
def ParesImpares():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    par = []
    impar = []
    
    for i in lista:
        if i % 2 == 0: 
            par.append(i)
        else:  
            impar.append(i)
    
    QuantidadePar = len(par)
    QuantidadeImpar = len(impar)
    
    print(f"Quantidade de números pares: {QuantidadePar}")
    print(f"Quantidade de números ímpares: {QuantidadeImpar}")

ParesImpares()
