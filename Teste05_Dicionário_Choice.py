import random

#Escolhe um elemento aleatório de uma lista
def escolhe():
    minha_lista = ["Tiago","Daniel","Waleska","Calebe"]
    escolha = random.choice(minha_lista)
    return escolha
print(escolhe())