from time import sleep as delay

num = int(input("Ingrese numero [1:10]: "))

list = [0,1,2,3,4,5,6,7,8,9,10]

dis = len(list)

while True:
    div = dis//2
    print(div)
    
    if num > list[div]:
        dis = div +1
        print("der")
    elif num < list[-div]:
        dis = div -1
        print("izq")
    elif num == list[div]:
        print("encontrado. Indice: ",div)
        break
    #print(izq,der)
    delay(.5)

    

