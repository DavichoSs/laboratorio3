##TRIANGULO
import math

def perimetroT(l1,l2,l3):
	return l1+l2+l3

def s(a,b,c):
    return (a+b+c)/2
 
def areaT(a,b,c):
    return round(math.sqrt((s(a,b,c)*(s(a,b,c)-a))*(s(a,b,c)-b)*(s(a,b,c)-c)),2)
 
##CUADRADO
def perimetroC(la):
    return la*4
 
def areaC(lado):
    return lado*lado

##PENTAGONO
def perimetroP(lad):
	return lad*5

def areaP(peri,apot):
	return (peri*apot)/2

##MENU DE OPCIONES
print("MENU\n"+"3.- TRIANGULO\n"+"4.- CUADRADO\n"+"5.- PENTAGONO")
i=int(input("Seleccione una opcion: "))
if i==3:
	a=float(input("Ingrese lado 1: "))
	b=float(input("Ingrese lado 2: "))
	c=float(input("Ingrese lado 3: "))
	print("Area: "+str(areaT(a,b,c))+"\nPerimetro: "+str(perimetroT(a,b,c)))
elif i==4:
	m=float(input("Ingrese el lado: "))
	print("Perimetro: "+str(perimetroC(m)))
	print("Area: "+str(areaC(m)))
elif i==5:
	apot=float(input("Ingrese el apotema: "))
	lado=float(input("Ingrese el lado: "))
	print("Perimetro: "+str(perimetroP(lado))+"\nArea: "+str(areaP(perimetroP(lado),apot)))
else:
	print("El numero no es valido")