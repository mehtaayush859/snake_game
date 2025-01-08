from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s = Screen()
# t = Turtle()
s.setup(width = 600, height = 600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

s.listen()
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
    s.update()
    time.sleep(0.1)
    snake.move()

    #Detect food collision with snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detection collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # is_game_on = False
        scoreboard.reset()
        snake.reset()
        
    # Detect the collision with the tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # is_game_on = False
            scoreboard.reset()
            snake.reset()

s.exitonclick()
