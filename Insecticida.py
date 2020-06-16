print ('Colillas al rescate')
inicio = True
personas = 0
menos100= 0
menos200=0
mas200=0

while inicio:
    print('Cantidad colillas: ')
    colillas= int(input("Colillas: "))
    if colillas<100:
        menos100+=colillas
    elif colillas <200:
        menos200 +=colillas
    else:
        mas200 +=colillas
    personas +=1

    seguimos = int(input("Seguimos 1-Si 0-No"))
    if seguimos == 0:
        inicio=False

print('Cantidad de personas', personas)
print('%menos de 100 colillas', menos100*100/personas)
print('FIN')