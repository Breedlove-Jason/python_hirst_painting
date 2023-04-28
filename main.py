import colorgram
from turtle import Turtle, Screen
import turtle as t
import random

turtle = Turtle()
color_list = [(251, 240, 245), (234, 247, 236), (202, 167, 135), (236, 243, 249), (144, 52, 97), (163, 167, 41),
              (237, 71, 121), (237, 83, 60), (17, 140, 65), (240, 220, 69), (225, 119, 162), (10, 142, 176),
              (65, 198, 218), (23, 169, 129), (158, 59, 52), (130, 187, 160), (109, 41, 85), (247, 232, 1),
              (34, 185, 201)]
# 10 x 10 rows of spots
# dots size 20
# space between dots 50
t.colormode(255)


def draw_grid(num_rows, num_columns, circle_radius, circle_spacing, offset_x, offset_y):
    turtle.speed("fastest")
    turtle.penup()
    for row in range(num_rows):
        for column in range(num_columns):
            x = column * (circle_radius * 2 + circle_spacing) + offset_x
            y = row * (circle_radius * 2 + circle_spacing) + offset_y
            turtle.goto(x, y)
            gen_colors = random.choice(color_list)
            turtle.pencolor(gen_colors)
            turtle.pendown()
            turtle.fillcolor(gen_colors)
            turtle.begin_fill()
            turtle.circle(circle_radius)
            turtle.end_fill()
            turtle.penup()
    turtle.hideturtle()


draw_grid(10, 10, 20, 50, -300, -400)

screen = Screen()
screen.exitonclick()
