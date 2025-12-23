import turtle
import math

# =====================================================
# PROGRAM GRAFIKA KOMPUTER 2D – RUMAH SEDERHANA
#
# MATERI YANG DITERAPKAN:
# 1. Algoritma Garis DDA
# 2. Algoritma Lingkaran Midpoint
# 3. Algoritma Poligon
# 4. Transformasi Geometris 2D (konsep translasi & penyesuaian koordinat)
# =====================================================

# ===================== SETUP LAYAR =====================
screen = turtle.Screen()
screen.title("Rumah 2D - wan ")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("white")

# =====================================================
# 1. ALGORITMA GAMBAR GARIS (DDA)
# Digunakan untuk menggambar semua garis lurus:
# - tanah
# - dinding
# - pintu
# - jendela kotak
# - cerobong
# =====================================================
def draw_line_DDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    # Menentukan jumlah langkah berdasarkan selisih terbesar
    steps = int(max(abs(dx), abs(dy)))

    # Kenaikan nilai x dan y tiap langkah
    x_inc = dx / steps
    y_inc = dy / steps

    x, y = x1, y1
    t.penup()
    t.goto(round(x), round(y))
    t.pendown()

    # Menggambar garis titik demi titik
    for _ in range(steps):
        x += x_inc
        y += y_inc
        t.goto(round(x), round(y))

# =====================================================
# 2. ALGORITMA GAMBAR LINGKARAN (MIDPOINT CIRCLE)
# Digunakan untuk menggambar jendela bulat
# Tanpa menggunakan fungsi circle() bawaan turtle
# =====================================================
def draw_circle_midpoint(cx, cy, r):
    x = 0
    y = r
    p = 1 - r  # parameter keputusan

    # Menggambar 8 titik simetris lingkaran
    def plot(x, y):
        for px, py in [
            (cx + x, cy + y), (cx - x, cy + y),
            (cx + x, cy - y), (cx - x, cy - y),
            (cx + y, cy + x), (cx - y, cy + x),
            (cx + y, cy - x), (cx - y, cy - x)
        ]:
            t.penup()
            t.goto(px, py)
            t.pendown()
            t.dot(3)

    plot(x, y)

    # Perhitungan titik berikutnya
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        plot(x, y)

# =====================================================
# 3. ALGORITMA GAMBAR POLIGON
# Digunakan untuk menggambar atap rumah
# Poligon dibentuk dari beberapa garis DDA
# =====================================================
def draw_polygon(points):
    for i in range(len(points)):
        draw_line_DDA(
            points[i][0], points[i][1],
            points[(i + 1) % len(points)][0],
            points[(i + 1) % len(points)][1]
        )

# =====================================================
# GAMBAR RUMAH 2D
# =====================================================

# ---- TANAH (GARIS DDA) ----
draw_line_DDA(-180, -80, 180, -80)

# ---- DINDING RUMAH (GARIS DDA) ----
draw_line_DDA(-120, -80, 120, -80)
draw_line_DDA(120, -80, 120, 60)
draw_line_DDA(120, 60, -120, 60)
draw_line_DDA(-120, 60, -120, -80)

# ---- ATAP RUMAH (POLIGON) ----
# Penerapan KONSEP TRANSFORMASI 2D:
# Titik bawah atap disamakan dengan titik atas dinding (y = 60)
# agar atap dan dinding menyatu tanpa celah
atap = [
    (-140, 60),   # kiri bawah
    (0, 140),     # puncak atap
    (140, 60)     # kanan bawah
]
draw_polygon(atap)

# ---- CEROBONG (GARIS DDA) ----
draw_line_DDA(-60, 60, -60, 110)
draw_line_DDA(-40, 60, -40, 110)
draw_line_DDA(-60, 110, -40, 110)

# ---- PINTU (GARIS DDA) ----
draw_line_DDA(-90, -80, -90, 10)
draw_line_DDA(-40, -80, -40, 10)
draw_line_DDA(-90, 10, -40, 10)

# ---- JENDELA KOTAK (GARIS DDA) ----
draw_line_DDA(20, -10, 90, -10)
draw_line_DDA(90, -10, 90, 40)
draw_line_DDA(90, 40, 20, 40)
draw_line_DDA(20, 40, 20, -10)
draw_line_DDA(55, -10, 55, 40)
draw_line_DDA(20, 15, 90, 15)

# ---- JENDELA BULAT (MIDPOINT CIRCLE) ----
draw_circle_midpoint(-10, 20, 10)

# ===================== SELESAI =====================
turtle.done()
