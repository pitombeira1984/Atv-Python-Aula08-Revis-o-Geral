import random

# Embaralhar Lista

def EmbaralharLista():
    minha_lista = [1,2,3,4,5,6,7,8,9,10]
    random.shuffle(minha_lista)
    return minha_lista
print(EmbaralharLista())