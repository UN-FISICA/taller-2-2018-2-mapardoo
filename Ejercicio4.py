import turtle
import math

def figura(lados):
	turtle.rt(90)
	turtle.fd(20/(2*math.tan(math.pi/lados))) #apotema
	turtle.lt(90)
	turtle.fd(10)
	turtle.down()
	for i in range(0,lados):
		turtle.lt(360/lados)
		turtle.fd(20) #longitud de los lados
	turtle.up()
	turtle.bk(10)
	turtle.lt(90)
	turtle.fd(20/(2*math.tan(math.pi/lados)))
	turtle.rt(90)

filas = input("Ingrese el numero de filas de la piramide: ")
lados = input("Ingrese el numero de lados de los poligonos a dibujar: ")
if(int(lados)<3 or int(filas)<1):
	if(int(lados)<3):
		print("Reinicie el codigo e ingrese un numero de lados mayor o igual a 3")
	else:
		print("Reinicie el codigo e ingrese un numero de filas mayor o igual a 1")
else:
	turtle.up()
	turtle.sety(300)
	
	for j in range(0,int(filas)):
		turtle.setx(-5*j*((int(lados)//2)+5))
		for k in range(0,j+1):
			figura(int(lados))
			turtle.fd(10*((int(lados)//2)+5))
		turtle.setx(0)
		turtle.rt(90)
		turtle.fd(18*((int(lados)//3)+1))
		turtle.lt(90)
		
	turtle.done()
