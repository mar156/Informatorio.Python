''''    -----------------------------------------------------------------
    Ejercicio simple para practicar Estructuras de control.
    Para resolver este ejercicio deberá utilizar estructuras 
    repetitivas.
    -----------------------------------------------------------------
    EJERCICIO 3: 
    Cree un programa que pida números hasta que se introduzca un cero. 
  Debe imprimir la suma total de todos los numeros introducidos y el promedio.
'''

# Coloque la resolución del Ejercicio 3 debajo de esta línea

acumulador = 0
n= 0
numero_consola = int(input('Ingrese por favor un número: '))
print()
while (numero_consola != 0):
    n= n+1
    acumulador+= numero_consola
    print("Suma total de todos los números: ", acumulador)
    print("Promedio de todos los números: ", (acumulador/n))
    print()
    numero_consola = int(input('Ingrese por favor un número: '))
    print()
    
