#imports
import Login
import Funciones
import time
#colores
RED = '\033[31m'
BLUE = '\033[34m'
YELLOW = '\033[33m'
WHITE = '\033[m'

#diccionario
# 0 nombre
# 1 apellido
# 2 login
# 3 contraseña
# 4 identificador interno
# 5 vendedores recomendados

usuarios = {
    1: ["ruben", "Apellido", "ru", "admin", 1, [1]],
    2: ["ivan", "Apellido", "iv", "admin", 1, [1]]
}

# 0 nombre
# 1 precio
# 2 identificador
# 3 listado de me gusta
# 4 listado de buen precio
# 5 listado de vendido

productos = {
    1: ["nombre1", 2000, "Descripciones1", 2, [1], [1], [1]],
    2: ["nombre2", 2000, "Descripciones2", 2, [1], [1], [1]],
    3: ["nombre3", 2000, "Descripciones3", 2, [1], [1], [1]],
    4: ["nombre4", 2000, "Descripciones4", 2, [1], [1], [1]]
}

#menu de usuario
print(YELLOW+" --------------------------------\n",
      "APLICACION DE VENTA DE PRODUCTOS\n",
      "--------------------------------", WHITE
      )

while True:
    print(YELLOW+" -----------------------------")
    print(BLUE+" 1 : IDENTIFICARSE\n",
          "2 : VER PRODUCTOS \n",
          "3 : SALIR ")
    print(YELLOW+" -----------------------------\n",WHITE)
    opcion = int(input(" Que quiere hacer : "))

    if opcion == 1:
        Login.identificarse(productos, usuarios)

    if opcion == 2:
        Funciones.verproductos(productos)

    if opcion == 3:
        print("Cerrando Aplicacion...")
        time.sleep(2)
        break
