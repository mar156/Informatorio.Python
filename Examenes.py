cantidad_preguntas = int(input ('Ingrese la cantidad total de preguntas: '))

print()
cantidad_correctas = int(input ('Ingrese la cantidad total de respuestas correctas: '))
print()

porcentaje = cantidad_correctas*100/cantidad_preguntas

if (porcentaje >= 90):
    print('¡Excelente!')
    
elif ((porcentaje >= 70) & (porcentaje < 90)) :
    print('Bueno')
    
elif ((porcentaje >= 60) & (porcentaje < 70)):
    print('Aprobado')
    
else:
    print('No alcanzó')
