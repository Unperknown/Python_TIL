from turtle import *
import turtle
t = turtle.Turtle()
t.shape("turtle")

def taegeuk(t, n):
    t.circle(n)
    t.up()
    t.left(180)
    t.forward(n)
    t.right(90)
    t.forward(n)
    t.down()
    t.left(180)
    t.circle(n / 2, -180)
    t.right(180)
    t.circle(n / 2, 180)
