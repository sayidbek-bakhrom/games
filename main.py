import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False


screen.exitonclick()