import turtle
t = turtle.Turtle()
t.shape("turtle")

def pentagon(t, n, x, y):
    t.up()
    t.goto(x, y)
    t.down()
    
    for i in range(1, 4):
        t.circle(n)
        t.up()
        t.forward(1.9 * n)
        t.down()

    t.up()
    t.goto(x + 2.9 * n, y + 0.8 * n)
    t.down()
    t.right(180)

    for i in range(1, 3):
        t.circle(n)
        t.up()
        t.forward(n * 2)
        t.down()

pentagon(t, 100, -100, -100)
