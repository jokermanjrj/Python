import time


def verproductos(productos):
    print("Mostrando productos...")
    time.sleep(3)
    for claves in productos.keys():
        print("------------------------------------")
        print("Nombre : ", productos[claves][0])
        print("Precio : ", productos[claves][1])
        print("Identificador", productos[claves][2])
        print("-------------------------------------")
    print("productos mostrados")
    time.sleep(3)