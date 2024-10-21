import os

R = "\033[31m"    # Red
G = "\033[32m"    # Green
Y = "\033[33m"    # Yellow
B = "\033[34m"    # Blue
P = "\033[35m"    # Pink
C = "\033[36m"    # Cyan
L = "\033[37m"    # Lead
W = "\033[0m"    # White

autorizedKey = 'admin'

T = L + " [" + G + "+" + L + "] " + W
F = L + " [" + R + "-" + L + "] " + W
FF = L + " [" + R + "!" + L + "] " + W
Q = L + " [" + C + "?" + L + "] " + W
N = L + " [" + C + "#" + L + "] " + W

def clasification(residuo):
    verde = [
        "papel",
        "carton",
        "vidrio",
        "plastico",
        "textil",
        "madera",
        "cuero",
        "metale"
    ]
    marron = [
        "comida",
        "planta",
        "fruta",
        "lacteo",
        "verdura",
        "hueso",
        "semilla",
        "flor"
    ]
    negro = [
        "servilleta",
        "comida",
        "ceramica",
        "cigarro",
        "pañal",
        "paño"
    ]
    rojo = [
        "",
        "",
        "mercurio",
        "fenol",
        "pila",
        "bateria",
        "electrodomestico",
        "medicamento",
        "plaguisida"
    ]
    if residuo in verde:
        print(T + "Tacho Verde")
    elif residuo in marron:
        print(T + "Tacho Marron")
    elif residuo in negro:
        print(T + "Tacho Negro")
    elif residuo in rojo:
        print(T + "Tacho Rojo")
    else:
        print(F + "No se encontró")

def autorized():
    print("\n" + T + "Rejistro de nuevo usuario")
    name = True
    while name:
        try:
            Name = input("\n" + Q + "Nombre: " + Y)
            ent = int(Name)
            print(F + "No puede poner números\n")
        except:
            name = False

    dni = True
    while dni:
        try:
            DNI = int(input(N + "N° DNI: " + Y))
            dni = False
        except ValueError:
            print(F + "No puede ingresar letras\n")

    DNI = str(DNI)
    with open("autorized.txt", "a") as file:
        file.write("[Nombre]: " + Name + "\n")
        file.write("[DNI]: " + DNI + "\n\n")

def login():
    key = False
    
    passwd = True
    while passwd:
        try:
            PassWd = input("\n" + T + "Clave de identificación [DNI]: " + Y)

            if PassWd == autorizedKey:
                autorized()
            else:
                ent = int(PassWd) 
                with open("autorized.txt", "r") as file:
                    for line in file:
                        if str("[DNI]: " + PassWd) in  str(line):
                            key = True
                            break
                if key:
                    passwd = False
                else:
                    print(FF + "Clave erronea")
        except ValueError:
            print(F + "No puede ingresar letras")
        
def start():
    os.system('clear')
    print("\n" + T + 'Precione "ENTER" para reiniciar')
    trash = True
    while trash:
        try:
            Trash = input("\n" + Q + "Ingrese el tipo de residuo: " + Y).lower()

            if len(Trash) == 0:
                os.system('clear')
                login()
                start()
  
            ent = int(Trash)
            print(F + "No puede poner números\n")
        except ValueError:
            clasification(Trash)
try:
    login()
    start()
except KeyboardInterrupt:
    print(F + "Bye")
