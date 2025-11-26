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

<img width="394" height="323" alt="Screenshot 2025-11-26 141617" src="https://github.com/user-attachments/assets/9c89dac5-1a15-491a-8641-1416e52c18ac" />

import turtle

# Fungsi untuk menggambar 8 titik simetri
def plot_circle_points(xc, yc, x, y):
    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]

    for point in points:
        turtle.penup()
        turtle.goto(point)
        turtle.dot(4, "red")

# Algoritma Midpoint
def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    plot_circle_points(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x + 1 - 2 * y

        plot_circle_points(xc, yc, x, y)

# Main program
turtle.speed(0)
turtle.title("Midpoint Circle Algorithm")

midpoint_circle(0, 0, 100)

turtle.done()

<img width="575" height="534" alt="Screenshot 2025-11-26 141118" src="https://github.com/user-attachments/assets/c12a039f-74ee-4eab-9bdd-510485d5e705" />

import turtle

# Algoritma DDA
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
        turtle.dot(6, "blue")
        turtle.pendown()
        x += x_inc
        y += y_inc

# Gambar poligon (segitiga)
def draw_polygon(points):
    n = len(points)
    for i in range(n):
        x1, y1 = points[i]
        x2, y2 = points[(i+1) % n]  # titik terakhir kembali ke titik pertama
        draw_line_DDA(x1, y1, x2, y2)
# MAIN PROGRAM
turtle.speed(0)
turtle.title("Poligon Segitiga - DDA")

# Titik segitiga sesuai PPT (dikalikan 20 supaya besar)
points = [(2*20, 2*20), (6*20, 2*20), (4*20, 6*20)]
draw_polygon(points)
turtle.done()


<img width="221" height="259" alt="Screenshot 2025-11-26 141427" src="https://github.com/user-attachments/assets/c02089b6-f90c-4afd-9400-a7ba90607146" />





