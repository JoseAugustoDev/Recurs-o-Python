def soma(l: list):
    if len(l) == 0:
        return 0
    else:
        return l[0] + soma(l[1:])
    
lista = [3, 54, 9, 4, 2]

print(soma(lista))