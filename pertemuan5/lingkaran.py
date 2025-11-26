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
