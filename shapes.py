from turtle import *

def square(size,x,y):
    penup()
    goto(x,y)
    pendown()
    for a in range(1,5):
        forward(size)
        left(90)

def squareColor(size,x,y,color1,color2):
    color(color1,color2)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for a in range(1,5):
        forward(size)
        left(90)
    end_fill()
    

def triangle(size,x,y):
    penup()
    goto(x,y)
    pendown()
    for x in range(3):
        forward(size)
        left(120)

def triangleColor(size,x,y,color1,color2):
    color(color1,color2)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for x in range(3):
        forward(size)
        left(120)
    end_fill()

def rectangle(length,width,x,y):
    penup()
    goto(x,y)
    pendown()
    for x in range(1,3):
        forward(width)
        lt(90)
        forward(length)
        lt(90)

def rectangleColor(length,width,x,y,color1,color2):
    color(color1,color2)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for x in range(1,3):
        forward(width)
        lt(90)
        forward(length)
        lt(90)
    end_fill()

def poligon(size,corners,x,y):
    angle=360/corners
    penup()
    goto(x,y)
    pendown()
    for x in range(corners):
        forward(size)
        lt(angle)

def poligonColor(size,corners,x,y,color1,color2):
    angle=360/corners
    color(color1,color2)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for x in range(corners):
        forward(size)
        lt(angle)
    end_fill()

def star(size,x,y):
    color('black')
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
        forward(size)
    end_fill()

def starColor(size,x,y,color1,color2):
    color(color1,color2)
    penup()
    goto(x,y)
    pendown()
    begin_fill()
    for i in range(5):
        forward(size)
        right(144)
        forward(size)
    end_fill()

def crescent(size,x,y,color1,color2,backgroundColor):
    penup()
    goto(x,y)
    pendown()
    color(color1,color2)
    begin_fill()
    circle(size)
    end_fill()
    if size >= 45 and size <= 56:
        N=size-100
        x1=x+30
        y2=y+100
        penup()
        goto(x1,y2)
        pendown()
        color(backgroundColor)
        begin_fill()
        circle(N)
        end_fill()
    elif size < 45 and size > 30:
        x1=x+x-26
        y1=y+1
        penup()
        goto(x1,y1)
        pendown()
        color(backgroundColor)
        begin_fill()
        circle(size)
        end_fill()
    elif size < 31 and size >= 25:
        x1=x+x-30
        y1=y+1
        penup()
        goto(x1,y1)
        pendown()
        color(backgroundColor)
        begin_fill()
        circle(size)
        end_fill()
    elif size < 25:
        print("Nuh uh")
    elif size > 150:
        print("Nuh uh")
    elif size > 56 and size <=150:
        N=size/100
        x1=x+40
        y2=y
        penup()
        goto(x1,y2)
        pendown()
        color(backgroundColor)
        begin_fill()
        circle(size)
        end_fill()

def background(backgroundColor):
    color(backgroundColor)
    begin_fill()
    square(1700,-850,-400)
    end_fill()


















    


