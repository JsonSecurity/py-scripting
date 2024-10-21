from math import sqrt as raiz

x = [];
y = [];


print("[+] Ingrese 777 para calcular\n")

vx = True
while vx:
	valx = float(input("[x]: "))
	if valx ==  777:
		vx = False
	else:
		x.append(valx)

print(" ")
vy = True
while vy:
	valy = int(input("[y]: "))
	if valy == 777:
		vy = False
	else:
		y.append(valy)

print("\n[+] Calculos\n")

xy = []
xc = []
yc = []
for i in range(len(x)):
	mult = x[i] * y[i]
	cx = x[i] ** 2
	cy = y[i] ** 2

	xy.append(mult)
	xc.append(cx)
	yc.append(cy)

n = len(x)
sumx = sum(x)
sumy = sum(y)
sumxy = sum(xy)
sumxc = sum(xc)
sumyc = sum(yc)

print("N = ",n)
print(sumx)
print(sumy)
print(xy,sumxy)
print(xc,sumxc)
print(yc,sumyc)
print("")

superior = (n*sumxy) - (sumx * sumy)
inferior = raiz(((n*sumxc)-(sumx**2)) * ((n*sumyc)-(sumy**2)))

print('(',n,'*',sumxy,'',')-(',sumx,'*',sumy,') =',superior)
print('------------------------------------------------------------------------------------')
print('[(',n,'*',sumxc,') - (',sumx,'**',2,'] * [(',n,'*',sumyc,') - (',sumy,'**',2,'] =',inferior)

repuesta = superior/inferior
print("\n r=",repuesta)
print("")

if repuesta >= 0.9:
	print("C. perfecta")
elif repuesta < 0.9 and repuesta >= 0.8:
	print("C. excelente")
elif repuesta < 0.8 and repuesta >= 0.6:
	print("C. regular")
elif repuesta < 0.6 and repuesta >= 0.3:
	print("C. Mala")
elif repuesta < 0.3:
	print("no hay C.")
