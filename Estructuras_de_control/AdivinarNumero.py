

'''    ----------------------------------------------------------------
    Ejercicio Desafío.
    Deberá aplicar las estructuras de control que crea conveniente
    para resolver el ejercicio, puede ser condicional/repetitiva
    o una mezcla de ambas.
    -----------------------------------------------------------------
    EJERCICIO 4: 
    Crea una aplicación que permita adivinar un número. 
    La aplicación genera un número aleatorio del 1 al 100. 
    A continuación va pidiendo números y va respondiendo 
    si el número a adivinar es mayor o menor que el introducido,
    además de los intentos que te quedan (tienes 10 intentos para acertarlo). 
    El programa termina cuando se acierta el número (además te dice en 
    cuantos intentos lo has acertado), si se llega al limite de intentos 
    te muestra el número que había generado.
'''
#Coloque la resolución del Ejercicio 4 debajo de esta línea:

import random
inicio = 0
final = 100
respuesta_programa = random.randint(inicio, final)

print("Adivina el número. Ingresa un número entre el 0 y el 100.")


respuesta_usuario = int(input("Respuesta: " ))
print('Intento: 1') 
print()
intentos = 1 
while ((respuesta_usuario != respuesta_programa) & (intentos < 10)):
    
    if (respuesta_usuario > respuesta_programa):
        print("El número es menor a: ", respuesta_usuario)
        
    elif (respuesta_usuario < respuesta_programa):
        print("El número es mayor a: ", respuesta_usuario)
            
      
    respuesta_usuario = int(input("Respuesta: "))
    intentos= intentos +1    
    print('Han pasado ', intentos, ' intentos')
    print()
inicio= inicio+1    
if (intentos == 10):
    print('Lo siento, han pasado los 10 intentos')
    print('Gracias por jugar')
else:
        print('Felicitaciones. Ha acertado el número en: ', intentos, ' intentos')

