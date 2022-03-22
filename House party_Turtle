#Samuel Rangira
#10/20/2021

#party time
import random
import turtle
from turtle import *
t = turtle.Turtle()
t.speed(0)
t.pensize(2)

for i in range(6):#creating a circle spirography lighting system
    for colours in ["red", "blue", "green", "yellow", "magenta", "pink", "white"]:
        t.color(colours)
        t.circle(200)
        t.left(10)

t.hideturtle()
    


colors = ["red", "green", "blue", "yellow", "pink", "orange"]#colors for circular lights
for i in range(200):# creating a loop for circular lights
    h = 200
    x = random.randint(-300,300)
    y = random.randint(30,300)
    circle_size = random.randint(10,30)
    circle_color = random.choice(colors)
    t.goto(x,y)
    t.color(circle_color)
    t.begin_fill()
    t.circle(circle_size)
    t.end_fill()
    t.up()
    if h > 200:
        break 
    

def draw_head(t,x,y,r):#drawing the head 
    t.setheading(0)
    t.up()
    t.goto(x,y)
    t.down()
    t.color("black")
    t.begin_fill()
    t.circle(r)
    t.end_fill()

def draw_body(t,x,y,r):#drawing the rest of the body 
    t.up()
    t.goto(x,y)
    t.down()
    t.goto(x,-15)
    t.setheading(270)
    t.left(45)
    t.forward(10)
    t.goto(x,-15)
    t.right(90)
    t.forward(10)
    t.goto(x,-15)
    t.setheading(90)
    t.goto(x,15)
    t.right(random.randint(20,170))
    t.forward(10)
    t.goto(x,15)
    t.setheading(90)
    t.left(random.randint(20,170))
    t.forward(10)
    t.goto(x,15)
    draw_head(t,x,y,r) 

x = -300  
for i in range(9):# loop to draw multiple people with head and body
    x = x + 50
    y = 30
    r = 10
    draw_body(t,x,y,r)
    
turtle.bgcolor('brown')


for x in range (1, 100):#creating a stage 
    t.color("grey")
    t.up()
    t.goto(-10,-22)
    t.down()
    t.forward(2*x)
    t.left(90)
   
for x in range (1, 100):#creating a stage 
    t.color("grey")
    t.up()
    t.goto(-100,-22)
    t.down()
    t.forward(2*x)
    t.left(90)









































