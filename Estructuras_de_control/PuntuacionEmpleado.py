
'''
    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    condicionales.
    -----------------------------------------------------------------
    EJERCICIO 2: 
    En una determinada empresa, sus empleados son evaluados al final 
    de cada año. Los puntos que pueden obtener en la evaluación comienzan 
    en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. 
    Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 
    o más, pero no valores intermedios entre las cifras mencionadas. 
    A continuación se muestra una tabla con los niveles correspondientes 
    a cada puntuación. La cantidad de dinero conseguida en cada nivel 
    es de 10000$ multiplicada por la puntuación del nivel.
        Nivel	        Puntuación
        Inaceptable	        0.0
        Aceptable	        0.5
        Meritorio	        0.6 o más
    Imprima por pantalla el nivel en que se encuentra el empleado, 
    la puntuación y la cantidad de dinero conseguida.
'''

# Coloque la resolución del Ejercicio 2 debajo de esta línea

puntuacion_empleado = float(input("Ingrese la puntuación del empleado: "))
print()
dinero = puntuacion_empleado*10000
if (puntuacion_empleado == 0):
    print('Nivel Inaceptable')
    print( 'Puntuación 0.0')
    print('La cantidad de dinero conseguida es de: ', dinero)
elif (puntuacion_empleado == 0.5):
    print('Nivel Aceptable')
    print('Puntuación 0.5')
    print('La cantidad de dinero conseguida es de: ', dinero)
elif ( puntuacion_empleado>= 0.6):
    print('Nivel Meritorio')
    print('Puntuación ', puntuacion_empleado )
    print('La cantidad de dinero conseguido es de: ', dinero)
else:
    print('Puntuación incorrecta. Ingrese nuevamente la puntuación')
print()
