import turtle as t
def square(size):
    for i in range(4):
        t.forward(size)
        t.left(90)

window = t.Screen()
size_number = 1

for i in range(10):
    square(size_number)
    size_number += 20
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

