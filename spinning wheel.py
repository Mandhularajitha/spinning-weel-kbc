import tkinter

from turtle import *
setup()
t1=Turtle()
colour=["red","blue","green","yellow","purple","orange"]

import random
t1.up()
t1.go(-200,0)
t1.down()
t1.width(5)
t1.hideturtle()

for i in range(9001):
    colourchoice=random.choice(color)
    t1.colour(colourchoice)
    t1.forward(181)
    
