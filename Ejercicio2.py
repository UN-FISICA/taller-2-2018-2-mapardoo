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

lados = input("Ingrese el numero de lados de los poligonos a dibujar: ")
if int(lados)<3:
	print("Reinicie el codigo e ingrese un numero mayor o igual a 3")
else:
	turtle.up()
	turtle.setx(50)
	turtle.sety(-50)

	for j in range(0,4):
		figura(int(lados))
		turtle.lt(90*(j+1))
		turtle.fd(100)
		turtle.rt(90*(j+1))
		
	turtle.done()
