#Autor del proyecto
#Ruben
############
#Importados#
############
import sys


#######################################
#Funciones de Acciones de los usuarios#
#######################################
def Identificarse():
    nombre=input("Nombre : ")
    contraseña=input("Contraseña : ")

del ver

def Salir():
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
    print("Ideentifiquese");
elif opcion == 2:
    print("Ver todos los productos");
elif opcion ==3:
    Salir()

############################
#Menu usuario Identificados#
############################