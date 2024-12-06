#def Media(*args):
    #if not args:
        #return 0.0
    #return sum(args) / len(args)
#resultado = Media(10, 20, 30, 40, 50)
#print(resultado)

#def Media(*num):
    #if not num:
        #return 0.0
    #return sum(num) / len(num)
#resultado = Media(10, 20, 30, 40, 50)
#print(resultado)

def Media(*args):
    resultado = sum(args) / len(args)
    return resultado
print(Media(10, 20, 30, 40, 50))