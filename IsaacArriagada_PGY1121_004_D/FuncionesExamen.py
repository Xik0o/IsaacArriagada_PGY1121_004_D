import os
from tkinter import N
import numpy as np

def fillmat(matriz):
    contador=10
    for i in range(10):
        for j in range(4):
            matriz[i,0]=f"A{contador}"
            matriz[i,1]=f"B{contador}"
            matriz[i,2]=f"C{contador}"
            matriz[i,3]=f"D{contador}"
        contador-=1

def validacionop(n):
    while(True):
        try:
            n=int(input("Elija Opcion: "))
            if(n<1 or n>5):
                print("Debe ingresar una de las opciones disponibles en el menu")
            else:
                return n
        except ValueError:
            print("Debe ingresar Numeros ENTEROS POSITIVOS")

def showdepa(matriz):
    piso=10
    print("Piso    A   B   C   D")
    for i in range (10):
        print("",piso, "\t", end="")
        piso-=1
        for j in range (4):
            print(" ", matriz[i,j], "\t")
            
def showdisponible(depa):
    for i in range(10):
        print("\t")
        for j in range (4):
            if(j==3):
                print("\t",depa[i,j], end=" ")
            else:
                print("\t",depa[i,j], end=" ")
    print("\n\n")

def rellenodatos(rut):
    while(len(rut)<=0):
        rut=int(input("Ingrese rut, debe tener minimo 8 caracteres "))
        if(rut>6 or rut<9):
            break
        else:
            print("Debe tener 8 caracteres minimo")

