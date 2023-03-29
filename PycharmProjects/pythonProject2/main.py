import random
print('======Piedra,Papel o Tijeras=======')
game = True
movimientos = ['piedra', 'papel', 'tijeras']
while game == True:
    adversario = random.choice(movimientos)
    print('movimientos: \n 1.piedra\n 2.papel\n 3.tijeras')

    mov=input('introduce movimiento')
    if mov == adversario:
        print('empate nadie pierde')
    elif mov == 'tijeras' and adversario == 'piedra'or mov == 'papel' and adversario == 'tijeras' or mov == 'piedra' and adversario == 'papel':
        print('tu pierdes')
    elif mov == 'papel' and adversario == 'piedra'or mov == 'tijeras' and adversario == 'papel' or mov == 'piedra' and adversario == 'tijera':
        print('tu ganas')
    else:
        print('repite el movimiento')

