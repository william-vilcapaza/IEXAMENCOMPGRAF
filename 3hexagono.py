import turtle

colors = ["cyan", "yellow", "blue", "green", "white", "red"]
sketch = turtle.Pen()

turtle.bgcolor("black")
for i in range(300):
    sketch.pencolor(colors[i%6])
    sketch.width(i/100+2)
    sketch.forward(i)
    sketch.left(59)