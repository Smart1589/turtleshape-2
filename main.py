import turtle
def shape(sides):
  for i in range(sides):
    turtle.fd(20)
    turtle.rt(360/sides)
turtle.color('red')
shape(10)
for n in range(9):
  turtle.fd(50)
  shape(4)