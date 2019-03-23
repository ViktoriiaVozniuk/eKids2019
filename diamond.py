from turtle import *

def draw_shape(sides, length):
    begin_fill()
    for _ in range(sides):
        forward(length)
        right(360 / sides)
        #fillcolor("green")
    end_fill()

def draw_mat_rix(mat_rix):
    startX = -200
    startY = 200
    shapeSide = 50
    for row in range (len (mat_rix)):
        for col in range (len(mat_rix[row])):
            cell = mat_rix [row][col]
            if cell == 1 :
                fillcolor ("red")
            else :
                fillcolor ("pink")
            curX = startX + shapeSide * col
            curY = startY - shapeSide * row
            goto (curX, curY)
            draw_shape(4,shapeSide )
mat_rix = [
          [0, 1, 1, 0, 0, 1, 1, 0],
          [1, 1, 1, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1, 1, 1, 1],
          [0, 1, 1, 1, 1, 1, 1, 0],
          [0, 0, 1, 1, 1, 1, 0, 0],
          [0, 0, 0, 1, 1, 0, 0, 0]
         ]

setup (width=600, height=600, startx=0, starty=0)
color('yellow')
# shape("turtle")
hideturtle()
speed(30)
draw_mat_rix(mat_rix)

exitonclick()
