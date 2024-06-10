import turtle
import random
import time
import math
from functions import countdown, makeTurtle, setupScoreTurtle
from repeatTimer import RepeatTimer

screen = turtle.Screen()
screen.bgcolor("light blue")
screen.title("Catch The Turtle")
score = 0
xOld = 0
yOld = 0
pulse = 0
countFrom = 20
FONT = ("Arial", 30, "normal")

t = makeTurtle(0, 0)

scoreTurtle = setupScoreTurtle(screen)
countdownTimer = countdown(screen)

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
