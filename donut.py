import turtle as t
import random
timmy = t.Turtle()

t.colormode(255)
timmy.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_need = (r, g, b)
    return random_color_need


def draw_spirograph(size_gap):
    for _ in range(int(720 / size_gap)):
        timmy.penup()
        timmy.right(1)
        timmy.forward(5)
        timmy.pendown()
        timmy.color(random_color())
        timmy.circle(50)
        timmy.setheading(timmy.heading() + size_gap)


timmy.penup()
timmy.forward(350)
timmy.right(90)
timmy.forward(100)
timmy.left(180)
timmy.pendown()

draw_spirograph(2)

screen = t.Screen()
screen.exitonclick()
