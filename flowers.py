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

t.penup()
t.speed(40)
t.goto(-200, 200)
a = abs(t.pos())
t.pendown()
t.begin_fill()
t.color('yellow')
while True:
    t.forward(150)
    t.left(170)
    b = abs(t.pos())
    if (a - 1 < b < a + 1):
        break
t.end_fill()
t.penup()

def draw_rainbow(start_x, color):
    t.goto(start_x - 200, 0)
    t.color(color)
    t.pendown()
    t.seth(90)
    t.circle(-240+start_x, 180)
    t.penup()

t.penup()

t.colormode(255)

colors = ['violet', 'indigo', 'blue', 'green', 'yellow', 'orange', 'red']

for j in range(7):
    for i in range(10):
            draw_rainbow(10*j+i, colors[j])

def draw_square(color, x=0, y=0, size=70):
    t.goto(x,y)
    t.begin_fill()
    t.pendown()
    t.color(color, 'red')
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(size)
    t.left(90)
    t.fillcolor(color)
    t.penup()
    t.end_fill()

def draw_flower(strong, x, y, size=60):
    draw_square((int(255*strong), int(128*strong), int(255*strong)), x - size, y - size, size)
    draw_square((int(255*strong), int(214*strong), int(51*strong)), x - size, y + size, size)
    draw_square((int(255*strong), int(77*strong), int(136*strong)), x + size, y + size, size)
    draw_square((int(77*strong), int(184*strong), int(255*strong)), x + size, y - size, size)
    draw_square((int(255*strong), int(255*strong), int(26*strong)), x, y, size)



t.colormode(255)
t.bgcolor(133, 238, 0)
for number in range(5):
    draw_flower(0.5, number * 100+50, number * 10, 30)
    draw_flower(0.5, number * -100-50, number * 10, 30)

    draw_flower(0.8, number * 150+65, number * 20 - 150, 40)
    draw_flower(0.8, number * -150-65, number * 20 - 150, 40)

    draw_flower(1, number * 200+80, number * 30 - 350, 50)
    draw_flower(1, number * -200-80, number * 30 - 350, 50)

t.color('blue')
t.shape("turtle")

t.hideturtle()

t.exitonclick()