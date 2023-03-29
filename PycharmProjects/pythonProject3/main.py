import math


def es_primo (num):
    for n in range(2,num):
        if num % n == 0:
            print('no es primo')
            return False
    print('Es Primo')
    return True

es_primo(9)

def raiz_cuadrada(num):
    return num**0.5
print(raiz_cuadrada(47))

def sacarMenor(lista):
    posicion = 0
    for i in range(len(lista)):
        menor =lista[0]
        if lista[i]< menor:
            menor=lista[i]
            posicion=i
    del lista[posicion]

listado =[2,6,4,1,5,7]
sacarMenor(listado)
print(listado)

def tabla ():
    for i in range(1,11):
        for j in range(1,11):
            print(i,'x',j,'=',j*i)
tabla()

def media(listado):
    media=0
    for i in range(len(listado)):
        media = media+listado[i]
    return media/len(listado)
print(media(listado))
listado2 =[2,6,4,1,5,7]

def bublesort(listado):
    intercambio = True
    while intercambio:
        intercambio=False
        for i in range(len(listado)-1):
            if listado[i]>listado[i+1]:
                listado[i],listado[i+1]=listado[i+1],listado[i]
                intercambio = True
bublesort(listado2)
print(listado2)

def primos (numero):
    for i in range(2,numero):
        if numero % i==0:
            return False
    return True
print(primos(31))