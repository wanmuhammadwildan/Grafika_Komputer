# Program menggambar garis dari (0,0) ke (5,3)
# dengan menghitung titik-titik koordinatnya

x0, y0 = 0, 0
x1, y1 = 5, 3

# Tentukan jumlah langkah (misal sesuai selisih terbesar)
steps = max(abs(x1 - x0), abs(y1 - y0))

# Hitung perubahan tiap langkah
dx = (x1 - x0) / steps
dy = (y1 - y0) / steps

# Hitung dan tampilkan titik-titik garis
x, y = x0, y0
print("Titik-titik koordinat garis dari (0,0) ke (5,3):")
for i in range(steps + 1):
    print(f"({round(x)}, {round(y)})")
    x += dx
    y += dy
