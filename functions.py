import turtle

FONT = ("Arial", 30, "normal")

def countdown(screen):
    countdownTurtle = turtle.Turtle()
    countdownTurtle.hideturtle()
    countdownTurtle.color("dark blue")
    countdownTurtle.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.8
    countdownTurtle.setpos(0, y)
    countdownTurtle.write(arg="Time: 20", move=False, align="center", font=FONT)
    return countdownTurtle

def setupScoreTurtle(screen):
    scoreTurtle = turtle.Turtle()
    scoreTurtle.hideturtle()
    scoreTurtle.color("dark blue")
    scoreTurtle.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.9
    scoreTurtle.setpos(0, y)
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)
    return scoreTurtle

def makeTurtle(x, y):
    t = turtle.Turtle()
    t.speed(6)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    return t

