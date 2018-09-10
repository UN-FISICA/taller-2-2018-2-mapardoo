import turtle
import math

def figura(filas):
	n=filas+2
	l=40*math.tan(math.pi/n)*math.cos(math.pi/n) #longitud de los lados
	apot=20*math.cos(math.pi/n) #apotema
	turtle.rt(90)
	turtle.fd(apot)
	turtle.lt(90)
	turtle.fd(l/2)
	turtle.down()
	for i in range(0,n):
		turtle.lt(360/n)
		turtle.fd(l) 
	turtle.up()
	turtle.bk(l/2)
	turtle.lt(90)
	turtle.fd(apot)
	turtle.rt(90)

filas = input("Ingrese el numero de filas de la piramide: ")

if(int(filas)<1 ):
	print("Reinicie el codigo e ingrese un numero de filas mayor o igual a 1")
	
else:
	turtle.up()
	turtle.sety(300)
	for j in range(0,int(filas)):
		turtle.setx(-5*j*((2+(int(filas))//2)+5))
		for k in range(0,j+1):
			figura(j+1)
			turtle.fd(10*((2+(int(filas))//2)+5))
		turtle.setx(0)
		turtle.rt(90)
		turtle.fd(18*((int(filas)//3)+1))
		turtle.lt(90)
		
	turtle.done()
