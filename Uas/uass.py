import pygame
from pygame.locals import *
import sys
import math

# --- IMPORT OPENGL ---
try:
    from OpenGL.GL import *
    from OpenGL.GLU import *
except ImportError:
    print("\n[EROR] Library PyOpenGL tidak ditemukan! Install dengan: pip install PyOpenGL PyOpenGL_accelerate")
    sys.exit()

# --- DATA MODEL 3D (Sedan Taksi) ---
# Hardcoded (tertulis langsung) untuk menghindari ketergantungan file eksternal .obj (Ramah untuk Thonny)

VERTICES = [
    # --- RANGKA BAWAH (Lantai Mobil) ---
    [-0.8, 0.2,  2.8], [ 0.8, 0.2,  2.8], # 0-1: Bumper depan bawah
    [ 1.1, 0.2,  1.0], [-1.1, 0.2,  1.0], # 2-3: Tengah depan bawah
    [ 1.1, 0.2, -1.0], [-1.1, 0.2, -1.0], # 4-5: Tengah belakang bawah
    [-0.8, 0.2, -2.8], [ 0.8, 0.2, -2.8], # 6-7: Bumper belakang bawah
    
    # --- GARIS BODI (Belt Line - Naikkan sedikit agar tidak ceper) ---
    [-0.9, 0.85,  2.9], [ 0.9, 0.85,  2.9], # 8-9: Bumper depan atas
    [ 1.15, 0.9, 1.2], [-1.15, 0.9, 1.2], # 10-11: Sisi dasar mesin
    [ 1.15, 0.9,-1.2], [-1.15, 0.9,-1.2], # 12-13: Sisi dasar bagasi
    [-0.9, 0.85,-2.9], [ 0.9, 0.85,-2.9], # 14-15: Bumper belakang atas

    # --- PERMUKAAN ATAS (Kap, Atap, Bagasi) ---
    [-0.7, 0.9,  2.8], [ 0.7, 0.9,  2.8], # 16-17: Ujung kap depan
    [-0.9, 0.95, 1.1], [ 0.9, 0.95, 1.1], # 18-19: Dasar kaca depan
    [-0.8, 1.65, 0.6], [ 0.8, 1.65, 0.6], # 20-21: Atap depan
    [ 0.8, 1.65,-0.7], [-0.8, 1.65,-0.7], # 22-23: Atap belakang
    [-0.9, 0.9, -1.1], [ 0.9, 0.9, -1.1], # 24-25: Dasar kaca belakang
    [-0.7, 0.9, -2.7], [ 0.7, 0.9, -2.7], # 26-27: Ujung bagasi belakang

    # --- PAPAN NAMA TAXI ---
    [-0.3, 1.65,  0.2], [ 0.3, 1.65,  0.2], [ 0.3, 1.85, 0.1], [-0.3, 1.85, 0.1], # 28-31: Bagian Depan
    [-0.3, 1.65, -0.2], [ 0.3, 1.65, -0.2], [ 0.3, 1.85,-0.1], [-0.3, 1.85,-0.1], # 32-35: Bagian Belakang

    # --- LAMPU ---
    [-0.8, 0.5, 2.91], [-0.5, 0.5, 2.91], [-0.5, 0.75, 2.91], [-0.8, 0.75, 2.91], # 36-39: Lampu Depan Kiri
    [ 0.5, 0.5, 2.91], [ 0.8, 0.5, 2.91], [ 0.8, 0.75, 2.91], [ 0.5, 0.75, 2.91], # 40-43: Lampu Depan Kanan
    [-0.8, 0.5, -2.91], [-0.5, 0.5, -2.91], [-0.5, 0.75, -2.91], [-0.8, 0.75, -2.91], # 44-47: Lampu Belakang Kiri
    [ 0.5, 0.5, -2.91], [ 0.8, 0.5, -2.91], [ 0.8, 0.75, -2.91], [ 0.5, 0.75, -2.91], # 48-51: Lampu Belakang Kanan
]

