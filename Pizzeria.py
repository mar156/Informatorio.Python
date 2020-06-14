print('Ciao! Bienvenido a Bella Napoli.')

menu_ordenar=int(input('Si desea ver nuestro menú presione 1, si ya sabe lo que va a ordenar presione 2: '))
if (menu_ordenar == 1):
   print('Menu: PIZZA')
   print('Ingredientes: ')
   print('- Tomate')
   print('- Muzzarella')
   print('OPCIONAL PIZZA COMÚN: Jamón o Panceta')
   print( 'OPCIONAL PIZZA VEGETARIANA:Pimiento o Rúcula')
   print()
   print('Si desea una Pizza vegetariana presione 1, ' )
   menu_orden=int(input('Si desea una Pizza común presione 2: '))
   print()
   if ( menu_orden == 1):
       print('Si desea su Pizza vegetariana sólo con tomate y muzzarella presione 1')
       print('Si desea su Pizza vegetariana con tomate, muzarella y pimiento presione 2')
       pizza_agregadoveg=int(input('Si desea su Pizza vegetariana con tomate, muzzarella y rúcula presione 3: '))
       print()
       if ( pizza_agregadoveg == 1):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza vegetariana con tomate y muzarella')
           print('Muchas gracias por su compra')
       elif(pizza_agregadoveg == 2):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza vegetariana con tomate, muzarella y pimiento')
           print('Muchas gracias por su compra') 
       elif(pizza_agregadoveg == 3):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza vegetariana con tomate, muzarella y rúcula')
           print('Muchas gracias por su compra')
   elif (menu_orden == 2):
        print('Si desea su Pizza común sólo con tomate y muzzarella presione 1')
        print('Si desea su Pizza común con tomate, muzarella y jamón presione 2')
        pizza_agregadocom=int(input('Si desea su Pizza común con tomate, muzzarella y panceta presione 3: '))   
        print()
        if (pizza_agregadocom== 1):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza común con tomate y muzarella')
           print('Muchas gracias por su compra')
        elif(pizza_agregadocom== 2):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza común con tomate, muzarella y jamón')
           print('Muchas gracias por su compra') 
        elif(pizza_agregadocom == 3):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza común con tomate, muzarella y panceta')
           print('Muchas gracias por su compra')
elif (menu_ordenar==2):
   print('Si desea una Pizza vegetariana presione 1, ' )
   menu_orden=int(input('Si desea una Pizza común presione 2: '))
   print()
   if ( menu_orden == 1):
       print('Si desea su Pizza vegetariana sólo con tomate y muzzarella presione 1')
       print('Si desea su Pizza vegetariana con tomate, muzarella y pimiento presione 2')
       pizza_agregadoveg=int(input('Si desea su Pizza vegetariana con tomate, muzzarella y rúcula presione 3: '))
       print()
       if ( pizza_agregadoveg == 1):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza vegetariana con tomate y muzarella')
           print('Muchas gracias por su compra')
       elif(pizza_agregadoveg == 2):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza vegetariana con tomate, muzarella y pimiento')
           print('Muchas gracias por su compra') 
       elif(pizza_agregadoveg == 3):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza vegetariana con tomate, muzarella y rúcula')
           print('Muchas gracias por su compra')
   elif (menu_orden == 2):
        print('Si desea su Pizza común sólo con tomate y muzzarella presione 1')
        print('Si desea su Pizza común con tomate, muzarella y jamón presione 2')
        pizza_agregadocom=int(input('Si desea su Pizza común con tomate, muzzarella y panceta presione 3: '))   
        print()
        if (pizza_agregadocom== 1):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza común con tomate y muzarella')
           print('Muchas gracias por su compra')
        elif(pizza_agregadocom== 2):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza común con tomate, muzarella y jamón')
           print('Muchas gracias por su compra') 
        elif(pizza_agregadocom == 3):
           print( 'Su pedido ha sido procesado con éxito' )
           print( 'Pedido: Pizza común con tomate, muzarella y panceta')
           print('Muchas gracias por su compra')    