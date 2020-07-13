ventas_dia_1 = float(input ('Ingrese las ventas del día uno: '))
print()
ventas_dia_2= float(input ('Ingrese las ventas del día dos: '))
print()
## Pongo float así pueden poner los ingresos de manera más exacta

if (ventas_dia_1> ventas_dia_2):
    print ('Se vendió más el día uno')
elif(ventas_dia_2>ventas_dia_1):
    print('Se vendió más el día dos')
else:
    print('Se vendió lo mismo en ambos días')
