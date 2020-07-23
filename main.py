import turtle
turtle.title("My turtle drawing")
turtle.bgcolor("green")
turtle.shape("turtle")
turtle.setup(600,600)
sally = turtle.Turtle() 

def circle(length,color):
  sally.fillcolor(color)
  sally.begin_fill() 
  sally.circle(int(length))
  sally.end_fill

def square(length,color):
  for i in range(4):
    sally.forward(length)
    sally.right(90)
  

circle(100,"hotpink")
sally.penup()
sally.goto(-200,-200)
sally.pendown()
square(100,"red")
