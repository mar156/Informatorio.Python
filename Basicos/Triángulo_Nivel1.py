''' 
    -----------------------------------------------------------------
    Ejercicio para practicar asignación de datos e 
    impresión de cálculos por pantalla por lo que no
    deben utilizar estructuras de control solo deben solicitar datos
    hacer el calculo e imprimirlo.
    -----------------------------------------------------------------
    EJERCICIO 1: 
    Dado de los valores ingresados por el usuario (base, altura) 
    calcular y mostrar en pantalla el área de un triángulo.
'''''
# Coloque la resolución del Ejercicio 1 debajo de esta línea

base_triangulo = float(input("Ingrese en cm la base del triángulo: " ))
altura_triángulo = float(input("Ingrese en cm la altura del triángulo: " ))

area_triangulo= (base_triangulo*altura_triángulo)/2
print( "El área del triángulo es de: ", area_triangulo, "cm²")

