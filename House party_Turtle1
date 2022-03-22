#Samuel Rangira
#09/30/2021

import random
import turtle
t = turtle.Turtle()
t.speed(0)

for i in range(10):
    x = random.randint(0,10)
    print(x)


def rand_color():# picks and returns a random color 
    x = random.randint(0,4)
    color = "black"
    #print(x)
    if(x==0):#if block 
        color="yellow"
    elif(x==1):
        color = "purple"
    elif(x == 2):
        color = "red"
    elif(x== 3):
        color = "orange"
    elif(x==4):
        color = "blue"
    else:
        print("Something is wrong")
    return(color)


t = turtle.Turtle()
screen = t.getscreen()
width = screen.window_width()
height = screen.window_height()
print(width)
print(height)

for i in range(10):
    x = random.randint(-width//2, width//2)
    y = random.randint(-height//2,height//2)
    t.up()
    t.goto(x,y)
    t.down()
    color = rand_color()
    t.color(color)
    #print(color)
    t.circle(10)



#My trial in drawing hats on top of a circle. 
t = turtle.Turtle()
screen = t.getscreen()
width = screen.window_width()
height = screen.window_height()
def draw_hat():
    x = random.randint(-width//2,width//2)
    y = random.randit(-height//2,width//2)

for i in range(10):
    x = random.randint(-width//2,width//2)
    y = random.randint(-height//2,width//2)
    t.up()
    t.goto(x,y)
    t.down()
    t.forward(25)
    t.left(90)
    t.forward(25)
    t.left(120)
    t.forward(25)

    
 
def rand_color():# picks and returns a random color 
    x = random.randint(0,4)
    color = "black"
    #print(x)
    if(x==0):#if block 
        color="yellow"
    elif(x==1):
        color = "purple"
    elif(x == 2):
        color = "red"
    elif(x== 3):
        color = "orange"
    elif(x==4):
        color = "blue"
    else:
        print("Something is wrong")
    return(color)


def drawhat(t,x,y,r):
    t.up()
    t.goto(x,y+2*2-r//5)
    color = rand_color()
    t.color(color)
    t.begin_fill()
    t.down()
    t.forward(r//2)
    t.left(120)
    t.forward(r)
    t.left(120)
    t.forward(r)
    t.left(120)
    t.forward(r/2)
    t.end_fill()
 

def draw_head(t,x,y,r):
    x = random.randint(-width//2, width//2)
    y = random.randint(-height//2,height//2)
    t.up()
    t.goto(x,y)
    t.down()
    t.circle(10)
    drawhat(t,x,y,r)

t = turtle.Turtle()
screen = t.getscreen()
width = screen.window_width()
height = screen.window_height()


for i in range(10):
    x = random.randint(-width//2, width//2)
    y = random.randint(-height//2,height//2)
    r = random.randint(10,50)
    draw_head(t,x,y,r)



