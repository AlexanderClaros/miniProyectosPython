from carta import Carta
import random



def baraja():
    listNumber = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']
    figure = ['❤', '☘', '♠', '♦']
    deck = []
    for i in range(len(listNumber)):
        for j in range(len(figure)):
            card =Carta(listNumber[i],figure[j])
            deck.append(card)
    return deck
def sacarCarta(baraja):
    indexRamdon = random.randrange(len(baraja))
    getCarta = baraja[indexRamdon]
    baraja.remove(getCarta)
    return getCarta,baraja


def iniciar():
    mazo = baraja()
    money=100


    while money > 0:
        global partida
        partida=True
        print('=========Bienvenido=========')
        print('dinero:', money)
        playerList = []
        crupierList = []
        apuesta = int(input('ingrese cantidad de dinero a apostar'))
        if apuesta <= money:
            countPlayer = 0
            countCrupier = 0
            while partida == True:
                print('seleccione accion:'
                      '\n 1.pedir   2.plantarse ')
                seleccion =int(input())
                if seleccion == 1:
                    tu_carta, mazo = sacarCarta(mazo)
                    print('tu carta:', tu_carta.numero + tu_carta.figura)
                    playerList.append(tu_carta.numero+tu_carta.figura)
                    if tu_carta.numero == 'J' or tu_carta.numero =='Q' or tu_carta.numero == 'K':
                        countPlayer = countPlayer + 10
                    elif tu_carta.numero == 'A':
                        if countPlayer > 11:
                            countPlayer = countPlayer+1
                        else:
                            countPlayer = countPlayer + 11
                    else:
                        carta_tmp =int(tu_carta.numero)
                        countPlayer = countPlayer + carta_tmp


                    if countPlayer > 21 :
                        print('perdiste')
                        countPlayer=0 fjñlll
                        partida = False
                        money = money - apuesta
                elif seleccion == 2:
                    solicitar =True
                    while solicitar:
                        crupier, mazo = sacarCarta(mazo)
                        crupierList.append(crupier.numero+crupier.figura)
                        if crupier.numero == 'J' or crupier.numero == 'Q' or crupier.numero == 'K':
                            countCrupier = countCrupier + 10
                        elif crupier.numero == 'A':
                            if countCrupier > 10:
                                countCrupier = countCrupier + 1
                            else:
                                countCrupier = countCrupier + 11
                        else:
                            carta_tmp = int(crupier.numero)
                            countCrupier = countCrupier + carta_tmp
                        if countCrupier >= 16:
                            solicitar = False
                    print('jugador:')
                    print(playerList)
                    print('crupier:')
                    print(crupierList)
                    if countPlayer == 21:
                        print('ganaste')
                        countPlayer = 0
                        countCrupier = 0
                        money = money + apuesta
                        partida = False
                    elif countPlayer > countCrupier and countPlayer <= 21:
                        print('ganaste')
                        countPlayer = 0
                        countCrupier = 0
                        money = money + apuesta
                        partida = False
                    elif countPlayer == countCrupier:
                        print('empate nadie gana')
                        countPlayer = 0
                        countCrupier = 0
                        partida = False
                    elif countPlayer < countCrupier and countCrupier > 21:
                        print('ganaste')
                        money = money + apuesta
                        countPlayer = 0
                        countCrupier = 0
                        partida = False
                    elif countPlayer < countCrupier and countCrupier <= 21:
                        print('perdiste')
                        countPlayer = 0
                        countCrupier = 0
                        money = money - apuesta
                        partida = False
        else:
            pass
iniciar()
