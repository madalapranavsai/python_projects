from turtle import Screen
from food import *
from snake import *
from scoreboard import *

import time



screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

madhu = Snake()
food = Food()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(madhu.up, "Up")
screen.onkey(madhu.down, "Down")
screen.onkey(madhu.left, "Left")
screen.onkey(madhu.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    madhu.move()
    if madhu.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        madhu.extend_segment()
    if madhu.head.xcor() < -280 or madhu.head.xcor() > 280 or madhu.head.ycor() > 280 or madhu.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
    for segment in madhu.segments[1:]:

        if madhu.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
screen.exitonclick()
