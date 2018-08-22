from turtle import *
import turtle
t = turtle.Turtle()
t.shape("turtle")

for i in range(500):
    t.forward(150)
    t.left(60)
    if i % 6 == 0:
        t.right(25)
