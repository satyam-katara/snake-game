from turtle import   Screen
from  Snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Katara snake game")
screen.tracer(0)
snake=Snake()
food=Food()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# segment_1=Turtle("square")this the convention method of creating three square one after another
# segment_1.color("white")
# segment_2=Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)
# segment_3=Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)
# starting_position=[(0,0),(-20,0),(-40,0)]
# segments=[]
# for position in starting_position:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)



game_is_on=True
while game_is_on:

    screen.update()
    time.sleep(0.3)
    snake.move()


    #Detect collision with food
    if snake.head.distance(food) <15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
       scoreboard.reset()
       snake.reset()

       # game_is_on=False
        # scoreboard.game_over()

    #Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment==snake.head:
            pass
        if snake.head.distance(segment)<10:
            scoreboard.reset()
            snake.reset()


            # game_is_on=False
            # scoreboard.game_over()
    # for seg_num in range(len(segments)-1,0,-1):
    #     new_x=segments[seg_num-1].xcor()
    #     new_y=segments[seg_num - 1].ycor()
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)

















screen.exitonclick()