import turtle

a = int(input("Square length="))
sq_color = input("Enter the color for the square: ")
r = int(input("Circle Radius="))
ci_color = input("Enter the color for the circle: ")
b = int(input("Triangle side length="))
tr_color = input("Enter the color for the triangle: ")


drawer = turtle.Turtle()
drawer.speed(3)

def draw_square(length, color):
    drawer.penup()
    drawer.goto(200, 200)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(length)
        drawer.right(90)
    drawer.end_fill()

def draw_circle(radius, color):
    drawer.penup()
    drawer.goto(50, 50)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()
    drawer.circle(radius)
    drawer.end_fill()

def draw_triangle(length, color):
    drawer.penup()
    drawer.goto(-200, -200)
    drawer.pendown()
    drawer.fillcolor(color)
    drawer.begin_fill()
    for _ in range(3):
        drawer.forward(length)
        drawer.left(120)
    drawer.end_fill()

def clear_and_start_over():
    drawer.clear()
    drawer.penup()
    drawer.goto(0, 0)
    drawer.pendown()

# Draw the shapes
draw_square(a, sq_color)
draw_circle(r, ci_color)
draw_triangle(b, tr_color)

# Clear the drawing
#clear_and_start_over()

turtle.done()
