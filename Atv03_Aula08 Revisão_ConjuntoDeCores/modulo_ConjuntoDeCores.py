#Esta Função relaciona as cores que temm mais de 4 caracteres.
def ConjuntoDeCores(Conjunto_Cores, Cores4Caracter):
    #Conjunto_Cores = {'amarelo', 'azul', 'vermelho', 'verde', 'preto', 'rosa', 'branco'}
    for cor in Conjunto_Cores:
        if len(cor) > 4:
            Cores4Caracter.add(cor)
    print(Cores4Caracter)
    print("Estas Cores tem mais de quatro caracteres.")