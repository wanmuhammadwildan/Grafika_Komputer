🏠 Proyek Grafika Komputer 2D

Tema: Rumah Sederhana 2D
Bahasa: Python (Thonny)

📌 Deskripsi Proyek

Proyek ini merupakan aplikasi grafika komputer 2D sederhana menggunakan Python dan modul turtle.
Seluruh objek digambar menggunakan algoritma grafika manual, tanpa menggunakan fungsi gambar siap pakai.

Proyek ini menerapkan 4 materi wajib dalam mata kuliah Grafika Komputer.

📚 Materi yang Diterapkan

Algoritma Gambar Garis (DDA)

Algoritma Gambar Lingkaran (Midpoint Circle)

Algoritma Gambar Poligon

Transformasi Geometri 2D (Translasi)

🧩 Penjelasan Umum Program

Dinding, pintu, dan kerangka rumah digambar menggunakan algoritma DDA

Jendela berbentuk lingkaran digambar menggunakan algoritma Midpoint Circle

Atap rumah digambar menggunakan algoritma Poligon

Transformasi translasi diterapkan untuk memindahkan posisi atap

🧠 Kode Program
import turtle
import math

# =====================================================
# Program Grafika 2D Rumah
# Menerapkan 4 Materi Wajib Grafika Komputer:
# 1. Algoritma Garis DDA
# 2. Algoritma Lingkaran Midpoint
# 3. Algoritma Poligon
# 4. Transformasi Geometri 2D (Translasi)
# =====================================================

# ===================== SETUP LAYAR =====================
screen = turtle.Screen()
screen.title("Rumah 2D - Grafika Komputer")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("white")

# ===================== 1. GARIS DDA =====================
def draw_line_DDA(x1, y1, x2, y2):
    """
    Menggambar garis menggunakan algoritma DDA (Digital Differential Analyzer)
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

    for _ in range(steps):
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
    Menggambar poligon dari kumpulan titik menggunakan garis DDA
    """
    for i in range(len(points)):
        x1, y1 = points[i]
        x2, y2 = points[(i + 1) % len(points)]
        draw_line_DDA(x1, y1, x2, y2)

# ===================== 4. TRANSFORMASI (TRANSLASI) =====================
def translate(points, tx, ty):
    """
    Transformasi translasi untuk menggeser objek
    """
    return [(x + tx, y + ty) for x, y in points]

# ===================== GAMBAR RUMAH =====================

# ---- DINDING RUMAH ----
draw_line_DDA(-100, -60, 100, -60)
draw_line_DDA(100, -60, 100, 40)
draw_line_DDA(100, 40, -100, 40)
draw_line_DDA(-100, 40, -100, -60)

# ---- PINTU ----
draw_line_DDA(-20, -60, -20, 10)
draw_line_DDA(20, -60, 20, 10)
draw_line_DDA(-20, 10, 20, 10)

# ---- JENDELA BULAT ----
draw_circle_midpoint(50, 0, 12)

# ---- ATAP (POLIGON) ----
atap = [(-120, 40), (0, 120), (120, 40)]

# Transformasi translasi pada atap
atap = translate(atap, 0, 25)

draw_polygon(atap)

# ===================== SELESAI =====================
turtle.done()

## 🖼️ Hasil Program

Berikut adalah hasil tampilan dari program grafika komputer 2D bertema rumah sederhana yang dibuat menggunakan Python (Thonny) dengan algoritma grafika manual.

<p align="center">
  <img src="hasil_program.png" alt="Hasil Program Rumah 2D" width="500">
</p>








