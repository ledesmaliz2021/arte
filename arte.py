from turtle import *
import random
title('Artes en Python')
bgcolor("black")
pencolor('white')

#Crear una animacion de figuras  a partir de lineas  
speed(0)
x=1
while x<400:
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colormode(255)
    pencolor(r,g,b)
    forward(5+x)
    right(200)# se puede modificar (200 una estrella)(20 espiral)
    x+=1
mainloop()

