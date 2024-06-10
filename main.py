import turtle
import random
import time
import math
from repeatTimer import RepeatTimer

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
FONT = ("Arial", 30, "normal")
score = 0
xOld = 0
yOld = 0
pulse = 0
countFrom = 20


def setupScoreTurtle():
    scoreTurtle = turtle.Turtle()
    scoreTurtle.hideturtle()
    scoreTurtle.color("dark blue")
    scoreTurtle.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.9
    scoreTurtle.setpos(0, y)
    scoreTurtle.write(arg="Score: 0", move=False, align="center", font=FONT)
    return scoreTurtle


def countdown():
    countdownTurtle = turtle.Turtle()
    countdownTurtle.hideturtle()
    countdownTurtle.color("dark blue")
    countdownTurtle.penup()
    topHeight = screen.window_height() / 2
    y = topHeight * 0.8
    countdownTurtle.setpos(0, y)
    countdownTurtle.write(arg="Time: 20", move=False, align="center", font=FONT)
    return countdownTurtle


def makeTurtle(x, y):
    t = turtle.Turtle()
    t.speed(6)
    t.penup()
    t.shape("turtle")
    t.shapesize(2, 2)
    return t


t = makeTurtle(0, 0)

scoreTurtle = setupScoreTurtle()
countdownTimer = countdown()


def handleClick(x, y):
    global score
    global scoreTurtle
    if countFrom > 0:
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg="Score: {0}".format(score), move=False, align="center", font=FONT)
    else:
        scoreTurtle.clear()
        scoreTurtle.write(arg="Your Final Score: {0}".format(score), move=False, align="center", font=FONT)

def pulseInc():
    global countFrom
    countFrom -= 1


timer = RepeatTimer(1, pulseInc)
timer.start()
if countFrom == 0:
    timer.cancel()

while True:

    x = random.randint(-700, 700)
    y = random.randint(-400, 400)
    tAngle = float(math.atan((y - yOld) / (x - xOld)) * 180 / 3.14)
    if tAngle < 0:
        tAngle = 360 + tAngle
    t.seth(tAngle)
    #print(t.heading())
    t.setpos(x, y)
    t.onclick(handleClick)
    time.sleep(0.5)
    countdownTimer.clear()
    countdownTimer.write(arg="Time: {0}".format(countFrom), move=False, align="center", font=FONT)
    xOld = x
    yOld = y
    if countFrom == 0:
        break
countdownTimer.clear()
countdownTimer.write(arg="Game Over !!!", move=False, align="center", font=FONT)

turtle.mainloop()
