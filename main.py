import turtle
def shape(sides):
  for i in range(sides):
    turtle.fd(50)
    turtle.rt(360/sides)
turtle.color('red')
shape(6)
