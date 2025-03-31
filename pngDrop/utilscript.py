#!/usr/bin/env python3

from time import sleep as sleep
import os

R = '\033[31;1m'  # Rojo
G = '\033[32;1m'  # Verde
Y = '\033[33;1m'  # A;1marillo
B = '\033[34;1m'  # Azul
M = '\033[35;1m'  # Magenta
C = '\033[36;1m'  # Cian
W = '\033[37;1m'  # Blanco
N = '\033[30;1m'  # Negro

# Negrita y subrayado
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# Fondo
BG_R = '\033[41m'  # Fondo rojo
BG_G = '\033[42m'  # Fondo verde
BG_B = '\033[44m'  # Fondo azul

RESET = '\033[0m'  # Restablecer al estilo normal

_C = Y
_B = N
_E = W

_T = f' {_B}[{_C}+{_B}]{_E}'
_A = f' {_B}[{_C}!{_B}]{_E}'
_Q = f' {_B}[{_C}?{_B}]{_E}'
_V = f' {_B}[{_C}*{_B}]{_E}'

_AUTOR = f' {_B}[{W} Json Security{_B} ] {RESET}{_C}'
_GITHUB = f'{_B}[{W} http://github.com/JsonSecurity{_B} ]{RESET}{_C}'
_SCRIPT = f'{_B}[{W} pngDrop {_B} ] {RESET}{_C}'

bb = N
yy = G
banner = f"""{_C}
                              ____                              
                             /\\  _`\\                            
  _____     ___       __     \\ \\ \\/\\ \\   _ __    ___    _____   
 /\\ '__`\\ /' _ `\\   /'_ `\\    \\ \\ \\ \\ \\ /\\`'__\\ / __`\\ /\\ '__`\\ 
 \\ \\ \\L\\ \\/\\ \\/\\ \\ /\\ \\L\\ \\    \\ \\ \\_\\ \\\\ \\ \\/ /\\ \\L\\ \\\\ \\ \\L\\ \\
  \\ \\ ,__/\\ \\_\\ \\_\\\\ \\____ \\    \\ \\____/ \\ \\_\\ \\ \\____/ \\ \\ ,__/
   \\ \\ \\/  \\/_/\\/_/ \\/___L\\ \\    \\/___/   \\/_/  \\/___/   \\ \\ \\/ 
    \\ \\_\\             /\\____/                             \\ \\_\\ 
     \\/_/             \\_/__/                               \\/_/  

     {_AUTOR} {_GITHUB} {_SCRIPT}
    """

def bar(time=2, message='Loading', large=60):
    print('')
    
    large -= len(message)
    iteration = time / 100
    for p in range(101):
        i = int(large * (p / 100))
        barra = '█' * i + '-' * (large - i)
        print(f'\r{_E} {message}:{Y} |{barra}| {_E} {p}%', end='')
        sleep(iteration)
    print('')

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
