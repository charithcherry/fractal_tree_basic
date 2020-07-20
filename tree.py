import turtle
from turtle import  *
hr=turtle.Turtle()
hr.left(90)
hr.speed(15000)

hr.color('brown','green')
def pat():
        l = ['red', 'green', 'yellow', 'blue', 'orange']

        for x in range(15):
                hr.color(l[x % 5])
                hr.pensize(x / 10 + 1)
                hr.forward(x)
                hr.left(90)  # 59


def t(i):
    if i<10:
        return
    else:
            hr.forward(i)
            hr.left(30)
            hr.begin_fill()
            hr.circle(5)
            hr.end_fill()
            t(3*i/4)
            hr.right(60)
            hr.begin_fill()
            hr.circle(5)
            hr.end_fill()
            t(3*i/4)
            hr.left(30)
            hr.backward(i)


t(100)

turtle.done()
