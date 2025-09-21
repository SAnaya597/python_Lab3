import random
import turtle
t = turtle.Turtle()
t.speed(10)
t.hideturtle()
#window to draw in with screen and background color
screen = turtle.Screen()
screen.bgcolor("darkblue")
# Height and width of screen
screen.setup(600, 800)
# clear screen
t.clear()
def draw_square(t, length):
    for _ in range(4):
        t.forward(length)
        t.right(90)


def draw_circle(t, radius):
    t.circle(radius)


def draw_polygon(t, sides,  length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

# part 2
def draw_pumpkin(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("orange")
    t.begin_fill()
    t.circle(radius)
    t.end_fill()
    # STEM
def draw_stem(t, x, y, radius):
    t.penup()
    t.goto(x, y)
    t.fillcolor("green")
    t.begin_fill()
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.left(90)
    t.forward(radius // 2)
    t.left(90)
    t.forward(radius // 5)
    t.end_fill()
def draw_eye(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    draw_polygon(t, 3, size)
    t.end_fill()

def draw_mouth(t, x, y, width):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("yellow")
    t.begin_fill()
    for _ in range(5):
        t.forward(width // 20)
        t.left(60)
        t.forward(width // 10)
        t.right(120)
        t.forward(width // 10)
        t.left(60)
    t.end_fill()


## PART 3
def draw_star(t, x, y, size):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.left(144)  # 144 degrees is the angle to form a star
    t.end_fill()

def draw_sky(t, num_stars):
    for _ in range(num_stars):
        x = random.randint(-300, 300)
        y = random.randint(-100, 300)
        size = random.randint(10, 30)
        draw_star(t, x, y, size)

# PART 4
# Draw three jack-o-lanterns
draw_stem(t, -190, -210, 100)
draw_pumpkin(t, -200, -400, 100)
draw_eye(t, -250, -290, 30)  # Left eye
draw_eye(t, -170, -290, 30)  # Right eye
draw_mouth(t, -260, -350, 190)  # Mouth

draw_stem(t, 5, -250, 100)
draw_pumpkin(t, 0, -400, 80)
draw_eye(t, -40, -315, 25)
draw_eye(t, 15, -315, 25)
draw_mouth(t, -40, -350, 100)

draw_stem(t, 215, -210, 100)
draw_pumpkin(t, 200, -400, 100)
draw_eye(t, 145, -290, 30)
draw_eye(t, 230, -290, 30)
draw_mouth(t, 130, -350, 190)

# Draw the night sky
draw_sky(t, 30)


turtle.exitonclick()