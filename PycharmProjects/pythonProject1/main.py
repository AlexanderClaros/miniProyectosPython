import random
def seguir():
    seguir = input('desea seguir jugando S/N')
    if seguir == 's':
        comprobar= True
    elif seguir == 'n':
        comprobar = False
    return comprobar
def menu():
    print('seleccione accion a realizar')
    print('pulse 1 para introducir una letra')
    print('pulse 2 para adivinar la palabra')
    accion = int(input())
    return accion
lista=['ordenador','silla','dragon','listado','raton']
comprobar = True

vida = 3
partida= True
while comprobar == True:
    print('=========Bienvenido========')
    print('este es el juego del ahorcado')
    print('vidas:3')
    adivinar = lista[random.randrange(len(lista))]
    print('-' * len(adivinar))
    resultado = '-' * len(adivinar)
    while vida >= 1  and partida == True:

        accion = menu()
        if accion == 1 :
            letra = input('introduzca la letra')
            if len(letra)> 1:
                print('solo debe introducir una letra')
            else:
                for i in range (len(adivinar)):
                    if adivinar[i] == letra:
                        tmp= list(resultado)
                        tmp[i]=letra
                        resultado=''.join(tmp)
                        break
                    elif i == len(adivinar)-1 and adivinar[i]!=letra:
                        vida = vida - 1
                        print('te quedan: ',vida, ' vidas')

                        if vida == 0:
                            print('has perdido')
                            comprobar=seguir()

                        break

            print(resultado)
        elif accion == 2:
            palabra =input('introduzca la palabra')
            if palabra == adivinar:
                print('ganaste')
                partida=False
                comprobar=seguir()
            elif palabra != adivinar:
                print('te equivocaste')
                vida = vida - 1
                print('te quedan: ', vida, ' vidas')
                if vida == 0:
                    print('has perdido')
                    comprobar=seguir()
        else:
            print('no le entendi')
    vida=3
    partida=True