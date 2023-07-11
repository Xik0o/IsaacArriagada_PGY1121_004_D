import os
import numpy as np
import FuncionesExamen as fn
from datetime import datetime

os.system("cls")

matriz=np.empty((10,4),type(object))
contador=0
fn.fillmat(matriz)
rut=""
op=0
depa=""
while(op!=5):
    print('''****Casa Feliz****
    1. Comprar departamento
    2. Mostrar departamentos disponibles
    3. Ver listado de compradores
    4. Mostrar ganancias totales
    5. Salir''')
    print("")
    op=fn.validacionop(op)
    if(op==1):
        rut=fn.rellenodatos(rut)
        fn.showdisponible(matriz)
        os.system("pause")
        os.system("cls")
    if(op==2):
        fn.showdisponible(matriz)
        os.system("pause")
        os.system("cls")
    if(op==3):
        fn.datosrut(matriz)
        os.system("pause")

    if(op==5):
        os.system("cls")
        print("Muchas gracias por usar el sistema")
        print("Isaac Arriagada ")
        print(datetime.today())