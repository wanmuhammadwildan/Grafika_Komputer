# Program menampilkan tabel perbandingan Raster dan Vektor
# berdasarkan hasil praktikum

# Header tabel
print("=" * 80)
print("{:<25} {:<25} {:<25}".format("Aspek Perbandingan", "Raster (Pixel-based)", "Vektor (Koordinat)"))
print("=" * 80)

# Isi tabel
data = [
    ("Konsep dasar", 
     "Tersusun dari piksel-piksel.", 
     "Tersusun dari garis dan titik koordinat."),
    
    ("Contoh hasil praktikum", 
     "Grid 10x10 dengan '.' dan 'X' mewakili piksel.", 
     "Garis dari (0,0) ke (5,3) dihitung secara vektor."),
    
    ("Ketika diperbesar", 
     "Menjadi pecah atau buram.", 
     "Tetap tajam karena dihitung ulang."),
    
    ("Penyimpanan data", 
     "Setiap piksel disimpan (file besar).", 
     "Simpan rumus atau koordinat (file kecil)."),
    
    ("Kegunaan umum", 
     "Foto, citra satelit, hasil kamera.", 
     "Logo, diagram, desain teknik (CAD)."),
    
    ("Contoh format file", 
     ".bmp, .jpg, .png", 
     ".svg, .ai, .eps"),
    
    ("Kelebihan", 
     "Realistis dan detail tinggi.", 
     "Dapat diperbesar tanpa pecah."),
    
    ("Kekurangan", 
     "Tidak fleksibel untuk ubah bentuk.", 
     "Kurang cocok untuk gambar realistis.")
]

# Cetak tiap baris tabel
for aspek, raster, vektor in data:
    print("{:<25} {:<25} {:<25}".format(aspek, raster, vektor))

print("=" * 80)
