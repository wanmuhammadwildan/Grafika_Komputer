import turtle
import math

# ================= SETUP =================
screen = turtle.Screen()
screen.setup(900, 650)
screen.bgcolor("#b3e5fc")
screen.title("Transformasi 3D - Auto Scale")
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# ================= TRANSFORM STATE =================
tx, ty = 0, -120          # Translasi
angle = 0                # Rotasi
scale = 1.0              # Skala
scale_dir = 1            # arah skala
reflect = 1              # Refleksi

dx, dy = 0, 0
speed = 5
arm_phase = 0

# ================= WARNA =================
def lighten(c):
    return {"yellow":"#fff176","blue":"#64b5f6","green":"#aed581"}.get(c,c)

def darken(c):
    return {"yellow":"#fbc02d","blue":"#1e88e5","green":"#558b2f"}.get(c,c)

# ================= TRANSFORMASI =================
def transform_point(x, y):
    # Skala + refleksi
    x *= scale * reflect
    y *= scale

    # Rotasi
    rad = math.radians(angle)
    xr = x * math.cos(rad) - y * math.sin(rad)
    yr = x * math.sin(rad) + y * math.cos(rad)

    # Translasi
    return xr + tx, yr + ty

# ================= BALOK 3D =================
def draw_box(x, y, w, h, d, color):
    front = [(x,y),(x+w,y),(x+w,y+h),(x,y+h)]
    top   = [(x,y+h),(x+d,y+h+d),(x+w+d,y+h+d),(x+w,y+h)]
    side  = [(x+w,y),(x+w+d,y+d),(x+w+d,y+h+d),(x+w,y+h)]

    def face(points, fill):
        pen.color("black", fill)
        pen.begin_fill()
        pen.penup()
        pen.goto(transform_point(*points[0]))
        pen.pendown()
        for p in points[1:]:
            pen.goto(transform_point(*p))
        pen.goto(transform_point(*points[0]))
        pen.end_fill()

    face(front, color)
    face(top, lighten(color))
    face(side, darken(color))

# ================= GAMBAR KARAKTER =================
def draw_character():
    pen.clear()
    d = 18
    swing = math.sin(arm_phase) * 20

    # kaki
    draw_box(-35, 0, 30, 70, d, "green")
    draw_box(5,   0, 30, 70, d, "green")

    # badan
    draw_box(-60, 70, 120, 100, d, "blue")

    # tangan
    draw_box(-120, 90 + swing, 55, 90, d, "yellow")
    draw_box(65,   90 - swing, 55, 90, d, "yellow")

    # kepala
    draw_box(-45, 170, 90, 90, d, "yellow")

    # mata
    e1 = transform_point(-15, 220)
    e2 = transform_point(15, 220)
    pen.color("black")
    pen.penup()
    pen.goto(e1); pen.dot(6)
    pen.goto(e2); pen.dot(6)

    screen.update()

# ================= UPDATE LOOP =================
def update():
    global tx, ty, arm_phase, scale, scale_dir

    # Translasi
    tx += dx
    ty += dy

    # Animasi tangan
    if dx != 0 or dy != 0:
        arm_phase += 0.3

    # Auto scaling (smooth)
    scale += 0.005 * scale_dir
    if scale > 1.3:
        scale_dir = -1
    elif scale < 0.7:
        scale_dir = 1

    draw_character()
    screen.ontimer(update, 30)

# ================= KONTROL =================
def up():    global dy; dy = speed
def down():  global dy; dy = -speed
def left():  global dx; dx = -speed
def right(): global dx; dx = speed
def stop():  global dx,dy; dx = dy = 0

def rot_left():  
    global angle
    angle += 5

def rot_right(): 
    global angle
    angle -= 5

def mirror():
    global reflect
    reflect *= -1

screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(stop, "space")

screen.onkey(rot_left, "a")
screen.onkey(rot_right, "d")
screen.onkey(mirror, "m")

# ================= START =================
update()
turtle.done()
