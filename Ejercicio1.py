import turtle
import math

def cuadrado():
	turtle.fd(math.sqrt(200))
	turtle.lt(135)
	turtle.down()
	for i in range(0,4):
		turtle.fd(20) #longitud de los lados
		turtle.lt(90)
	turtle.up()
	turtle.lt(45)
	turtle.fd(math.sqrt(200))

turtle.up()
turtle.lt(45)
turtle.fd(math.sqrt(5000))

for j in range(0,4):
	cuadrado()
	turtle.lt(45)
	turtle.fd(100)
	turtle.lt(45)

turtle.done()
