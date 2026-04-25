def filtrar_pares(lista_numeros):
    """Filtrar números pares de una lista dada."""
    pares = []
    for x in lista_numeros:
     if x % 2==0:
        pares.append(x)
        return pares
"""Ejemplo de uso"""
numeros = [1, 2, 3, 4, 5, 6,]
numeros_pares = filtrar_pares(numeros)
print(numeros_pares)


