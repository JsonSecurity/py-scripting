list = []

for i in range(5):
    val = int(input("[?] "))
    list.append(val)

Intercambio = True
while Intercambio:
    Intercambio = False
    for i in range(len(list)-1):
        if list[i] > list[i+1]:
            Intercambio = True
            list[i], list[i+1] = list[i+1], list[i]
print(list)
