def bublesort(lista):
    intercambio =True
    while intercambio:
        intercambio=False
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                lista[i],lista[i+1] = lista[i+1],lista[i]
                intercambio = True

listado = [8,5,4,7,9,45,21,57,24,2]
bublesort(listado)
print(listado)