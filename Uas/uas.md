# 🚖 Simulator Taksi 3D (PyOpenGL)

Simulator kendaraan 3D berperforma tinggi yang dibangun menggunakan **Python**, **Pygame**, dan **PyOpenGL**. Proyek ini mendemonstrasikan pemodelan 3D prosedural, pencahayaan, dan sistem kamera interaktif untuk keperluan studi Grafika Komputer.

---

## 🌟 Fitur Utama

- **Pemodelan 3D Prosedural**: Seluruh model taksi didefinisikan secara manual melalui titik koordinat (`VERTICES`) dan bidang (`FACES`), sehingga tidak memerlukan file eksternal seperti `.obj`.
- **Sistem Kamera Orbital**: Rotasi penuh 360 derajat dan fitur zoom yang halus menggunakan interaksi mouse (drag dan scroll).
- **Pencahayaan Dinamis**: Implementasi `GL_LIGHT0` dengan perhitungan **Vektor Normal** khusus untuk pantulan cahaya yang realistis pada bodi mobil.
- **Efek Visual**:
  - **Alpha Blending**: Efek kaca jendela berwarna biru yang transparan.
  - **Anti-Aliasing**: Mengaktifkan multi-sampling untuk menghaluskan tepi objek yang kasar.
  - **Bayangan Lantai**: Simulasi bayangan lembut secara real-time pada bidang lantai.

---

## 📐 Implementasi Teknis & Transformasi

### 1. Data Geometri
Model ini disusun dari beberapa lapisan titik sudut (vertices):
- **Sasis**: Kerangka bagian bawah mobil.
- **Belt Line**: Bagian tengah yang menentukan siluet mobil.
- **Permukaan Atas**: Kap mesin, atap, dan bagasi.
- **Detail**: Lampu depan, lampu belakang, dan papan nama khas "TAXI" di atap.

### 2. Transformasi Geometris
Proyek ini menggunakan alur transformasi standar OpenGL:
- **Translasi**: `glTranslatef(0.0, -1.0, zoom)` digunakan untuk mengatur jarak kamera dan memposisikan taksi di dalam studio virtual.
- **Rotasi**: `glRotatef()` menangani rotasi orbit yang dikendalikan pengguna berdasarkan pergerakan mouse terhadap sumbu $X$ dan $Y$.
- **Skala**: Penentuan ukuran didefinisikan langsung di dalam unit koordinat pada array `VERTICES`.

### 3. Perhitungan Vektor Normal
Untuk mengaktifkan pencahayaan yang realistis, program menghitung vektor normal untuk setiap bidang poligon menggunakan perkalian silang (*cross-product*) dari dua tepi bidang:

Fungsi `hitung_normal(v1, v2, v3)` memastikan bodi kuning taksi memantulkan cahaya secara akurat berdasarkan orientasi permukaannya.

---

## ⌨️ Kontrol Pengguna

| Input | Aksi |
| :--- | :--- |
| **Klik Kiri + Geser Mouse** | Rotasi Kamera (Orbit) |
| **Scroll Atas** | Zoom In (Mendekat) |
| **Scroll Bawah** | Zoom Out ( menjauh) |

---
