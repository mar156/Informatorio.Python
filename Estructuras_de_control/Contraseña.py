
#En este ejercicio debo ingresar una contraseña y sólo aceptar si la contraseña
#es correcta, en caso contrario, tenemos 3 intentos y se bloquea la cuenta
clave = input ('Ingrese su contraseña: ')
clave= str()
print()

cont = 0
int(cont)

while cont < 4 :
    if (clave == 'clave123'): 
        print('Bienvenido')
        break 
    
    elif (clave != 'clave123'): 
        print('Su contraseña es incorrecta')
        print()
        clave = input ('Ingrese su contraseña: ')   
        cont= cont+1
        if (cont==4):
            print('Se ha bloqueado su cuenta')
    
