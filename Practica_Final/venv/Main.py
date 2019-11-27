#Autor del proyecto
#Ruben
############
#Importados#
############
import sys

#######################################
#Funciones de Acciones de los usuarios#
#######################################
def identificarse():
    nombre=input("Nombre : ")
    contraseña=input("Contraseña : ")

    #Comprobamos el si el nombre y la contraseña existe y si es admin
    contador = 1
    #Empieza en no logeado por defecto ni en usuario ni en administrado

    while contador < len(usuarios)+1:
        if usuarios.get(contador)[0] == nombre and usuarios.get(contador)[2] == contraseña:
            if usuarios.get(contador)[4] == 'false':
                #Si a pasado el logueo de usuario cambiamos la variable login a true
                print("Usuario normal logueado correctamente\n")
                menu_registrado()
            elif usuarios.get(contador)[4] == 'true':
                print("Usuario administrador logueado correctamente\n")
                menu_admin()
        contador = contador + 1

#########################
#Menu usuario Registrado#
#########################
def menu_registrado():
    print('Bienvenido señor\n')
    print("Menu de usuario anónimo\n"
          "1 : Modificar tus Datos\n"
          "2 : Mostrar tus vendedores recomendados\n"
          "3 : Recomendar un vendedor\n"
          "4 : Ver todos los productos a la venta\n"
          "5 : Ver productos de tus vendedores recomendados\n"
          "6 : Valorar producto\n"
          "7 : Poner a la venta un producto\n"
          "8 : Desconectarse (Volverse anónimo)\n"
          "9 : Salir de la aplicación\n"
          "------------------------------------------------\n"
          )
    opcion = int(input("Opción : "))

    if opcion == 1:
        print()


def menu_admin():
    print('Bienvenido esclavo')


def listar():
    contador = 1
    while contador < len(productos)+1:
        print(productos.get(contador)[0])
        contador = contador + 1


def salir():
    sys.exit()

##############
#Diccionarios#
##############

#Diccionario Usuarios


usuarios = {1: ['ruben', 'martinez', 'admin', '20', 'true', [1, 2]],
            2: ['ivan', 'clemente', 'admin', '20', 'false', [1]]
            }

#Diccionario Productos


productos = {1: ['1', 'casco', 'seminuevo', '2', [1, 2], [1, 2], [1, 2]],
             2: ['2', 'ivan', 'nuevo', '1', [1, 2], [1, 2], [1]]
             }
#######################
#Menu usuario anónimos#
#######################
print("Menu de usuario anónimo\n"
      "1 : Identificarse\n"
      "2 : Ver todos los productos\n"
      "3 : Salir de la aplicacion")
opcion=int(input("Opción : "))


#Menu que comprueba la opcion introducida y llama al metodo correspondiente
if opcion == 1:
    identificarse()
elif opcion == 2:
    listar()
elif opcion == 3:
    salir()

