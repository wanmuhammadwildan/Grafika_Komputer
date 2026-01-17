# 🤖 3D Character Transformation (Manual Matrix)

Program ini mendemonstrasikan bagaimana konsep **Grafika Komputer** tingkat lanjut diimplementasikan menggunakan library `turtle` di Python. Berbeda dengan library grafis modern, proyek ini menghitung setiap transformasi titik secara manual menggunakan prinsip matematika linear.

## 🚀 Fitur Utama
- **Auto-Scaling**: Karakter membesar dan mengecil secara otomatis dengan animasi yang halus.
- **Manual Rotation**: Rotasi 2D pada sumbu pusat menggunakan input keyboard (A/D).
- **Reflection**: Fitur *mirroring* instan pada sumbu X (Tombol M).
- **Smooth Translation**: Pergerakan karakter yang responsif menggunakan tombol panah.
- **Pseudo-3D Projection**: Teknik menggambar balok dengan perspektif buatan (Front, Top, Side) untuk menciptakan kesan kedalaman.

---

## 📐 Penjelasan Matematis (Transformasi)

Seluruh keajaiban program ini berada pada fungsi `transform_point(x, y)`. Berikut adalah urutan perhitungan yang terjadi pada setiap titik (vertex):

### 1. Skala & Refleksi (Scaling & Reflection)
Sebelum diputar atau dipindahkan, ukuran objek diubah terlebih dahulu.
$$x' = x \cdot \text{scale} \cdot \text{reflect}$$
$$y' = y \cdot \text{scale}$$
* Jika `reflect` bernilai `-1`, titik akan berpindah ke sisi berlawanan pada sumbu X (Mencerminkan objek).



### 2. Rotasi (Rotation)
Menggunakan **Matriks Rotasi 2D** untuk memutar titik terhadap titik pusat $(0,0)$ berdasarkan sudut $\theta$.
$$x_r = x' \cos(\theta) - y' \sin(\theta)$$
$$y_r = x' \sin(\theta) + y' \cos(\theta)$$



### 3. Translasi (Translation)
Langkah terakhir adalah memindahkan titik yang sudah diproses ke posisi karakter di layar.
$$x_{final} = x_r + t_x$$
$$y_{final} = y_r + t_y$$

---

## 🏗️ Teknik Rendering Balok 3D
Program menggunakan fungsi `draw_box()` untuk membangun ilusi 3D dengan menggambar 3 bidang (faces) secara berurutan:
1.  **Front Face**: Persegi utama (warna dasar).
2.  **Top Face**: Menggunakan fungsi `lighten()` untuk memberikan efek cahaya dari atas.
3.  **Side Face**: Menggunakan fungsi `darken()` untuk memberikan efek bayangan di sisi samping.

---

## ⌨️ Kontrol Navigasi

| Tombol | Fungsi |
| :--- | :--- |
| **Arrow Up/Down/Left/Right** | Menggerakkan Karakter (Translasi) |
| **Space** | Menghentikan Gerakan |
| **A** | Rotasi Berlawanan Jarum Jam |
| **D** | Rotasi Searah Jarum Jam |
| **M** | Refleksi / Mirroring |

---

## 🛠️ Persyaratan Sistem
- Python 3.x
- Library `turtle` (Sudah termasuk dalam instalasi standar Python)
- Library `math` (Sudah termasuk dalam instalasi standar Python)

