# Image Processing

Repositori ini berisi kumpulan script Python untuk mata kuliah **Pengolahan Citra Digital (Image Processing)**. Materi disusun per pertemuan dan mencakup manipulasi piksel, pembuatan gambar sintetis, konversi warna, serta efek visual menggunakan NumPy dan Matplotlib.

## Persyaratan

- Python 3.x
- NumPy
- Matplotlib

```bash
pip install numpy matplotlib
```

## Struktur Direktori

```
image_processing/
├── pertemuan 1/
│   ├── Membuat_lapisan_warna_horizontal.py
│   ├── Membuat_lapisan_warna_vertikal.py
│   ├── bendera_merah_putih.py
│   ├── simpan_rename_file_looping.py
│   └── gambar/
├── pertemuan 2/
│   ├── Efek_kaca.py
│   ├── RGB_and_Grayscale.py
│   ├── RGB_dinolkan.py
│   ├── RGB_to_Grayscale.py
│   ├── Spiderman.jpeg
│   ├── kucing.jpeg
│   └── macbook.jpeg
└── README.md
```

## Pertemuan 1 — Pembuatan Gambar Sintetis & Operasi File

| Script | Deskripsi |
|---|---|
| `Membuat_lapisan_warna_horizontal.py` | Membuat gambar 1920×1080 dengan 5 lapisan warna horizontal (merah, hijau, biru, kuning, magenta) menggunakan manipulasi array NumPy piksel per piksel. |
| `Membuat_lapisan_warna_vertikal.py` | Sama seperti di atas, tetapi lapisan warna disusun secara vertikal (magenta, kuning, biru, hijau, merah). |
| `bendera_merah_putih.py` | Membuat gambar bendera Indonesia (merah-putih) pada kanvas hitam 1920×1080 menggunakan slicing array NumPy. |
| `simpan_rename_file_looping.py` | Membaca file gambar, menyimpan 20 salinan dengan nama berurutan, lalu menampilkan 5 gambar pertama secara bergiliran dengan jeda 1 detik. |

### Cara Menjalankan

```bash
cd "pertemuan 1"
python bendera_merah_putih.py
python Membuat_lapisan_warna_horizontal.py
python Membuat_lapisan_warna_vertikal.py
python simpan_rename_file_looping.py
```

Hasil gambar disimpan di folder `pertemuan 1/gambar/`.

## Pertemuan 2 — Manipulasi Warna & Efek Visual

| Script | Deskripsi |
|---|---|
| `RGB_to_Grayscale.py` | Memisahkan channel R, G, B dari gambar (`macbook.jpeg`) dan menampilkannya masing-masing sebagai grayscale. |
| `RGB_and_Grayscale.py` | Menampilkan channel R, G, B secara terpisah (grayscale) beserta gambar asli RGB dari `macbook.jpeg`. |
| `RGB_dinolkan.py` | Mendemonstrasikan efek menghilangkan channel warna satu per satu (R→0, G→0, B→0) pada gambar `kucing.jpeg`. |
| `Efek_kaca.py` | Membuat efek kaca transparan pada setengah kanan gambar `Spiderman.jpeg` dengan bingkai abu-abu terang. Transparansi dan tebal bingkai dapat dikonfigurasi. |

### Cara Menjalankan

```bash
cd "pertemuan 2"
python RGB_to_Grayscale.py
python RGB_and_Grayscale.py
python RGB_dinolkan.py
python Efek_kaca.py
```

## Lisensi

Belum ditentukan.