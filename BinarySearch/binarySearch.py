#!/bin/python

from time import sleep as delay

R = "\033[31m"    # Red
G = "\033[32m"    # Green
Y = "\033[33m"    # Yellow
B = "\033[34m"    # Blue
P = "\033[35m"    # Pink
C = "\033[36m"    # Cyan
L = "\033[37m"    # Lead
W = "\033[0m"     # White

T = L + " [" + G + "+" + L + "] " + W
F = L + " [" + R + "-" + L + "] " + W
FF = L + " [" + R + "!" + L + "] " + W
Q = L + " [" + C + "?" + L + "] " + W
N = L + " [" + C + "#" + L + "] " + W
S = L + " [" + C + "str" + L + "] " + W

control = False

def binarySearch(list):
    #list = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    valor = int(input("\n" +T + "Ingrese un elemento:  "))

    steps = 0
    izq = 0
    der = len(list)-1

    while izq <= der:
        steps += 1
        punto_medio = (izq + der) // 2

        if list[punto_medio] == valor:
            print("\n" + T + "Valor encontrado en {} pasos, en la posición {}.".format(steps,punto_medio))
            return True
        if list[punto_medio] > valor:
            der = punto_medio -1
        if list[punto_medio] < valor:
            izq = punto_medio +1

    print("\n" +F+ "Elemento no encontrado")
    return False

def txtOrde():
    palabras = []
    print("\n" + T + "Ingrese las letras - Enter para detener\n")

    while True:
        val = input(S).lower()
        if len(val) == 0:
            break
        else:
            palabras.append(val)

    Intercambio = True
    while Intercambio:
        Intercambio = False
        for i in range(len(palabras)-1):
            i_1 = palabras[i]
            i_2 = palabras[i+1]

            a = ord(i_1[0])
            b = ord(i_2[0])

            if a > b:
                Intercambio = True
                palabras[i], palabras[i+1] = palabras[i+1], palabras[i]

    if control:
        print(T,palabras) 
        binarySearch(palabras)
    else:
        print(T,palabras)
            
def numOrde():
    numeros = []
    print("\n" + T + "Ingrese los numeros - Enter para detener\n")

    while True:
        try:
            val = int(input(N))
            numeros.append(val)
        except ValueError:
            break

    Intercambio = True
    while Intercambio:
        Intercambio = False
        for i in range(len(numeros)-1):
            if numeros[i] > numeros[i+1]:
                Intercambio = True
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]

    if control:
        print(T,numeros)
        binarySearch(numeros)
    else:
        print(T,numeros)
        
def start():    
    print(L+ " ["+B+"1"+L+"] "+W+" SorTxt\n"+L+" ["+B+"2"+L+"] "+W+" SortNum\n"+L+" ["+B+"3"+L+"] "+W+" BinarySearch\n")

    option = int(input(T + "Opción: "))

    if option == 1:
        txtOrde()
    elif option == 2:
        numOrde()
    elif option == 3:
        global control
        control = True
        
        print("\n" +L+" ["+B+"1"+L+"] "+W+" BinarySearchTxt\n"+L+" ["+B+"2"+L+"] "+W+" BinarySearchNum\n")

        option = int(input(T + "BinarySearch: "))
        
        if option == 1:
            txtOrde()
        elif option == 2:
            numOrde()
        else:
            print(F + "Invalid")
    else:
        print(F + "Invalid")

try:
    start()
except KeyboardInterrupt:
    print(F + "Bye")
