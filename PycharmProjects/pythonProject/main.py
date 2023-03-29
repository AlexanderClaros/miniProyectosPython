from Calculadora import *
def sumar(numero1,numero2):
    return numero1+numero2
def restar(numero1,numero2):
    return numero1-numero2
def multiplicar (numero1,numero2):
    return numero1*numero2
def dividir (numero1, numero2):
    return numero1 / numero2
def potencia(numero1, numero2):
    return numero1 ** numero2
def introducir():
    print('introduzca un numero')
    numero = int(input())
    return numero

check = True


while check == True:
    print('iniciando calculadora'
          'indique que operacion desea realizar '
          'pulse 1 para sumar'
          'pulse 2 para restar'
          'pulse 3 para multiplicar'
          'pulse 4 para dividir'
          'pulse 5 para salir')
    comprobante =input()

    if comprobante == '1':
        numero1=introducir()
        numero2=introducir()
        print('El resultado es : ', sumar(numero1,numero2))
    elif comprobante =='2':
        numero1 = introducir()
        numero2 = introducir()
        print('El resultado es : ', restar(numero1, numero2))
    elif comprobante =='3':
        numero1 = introducir()
        numero2 = introducir()
        print('El resultado es : ', multiplicar(numero1, numero2))
    elif comprobante =='4':
        numero1 = introducir()
        numero2 = introducir()
        print('El resultado es : ', dividir(numero1, numero2))
    elif comprobante == '5':
        print('adios')
        check=False

    else:
        print('no le entendi')

def adivina_el_numero():
    print("")