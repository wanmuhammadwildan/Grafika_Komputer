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

# ----------------------------
# MAIN PROGRAM
# ----------------------------
turtle.speed(0)
turtle.title("Poligon Segitiga - DDA")

# Titik segitiga sesuai PPT (dikalikan 20 supaya besar)
points = [(2*20, 2*20), (6*20, 2*20), (4*20, 6*20)]

draw_polygon(points)

turtle.done()
