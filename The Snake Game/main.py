from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
import winsound

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0) 

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_paused = False

def toggle_pause():
    global game_is_paused
    game_is_paused = not game_is_paused

screen.onkey(toggle_pause, "space")

scoreboard.start_scoreboard()
game_is_on = True
speed = 0.1  

while game_is_on:
    if not game_is_paused:
        screen.update()
        time.sleep(speed)
        snake.move()

        if snake.head.distance(food) < 15:
            winsound.PlaySound("eat_sound.wav", winsound.SND_ASYNC) 
            scoreboard.increase_scoreboard()
            snake.extend_when_eats()
            food.refresh()
            speed *= 0.9 

        if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
            winsound.PlaySound("game_over.wav", winsound.SND_ASYNC) 
            game_is_on = False
            scoreboard.game_over()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                winsound.PlaySound("game_over.wav", winsound.SND_ASYNC)  
                game_is_on = False
                scoreboard.game_over()

screen.exitonclick()
