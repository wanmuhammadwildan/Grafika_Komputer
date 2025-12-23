🏠 Proyek Grafika Komputer 2D – Rumah Sederhana
📌 Deskripsi

Proyek ini merupakan implementasi grafika komputer 2D menggunakan Python (Thonny) dengan tema Rumah Sederhana.


📚 Materi yang Diterapkan

Program ini menerapkan 4 materi wajib Grafika Komputer, yaitu:

Algoritma Gambar Garis (DDA)

Algoritma Gambar Lingkaran (Midpoint Circle)

Algoritma Gambar Poligon

Transformasi Geometris 2D (konsep translasi & penyesuaian koordinat)

🧠 Penjelasan Singkat

Algoritma DDA digunakan untuk menggambar seluruh garis lurus seperti tanah, dinding, pintu, jendela kotak, dan cerobong.

Algoritma Midpoint Circle digunakan untuk menggambar jendela berbentuk lingkaran.

Algoritma Poligon digunakan untuk membentuk atap rumah.

Transformasi 2D diterapkan melalui pengaturan koordinat objek agar atap menyatu dengan dinding tanpa celah.

💻 Kode Program
import turtle
import math


# PROGRAM GRAFIKA KOMPUTER 2D – RUMAH SEDERHANA
# MATERI YANG DITERAPKAN:
# 1. Algoritma Garis DDA
# 2. Algoritma Lingkaran Midpoint
# 3. Algoritma Poligon
# 4. Transformasi Geometris 2D


#  SETUP LAYAR
screen = turtle.Screen()
screen.title("Rumah 2D - wan ")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
turtle.bgcolor("white")

# GARIS DDA 
def draw_line_DDA(x1, y1, x2, y2):
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

# MIDPOINT CIRCLE 
def draw_circle_midpoint(cx, cy, r):
    x = 0
    y = r
    p = 1 - r

    def plot(x, y):
        for px, py in [
            (cx+x, cy+y), (cx-x, cy+y),
            (cx+x, cy-y), (cx-x, cy-y),
            (cx+y, cy+x), (cx-y, cy+x),
            (cx+y, cy-x), (cx-y, cy-x)
        ]:
            t.penup()
            t.goto(px, py)
            t.pendown()
            t.dot(3)

    plot(x, y)
    while x < y:
        x += 1
        if p < 0:
            p += 2*x + 1
        else:
            y -= 1
            p += 2*(x - y) + 1
        plot(x, y)

#  POLIGON 
def draw_polygon(points):
    for i in range(len(points)):
        draw_line_DDA(
            points[i][0], points[i][1],
            points[(i+1)%len(points)][0],
            points[(i+1)%len(points)][1]
        )

#  GAMBAR RUMAH 
draw_line_DDA(-180, -80, 180, -80)

draw_line_DDA(-120, -80, 120, -80)
draw_line_DDA(120, -80, 120, 60)
draw_line_DDA(120, 60, -120, 60)
draw_line_DDA(-120, 60, -120, -80)

atap = [(-140, 60), (0, 140), (140, 60)]
draw_polygon(atap)

draw_line_DDA(-60, 60, -60, 110)
draw_line_DDA(-40, 60, -40, 110)
draw_line_DDA(-60, 110, -40, 110)

draw_line_DDA(-90, -80, -90, 10)
draw_line_DDA(-40, -80, -40, 10)
draw_line_DDA(-90, 10, -40, 10)

draw_line_DDA(20, -10, 90, -10)
draw_line_DDA(90, -10, 90, 40)
draw_line_DDA(90, 40, 20, 40)
draw_line_DDA(20, 40, 20, -10)
draw_line_DDA(55, -10, 55, 40)
draw_line_DDA(20, 15, 90, 15)

draw_circle_midpoint(-10, 20, 10)

turtle.done()

🖼️ Hasil Program

Berikut adalah hasil tampilan dari program grafika komputer 2D yang telah dijalankan:

<img width="603" height="458" alt="Screenshot 2025-12-23 170430" src="https://github.com/user-attachments/assets/42b7f9c1-7a28-4c21-bda1-47d14abe213b" />

✅ Kesimpulan

Program ini berhasil menerapkan algoritma grafika komputer manual berupa algoritma DDA, Midpoint Circle, Poligon, serta konsep transformasi geometri 2D untuk membentuk objek rumah 2D yang utuh.
