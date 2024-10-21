#!/usr/bin/env python3

from random import randint
import os
import time

R = "\033[31m"
G = "\033[32m"
Y = "\033[33m"
C = "\033[36m"
W = "\033[0m"

os.system("clear")

banner = G + '''
 ____  _                         ______        __
/ ___|| |_ _ __ ___  _ __   __ _|  _ \ \      / /
\___ \| __| '__/ _ \| '_ \ / _` | |_) \ \ /\ / /
 ___) | |_| | | (_) | | | | (_| |  __/ \ V  V /
|____/ \__|_|  \___/|_| |_|\__, |_|     \_/\_/
                           |___/
'''
print(banner)

val = R + "[" + W + "+" + R + "] "

name_file = "pass.txt"

v_i = 33
v_f = 126

name_user = input(val + W + "Nombre de usuario: " + C)

large_pass = int(input(val + W + "N° caracteres: " + C))

with open(name_file, "a") as file:
    file.write(os.linesep)
    file.write(os.linesep)
    file.write(name_user + " >>> ")
    for i in range(large_pass):
        rand = randint(v_i, v_f)
        asc = chr(rand)
        file.write(asc)
print(Y)
#os.system("tail -n 1 " + name_file)

time.sleep(.3)

os.system("cat pass.txt | base64 >> pass2.txt;rm -rf pass.txt")
file.close()
