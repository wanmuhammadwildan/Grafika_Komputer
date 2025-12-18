import turtle
import math
# -------------------------------------------------
# Program Grafika 2D Rumah
# Menerapkan 4 Materi Wajib:
# 1. Algoritma Garis DDA
# 2. Algoritma Lingkaran Midpoint
# 3. Algoritma Poligon
# 4. Transformasi Geometri 2D (Translasi)
# -------------------------------------------------

# ===================== SETUP LAYAR =====================
screen = turtle.Screen()
screen.title("Rumah 2D - Lengkap 4 Materi")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("white")

# ===================== 1. GARIS DDA =====================
def draw_line_DDA(x1, y1, x2, y2):
    """
    Menggambar garis menggunakan algoritma DDA
    """
    dx = x2 - x1
    dy = y2 - y1
    steps = int(max(abs(dx), abs(dy)))

    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    t.penup()
    t.goto(round(x), round(y))
    t.pendown()

    for i in range(steps):
        x += x_inc
        y += y_inc
        t.goto(round(x), round(y))

# ===================== 2. LINGKARAN MIDPOINT =====================
def draw_circle_midpoint(cx, cy, r):
    """
    Menggambar lingkaran menggunakan algoritma Midpoint Circle
    """
    x = 0
    y = r
    p = 1 - r

    def plot(x, y):
        points = [
            (cx + x, cy + y), (cx - x, cy + y),
            (cx + x, cy - y), (cx - x, cy - y),
            (cx + y, cy + x), (cx - y, cy + x),
            (cx + y, cy - x), (cx - y, cy - x)
        ]
        for px, py in points:
            t.penup()
            t.goto(px, py)
            t.pendown()
            t.dot(3)

    plot(x, y)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot(x, y)

# ===================== 3. POLIGON =====================
def draw_polygon(points):
    """
    Menggambar poligon dari kumpulan titik
    """
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        draw_line_DDA(x1, y1, x2, y2)

# ===================== 4. TRANSFORMASI (TRANSLASI) =====================
def translate(points, tx, ty):
    """
    Translasi (menggeser objek)
    """
    return [(x + tx, y + ty) for x, y in points]

# ===================== GAMBAR RUMAH =====================

# ---- DINDING RUMAH (GARIS DDA) ----
draw_line_DDA(-100, -60, 100, -60)
draw_line_DDA(100, -60, 100, 40)
draw_line_DDA(100, 40, -100, 40)
draw_line_DDA(-100, 40, -100, -60)

# ---- PINTU (GARIS DDA) ----
draw_line_DDA(-20, -60, -20, 10)
draw_line_DDA(20, -60, 20, 10)
draw_line_DDA(-20, 10, 20, 10)

# ---- JENDELA BULAT (MIDPOINT CIRCLE) ----
draw_circle_midpoint(50, 0, 12)

# ---- ATAP (POLIGON SEGITIGA) ----
atap = [(-120, 40), (0, 120), (120, 40)]
draw_polygon(atap)

# ---- TRANSFORMASI: ATAP DITRANSLASI ----
atap_pindah = translate(atap, 0, 25)
draw_polygon(atap_pindah)

# ===================== SELESAI =====================
turtle.done()
