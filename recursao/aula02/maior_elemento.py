def maior(a, b):
    if a > b: return a
    else: return b

def maximo(l: list):
    if len(l) == 1:
        return l[0]
    else:
        return maior(l[0], maximo(l[1:]))
    
lista = [32]

print(maximo(lista))