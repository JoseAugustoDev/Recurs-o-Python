def troca(l, i, j):
    aux = l[i]
    l[i] = l[j]
    l[j] = aux

def perm(l: list, result, pos=0):
    if pos == len(l) - 1:
        l_aux = l[:]
        result.append(l_aux)
    else:
        for i in range(pos, len(l)):
            troca(l, pos, i)
            perm(l, pos=pos+1, result=result)
            troca(l, pos, i)

lista = [8, 0, 9]

result = []

perm(lista, result)

print(result)