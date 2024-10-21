import os

autorizedKey = 'admin'

T = " [+] "
F = " [-] "
Q = " [?] "
N = " [#] "

def clasification(residuo):
    verde = [
        "papel",
        "carton",
        "vidrio",
        "plastico",
        "textiles",
        "madera",
        "cuero",
        "metales"
    ]
    marron = [
        "comida",
        "plantas",
        "fruta",
        "lacteos",
        "verdura",
        "huesos",
        "semillas",
        "flores"
    ]
    negro = [
        "servilletas",
        "comida",
        "ceramica",
        "cigarro",
        "pañales",
        "paño"
    ]
    rojo = [
        "",
        "",
        "mercurio",
        "fenoles",
        "pila",
        "bateria",
        "electrodomestico",
        "medicamentos",
        "plaguisidas"
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
            Name = input("\n" + Q + "Nombre: ")
            ent = int(Name)
            print(F + "No puede poner números\n")
        except:
            name = False

    dni = True
    while dni:
        try:
            DNI = int(input(N + "N° DNI: "))
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
            PassWd = input("\n" + T + "Clave de identificación [DNI]: ")

            if PassWd == autorizedKey:
                autorized()
            else:
                ent = int(PassWd) 
                with open("autorized.txt", "r") as file:
                    for line in file:
                        if str("[DNI]: " + PassWd) in str(line):
                            key = True
                            break
                if key:
                    passwd = False
                else:
                    print(F + "Clave erronea")
        except ValueError:
            print(F + "No puede ingresar letras")
        
def start():
    os.system('clear')
    print("\n" + T + 'Precione "ENTER" para reiniciar')
    trash = True
    while trash:
        try:
            Trash = input("\n" + Q + "Ingrese el tipo de residuo: ").lower()

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
