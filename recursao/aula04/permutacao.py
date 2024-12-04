def troca(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux

def perm(l: list, pos=0):
    if pos == len(l) - 1:
        print(l)
    else:
        for i in range(pos, len(l)):
            troca(l, pos, i)
            perm(l, pos=pos+1)
            troca(l, pos, i)

lista = [8, 0, 9]

perm(lista)