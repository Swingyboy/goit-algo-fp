import turtle


def draw_pythagoras_tree(t, length, level):
    if level == 0:
        return
    t.forward(length)
    t.left(45)
    draw_pythagoras_tree(t, length * 0.7071, level - 1)
    t.right(90)
    draw_pythagoras_tree(t, length * 0.7071, level - 1)
    t.left(45)
    t.backward(length)


if __name__ == "__main__":
    level = int(input("Enter recursion depth:"))

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.left(90)
    draw_pythagoras_tree(t, 100, level)

    turtle.done()
