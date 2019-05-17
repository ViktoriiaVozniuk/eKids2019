#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Техническое задание:
На основе цветочка из квадратов, сделанного в первой итерации,
нарисовать картину из этого цветочка и солнышка.
Солнышко такое как тут, подойдет https://docs.python.org/3.7/library/turtle.html
В будущем ожидаю увидеть поле из разных цветов. Может, сделать цветок красивее.
"""

import turtle as t

import a as a

t.penup()
t.goto(-200,230)
a = abs(t.pos())
t.speed(300)
t.color('yellow')
t.pendown()
t.begin_fill()
while True:
    t.forward(170)
    t.left(190)
    b= abs(t.pos())
    if (a - 1 < b < a +1):
        break
t.end_fill()
t.penup()
#
# def draw_square(color):
#     t.begin_fill()
#     t.pendown()
#     t.color(color, 'red')
#     t.forward(70)
#     t.left(90)
#     t.forward(70)
#     t.left(90)
#     t.forward(70)
#     t.left(90)
#     t.forward(70)
#     t.left(90)
#     t.fillcolor(color)
#     t.penup()
#     t.end_fill()
#
# def draw_flower(shift_x, shift_y):
#     t.goto(shift_x + 60, shift_y + 60)
#     draw_square('purple')
#     t.goto(shift_x - 60, shift_y - 60)
#     draw_square('orange')
#     t.goto(shift_x - 60, shift_y + 60)
#     draw_square('pink')
#     t.goto(shift_x + 60, shift_y - 60)
#     draw_square('blue')
#     t.goto(shift_x, shift_y)
#     t.color('blue')
#     draw_square('yellow')
#
# draw_flower(0, 0)
# draw_flower(0, -250)
# draw_flower(250, -250)
# draw_flower(-250, -250)

def draw_square(length, color):
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()


def draw_flower(shift_x, shift_y, length):
    t.goto(shift_x + length-10, shift_y + length-10)
    draw_square(length, 'purple')
    t.goto(shift_x - (length-10), shift_y - (length-10))
    draw_square(length, 'orange')
    t.goto(shift_x - (length-10), shift_y + length-10)
    draw_square(length, 'pink')
    t.goto(shift_x + length-10, shift_y - (length-10))
    draw_square(length, 'blue')
    t.goto(shift_x, shift_y)
    draw_square(length, 'yellow')

draw_flower(0, 0, 70)
draw_flower(-270, -110, 60)
draw_flower(270, -110, 60)
draw_flower(0, -250, 42)
draw_flower(125, -250, 42)
draw_flower(-125, -250, 42)
draw_flower(250, -250, 42)
draw_flower(-250, -250, 42)

t.shape("turtle")
t.hideturtle()
t.end_fill()
t.penup()


t.done()

t.exitonclick()