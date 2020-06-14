
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
    