FACES = [
    # Bodi Depan
    (8, 9, 1, 0), (8, 16, 17, 9), (16, 18, 19, 17), 
    # Bodi Belakang
    (14, 15, 7, 6), (14, 26, 27, 15), (26, 24, 25, 27),
    # Sisi Bodi (Kiri)
    (0, 8, 11, 13, 14, 6, 5, 3), (11, 18, 24, 13), 
    # Sisi Bodi (Kanan)
    (1, 9, 10, 12, 15, 7, 4, 2), (10, 19, 25, 12),
    # Pengisi Sisi Kap/Bagasi
    (8, 11, 18, 16), (9, 10, 19, 17), (14, 13, 24, 26), (15, 12, 25, 27),

    # Kaca Jendela
    (18, 19, 21, 20), # Kaca Depan
    (24, 25, 22, 23), # Kaca Belakang
    (18, 20, 23, 24), # Kaca Samping Kiri
    (19, 21, 22, 25), # Kaca Samping Kanan
    # Atap
    (20, 21, 22, 23),
    # Papan Nama Taxi
    (28, 29, 30, 31), (32, 33, 34, 35), (29, 33, 34, 30), (28, 32, 35, 31), (30, 34, 35, 31), (28, 29, 33, 32),
    # Lampu
    (36, 37, 38, 39), (40, 41, 42, 43), # Lampu Depan
    (44, 45, 46, 47), (48, 49, 50, 51), # Lampu Belakang
]

def gambar_teks_taxi():
    # Menggambar tulisan "TAXI" pada papan di atas menggunakan garis
    glDisable(GL_LIGHTING)
    glColor3f(0.0, 0.0, 0.0) # Warna hitam pekat
    glLineWidth(3)
    
    # Sisi Depan
    for side_z in [0.22, -0.22]:
        glBegin(GL_LINES)
        y_top = 1.82
        y_bot = 1.70
        y_mid = 1.76
        
        # T
        glVertex3f(-0.25, y_top, side_z); glVertex3f(-0.15, y_top, side_z)
        glVertex3f(-0.20, y_top, side_z); glVertex3f(-0.20, y_bot, side_z)
        # A
        glVertex3f(-0.12, y_bot, side_z); glVertex3f(-0.07, y_top, side_z)
        glVertex3f(-0.07, y_top, side_z); glVertex3f(-0.02, y_bot, side_z)
        glVertex3f(-0.10, y_mid, side_z); glVertex3f(-0.04, y_mid, side_z)
        # X
        glVertex3f(0.02, y_top, side_z); glVertex3f(0.10, y_bot, side_z)
        glVertex3f(0.10, y_top, side_z); glVertex3f(0.02, y_bot, side_z)
        # I
        glVertex3f(0.15, y_top, side_z); glVertex3f(0.25, y_top, side_z)
        glVertex3f(0.20, y_top, side_z); glVertex3f(0.20, y_bot, side_z)
        glVertex3f(0.15, y_bot, side_z); glVertex3f(0.25, y_bot, side_z)
        glEnd()
    glEnable(GL_LIGHTING)

def hitung_normal(v1, v2, v3):
    # Menghitung vektor normal permukaan untuk pencahayaan yang benar
    ax, ay, az = v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]
    bx, by, bz = v3[0] - v1[0], v3[1] - v1[1], v3[2] - v1[2]
    nx = ay * bz - az * by
    ny = az * bx - ax * bz
    nz = ax * by - ay * bx
    panjang = math.sqrt(nx*nx + ny*ny + nz*nz)
    if panjang == 0: return (0, 1, 0)
    return (nx/panjang, ny/panjang, nz/panjang)

def gambar_roda(x, y, z):
    glPushMatrix()
    glTranslatef(x, y, z)
    glRotatef(90, 0, 1, 0)
    glColor3f(0.12, 0.12, 0.12) # Warna ban hitam
    quadric = gluNewQuadric()
    # Gambar sisi ban dan silinder
    gluDisk(quadric, 0, 0.35, 32, 1)
    glTranslatef(0,0, 0.1)
    gluDisk(quadric, 0, 0.35, 32, 1)
    glTranslatef(0,0, -0.1)
    gluCylinder(quadric, 0.35, 0.35, 0.1, 32, 1)
    glPopMatrix()

