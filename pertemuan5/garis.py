import turtle
import time

# Fungsi Algoritma DDA
def draw_line_DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    x_inc = dx / steps
    y_inc = dy / steps

    x = x1
    y = y1
    
    for i in range(steps):
        turtle.penup()
        turtle.goto(round(x), round(y))
        turtle.dot(5, "black")  # menggambar titik
        turtle.pendown()
        x += x_inc
        y += y_inc

# Main program
turtle.speed(0)
turtle.title("Garis - Algoritma DDA")

draw_line_DDA(-100, -50, 100, 80)

turtle.done()
