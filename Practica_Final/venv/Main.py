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


def listar():
    print("Ver todos los productos")


def salir():
    sys.exit()



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