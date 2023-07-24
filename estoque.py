def max_estoque(lista_estoque):
    if (len(lista_estoque) == 0):
        return []
    resultado = []
    max_estoque = lista_estoque[0][1]
    for elem in lista_estoque:
        if (elem[1] == max_estoque):
            resultado.append(elem)
        elif (elem[1] > max_estoque):
            max_estoque = elem[1]
            resultado = []
            resultado.append(elem)
    return resultado