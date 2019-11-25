idinterno = 1
idvendedorrecomendado=0
dicusers = {'1': ["administrador","admin","admin",123,idinterno],'2':["jesus","fernandez","jesus",123,idinterno+1]}
dicvalueadmin = dicusers.get('1')
dicvalueregister = dicusers.get('2')



opcion=0;

while True:
    print("Bienvenido a nuestra aplicacion: ")
    print("----------------------------------")
    print("----------------------------------")
    print("----------------------------------")
    print("Bienvenido usuario anonimo")
    print("----------------------------------")

    print("Introduce una opcion: ")
    print("1. Login")
    print("2. Ver productos a la venta")
    print("0. Salir")
    opcion=int(input())

    if(opcion==1):
        login = input("introduce un nombre de inicio de sesion: ")
        password = int(input("Introduce una contraseña: "))

        if ((login == dicvalueadmin[2]) and (password == dicvalueadmin[3])):
            print("Bienvenido administrador")
            opcion2=int(input("Introduce una opcion"))




        if(login == dicvalueregister[2] and (password == dicvalueregister[3])):
            print("Bienvenido usuario registrado")





    if(opcion==2):
        print("hola que tal")
        #TO DO visualizar todos los productos a la venta

    if(opcion==0):
        break
        #Salir


