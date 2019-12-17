import time
GREEN = '\033[32m'
WHITE = '\033[m'
RED = '\033[31m'
YELLOW = '\033[33m'
BLUE = '\033[34M'


def loginregistrado(productos, usuario, id):
    print(BLUE+" --------------------------")
    print(" Bienevenido ", usuario[id][0])
    print(" --------------------------\n", WHITE)


def identificarse(productos, usuarios):
    print(" Iniciando Login...\n")
    time.sleep(2)
    print(YELLOW+" ---------------------------------------\n",
          "Bienvenido al Login de la aplicacion\n",
          "---------------------------------------\n", WHITE)
    nombre = input(" Introduzca el nombre de su usuario : ")
    contraseña = input(" Introduzca su contraseña : ")
    print("")
    coincidencias = 0
    for clave in usuarios.keys():
        if nombre == usuarios[clave][2] and contraseña == usuarios[clave][3]:
            coincidencias = 1
            print(GREEN+" Usuario Logeado correctamente\n", WHITE)
            loginregistrado(productos, usuarios, clave)

    if coincidencias == 0:
        print(RED+" Error en el usuario o la contraseña\n", WHITE)