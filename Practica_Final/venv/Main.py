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
    while contador < len(usuarios):
        print(usuarios.get(contador)[0], usuarios.get(contador)[2])
        if usuarios.get(contador)[0] == nombre and usuarios.get(contador)[2] == contraseña:
            if usuarios.get(contador)[4] == 'false':
                print("Usuario normal logueado correctamente")
                break;
            elif usuarios.get(contador)[4] == 'true':
                print("Usuario administrador logueado correctamente")
                break;
        contador = contador + 1


def listar():
    print("Ver todos los productos")


def salir():
    sys.exit()

##############
#Diccionarios#
##############

#Diccionario Usuarios


usuarios = {1: ['ruben', 'martinez', 'admin', '20', 'true', [1, 2]],
            2: ['ivan', 'clemente', 'admin', '20', 'false', [1]]
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

############################
#Menu usuario Identificados#
############################

