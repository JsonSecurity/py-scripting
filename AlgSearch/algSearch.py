#!/bin/python
from collections import Counter
import pprint
from time import sleep as delay

R = "\033[31m"    # Red
G = "\033[32m"    # Green
Y = "\033[33m"    # Yellow
B = "\033[34m"    # Blue
P = "\033[35m"    # Pink
C = "\033[36m"    # Cyan
L = "\033[37m"    # Lead
W = "\033[0m"    # White

T = L + " [" + G + "+" + L + "] " + W
F = L + " [" + R + "-" + L + "] " + W
A = L + " [" + R + "!" + L + "] " + W
Q = L + " [" + C + "?" + L + "] " + W
N = L + " [" + C + "#" + L + "] " + W
E = L + " [" + G + "..." + L + "] " + W

list = [
        "comida",
        "nadar",
        "mirada",
        "cantar",
        "nadie",
        "nunca",
        "andar",
        "juntar",
        "jugar",
        "ludo",
        "lima",
        "limon",
        "como",
        "untar",
        "donde"
             ]

def search(cadena):
    val = len(cadena)
    print("\n" + N + "longitud:",val,"\n")

    similitudes = []
    for i in range(val-1):
        for pal in list:
            if cadena[i:i+2] in pal:
                print(E + "Buscando:"+ C,cadena[i:i+2] + B + " ",pal)
                similitudes.append(pal)

    #print(similitudes)
    #print(T + "Longitud:", len(similitudes))

    if len(similitudes) >= 1:
        counter = Counter(similitudes)
    
        first = counter.most_common()

        tup = first[0]
        print("\n" + T + "Palabra: " + G + tup[0])
    else:
        print(F + "No se encontraron similitudes")
    
    '''
    for i in list:
        if str(cadena[0:2]) in i:
            print("[1]")
            print(i)

    for i in list:
        if cadena[2:4] in i:
            print("2")
            print(i)

    for i in list:
        if cadena[4:6] in i:
            print("3")
            print(i)
'''
for i in list:
    print(T + i)
    delay(.1)

palabra = input("\n" + Q + "Ingrese una palabra mal escrita: "+ Y).lower()
search(palabra)