def gambar_taksi():
    # --- TAHAP 1: GAMBAR BIDANG SOLID (ISI) ---
    for i, face in enumerate(FACES):
        # Logika Pewarnaan berdasarkan urutan FACES yang baru
        if i < 14: glColor3f(1.0, 0.8, 0.0)    # Bodi Kuning
        elif 14 <= i < 18: glColor4f(0.4, 0.7, 1.0, 0.6) # Kaca Jendela (Cyan)
        elif i == 18: glColor3f(1.0, 0.8, 0.0) # Atap
        elif 19 <= i < 25: glColor3f(1.0, 1.0, 0.5) # Dasar Papan Taksi
        elif 25 <= i < 27: glColor3f(1.0, 1.0, 0.9) # Lampu Depan
        elif 27 <= i < 29: glColor3f(0.8, 0.0, 0.0) # Lampu Belakang
        else: glColor3f(0.5, 0.5, 0.5)

        # Hitung Normal untuk bidang ini
        v1, v2, v3 = VERTICES[face[0]], VERTICES[face[1]], VERTICES[face[2]]
        norm = hitung_normal(v1, v2, v3)
        
        glBegin(GL_POLYGON)
        glNormal3fv(norm)
        for v_idx in face:
            glVertex3fv(VERTICES[v_idx])
        glEnd()

    # --- TAHAP 2: GAMBAR BINGKAI JENDELA ---
    glDisable(GL_LIGHTING)
    glColor3f(0.05, 0.05, 0.05) # Warna bingkai hitam
    glLineWidth(3)
    for i in range(14, 18): # Bidang kaca 14 sampai 17
        face = FACES[i]
        glBegin(GL_LINE_LOOP)
        for v_idx in face:
            glVertex3fv(VERTICES[v_idx])
        glEnd()
    glEnable(GL_LIGHTING)
    
    # Gambar teks "TAXI" dan Roda
    gambar_teks_taxi()
    gambar_roda(-1.18, 0.35,  1.8)
    gambar_roda( 1.12, 0.35,  1.8)
    gambar_roda(-1.18, 0.35, -1.8)
    gambar_roda( 1.12, 0.35, -1.8)

def jalankan():
    print("Memulai Inisialisasi Pygame...")
    pygame.init()
    
    # Pengaturan atribut OpenGL untuk stabilitas di Windows/Thonny
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLEBUFFERS, 1)
    pygame.display.gl_set_attribute(pygame.GL_MULTISAMPLESAMPLES, 4)
    pygame.display.gl_set_attribute(pygame.GL_DEPTH_SIZE, 24)
    
    WIDTH, HEIGHT = 1000, 700
    print(f"Membuka Jendela: {WIDTH}x{HEIGHT}...")
    try:
        pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
    except pygame.error as e:
        print(f"Gagal membuka jendela OpenGL: {e}")
        pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF) # Fallback 
        return

    pygame.display.set_caption("SIMULATOR TAKSI 3D - VERSI PROPOSIONAL (Ramah Thonny)")

    print("Mengatur OpenGL...")
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_NORMALIZE)
    
    glLightfv(GL_LIGHT0, GL_POSITION, (5, 10, 5, 1))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.6, 0.6, 0.6, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.8, 0.8, 0.8, 1.0))
    
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)
    
    print("Aplikasi Siap! Gunakan Mouse untuk Rotasi dan Zoom.")

    rx, ry = 20, 45
    zoom = -12.0
    dragging = False
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1: dragging = True
                elif event.button == 4: zoom += 0.5 # Scroll atas (Zoom in)
                elif event.button == 5: zoom -= 0.5 # Scroll bawah (Zoom out)
            elif event.type == MOUSEBUTTONUP:
                if event.button == 1: dragging = False
            elif event.type == MOUSEMOTION and dragging:
                dx, dy = event.rel
                ry += dx; rx += dy

        glClearColor(0.2, 0.2, 0.2, 1.0) # Latar Belakang Abu-abu Studio
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        
        glLoadIdentity()
        gluPerspective(45, (WIDTH/HEIGHT), 0.1, 100.0)
        glTranslatef(0.0, -1.0, zoom)
        
        glRotatef(rx, 1, 0, 0)
        glRotatef(ry, 0, 1, 0)
        
        # Bayangan Lantai
        glDisable(GL_LIGHTING)
        glEnable(GL_BLEND); glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glColor4f(0, 0, 0, 0.3)
        glBegin(GL_POLYGON)
        for i in range(32):
            angle = i * 2 * math.pi / 32
            glVertex3f(5.0 * math.cos(angle), 0, 4.0 * math.sin(angle))
        glEnd()
        glDisable(GL_BLEND)
        glEnable(GL_LIGHTING)

        gambar_taksi()
        
        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    jalankan()