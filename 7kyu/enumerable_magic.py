def each_cons(lst, n):
    lista = []
    for i in range(len(lst) - n + 1):
        lista.append(lst[i:i+n])
    return lista



