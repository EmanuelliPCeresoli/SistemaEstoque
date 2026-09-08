def ordenar_produtos_por_codigo(produtos):
    produtos_ordenados = produtos.copy()

    for i in range(1, len(produtos_ordenados)):
        produto = produtos_ordenados[i]
        indice = i - 1

        while indice >= 0 and produtos_ordenados[indice].codigo > produto.codigo:
            produtos_ordenados[indice + 1] = produtos_ordenados[indice]
            indice -= 1

        produtos_ordenados[indice + 1] = produto

    return produtos_ordenados