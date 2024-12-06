
def ListaDePalindromo():
    minha_lista = ['tiago', 'ana', 'arara', 'pistola', 'osso', 'cabeça', 'radar']
    palindromos = []
    for palavra in minha_lista:
        if palavra == palavra[::-1]:
            palindromos.append(palavra)
    print(palindromos)
ListaDePalindromo()