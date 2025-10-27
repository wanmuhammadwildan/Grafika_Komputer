# Membuat dan menampilkan grid 10x10 dengan '.' lalu mengganti piksel di posisi (4,6) menjadi 'X'.
# Asumsi: posisi (4,6) diinterpretasikan sebagai (baris, kolom) dengan indeks 0-based.
# Jika Anda ingin memakai 1-based, lihat catatan di bagian bawah.

rows, cols = 10, 10
grid = [['.' for _ in range(cols)] for _ in range(rows)]

# ganti piksel (baris, kolom) = (4,6) -> 0-based
grid[4][6] = 'X'

# tampilkan grid
for r in grid:
    print(' '.join(r))

# ---------- Catatan ----------
# Jika (4,6) maksudnya 1-based (manusia): 
# row, col = 4, 6
# grid[row-1][col-1] = 'X'
# lalu cetak seperti di atas.
