import pygame
import sys

pygame.init()

# ----------------------------------------------------
# SETUP WINDOW
# ----------------------------------------------------
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Transformasi 2D - Sprite")

clock = pygame.time.Clock()

# ----------------------------------------------------
# LOAD SPRITE (gunakan gambar yang dibuat)
# ----------------------------------------------------
sprite = pygame.image.load("karakter.png").convert_alpha()

# posisi awal
x, y = 100, 200
angle = 0
scale = 1.0
flip_x = False

# ----------------------------------------------------
# FUNGSI TRANSFORMASI
# ----------------------------------------------------
def dash():
    global x
    x += 20

def rotate():
    global angle
    angle += 30

def scale_up():
    global scale
    scale *= 1.5

def mirror():
    global flip_x
    flip_x = not flip_x

# ----------------------------------------------------
# PROGRAM UTAMA
# ----------------------------------------------------
running = True
step = 0  # transformasi berurutan

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((220, 220, 220))

    keys = pygame.key.get_pressed()

    # Tekan ENTER untuk menjalankan langkah
    if keys[pygame.K_RETURN]:
        step += 1
        pygame.time.delay(250)

        if step == 1:
            dash()
        elif step == 2:
            rotate()
        elif step == 3:
            scale_up()
        elif step == 4:
            mirror()

    # ------------------------------------------------
    # Terapkan transformasi
    # ------------------------------------------------
    rotated = pygame.transform.rotate(sprite, angle)

    new_size = (int(rotated.get_width() * scale),
                int(rotated.get_height() * scale))
    scaled = pygame.transform.scale(rotated, new_size)

    final_sprite = pygame.transform.flip(scaled, flip_x, False)

    screen.blit(final_sprite, (x, y))

    # Text
    font = pygame.font.SysFont("Arial", 24)
    text = font.render("Tekan ENTER untuk Transformasi", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    step_text = font.render(f"Step: {step}", True, (0, 0, 0))
    screen.blit(step_text, (10, 40))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
