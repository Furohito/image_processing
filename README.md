## Pertemuan 1 — Gambar sintetis (dibuat dari array) + simpan file
Inti: membangun citra RGB dari nol pakai NumPy (`np.zeros`), mengisi area piksel untuk membentuk pola/warna, menampilkan dan menyimpan hasil.

Isi:
- `a_bendera_merah_putih.py`
  - Buat canvas ukuran 1080×1920×3.
  - Definisikan batas area (quarter/half/three-quarter).
  - Isi area atas dengan merah (channel R = 255).
  - Isi area bawah dengan putih (R,G,B = 255).
  - Simpan sebagai PNG/JPG.
- `b_bendera_pelangi_horizontal.py`
  - Canvas 1080×1920.
  - Bagi tinggi gambar jadi 5 zona (0–20–40–60–80–100%).
  - Isi warna per zona secara horizontal:
    - zona1: merah, zona2: hijau, zona3: biru, zona4: kuning (R+G), zona5: magenta (R+B).
  - Simpan PNG/JPG.
- `c_bendera_pelangi_vertikal.py`
  - Mirip file horizontal, tapi pembagian zona berdasarkan lebar (kolom) → strip vertikal.
  - Urutan warna per zona dibuat lewat kombinasi kanal RGB.
  - Simpan PNG/JPG.
- `d_simpan_rename_file_looping.py`
  - Baca satu file JPG dari folder output.
  - Simpan ulang file itu 20 kali dengan penamaan berurutan (`...0.jpg` s/d `...19.jpg`).
  - Baca balik beberapa file pertama lalu tampilkan satu per satu dengan jeda (preview animasi sederhana).
- `gambar/`
  - Folder asset/output untuk pertemuan 1.

---

## Pertemuan 2 — Kanal RGB, grayscale (tampilan per channel), manipulasi kanal, efek “kaca”
Inti: baca file gambar (`plt.imread`), akses kanal `[:,:,0/1/2]`, tampilkan sebagai grayscale per kanal, lalu lakukan modifikasi nilai piksel.

Isi:
- `a_grayscale_per_channel.py`
  - Input: `macbook.jpeg`.
  - Tampilkan kanal R, G, B masing-masing sebagai grayscale (`cmap='gray'`).
- `b_grayscale_dan_rgb.py`
  - Sama seperti (a), ditambah tampilkan gambar RGB aslinya.
- `c_grayscale_rgb_manipulasi.py`
  - Input: `gambar\kucing.jpeg`.
  - Tampilkan kanal per-channel + RGB.
  - Lalu manipulasi kanal bertahap:
    - Nolkan merah (`[:,:,0]=0`) → tampil.
    - Nolkan hijau (`[:,:,1]=0`) → tampil.
    - Nolkan biru (`[:,:,2]=0`) → tampil.
- `d_Efek_kaca.py`
  - Input default: `Spiderman.jpeg`.
  - Terapkan efek “kaca” pada setengah kanan gambar:
    - Tentukan area: `x1 = 0.5*col` sampai `x2 = col`, `y1=0` sampai `y2=row`.
    - Skala intensitas area itu dengan `transparansi_kaca` (contoh 0.5) → area jadi lebih gelap/pudar.
  - Tambahkan bingkai pada area kaca dengan warna abu-abu terang, ketebalan proporsional terhadap tinggi gambar.

---

## Pertemuan 4 — Watermark / overlay teks ke foto (blending berbobot)
Inti: gabungkan dua gambar (foto + teks) dengan pembobot (opacity). Overlay hanya diterapkan pada piksel yang dianggap “teks” lewat threshold.

Isi:
- `Watermark.py`
  - Input default:
    - Foto: `Foto_Family.jpg`
    - Teks (gambar): `Selamat_Idulfitri_1447_H.jpg`
  - Pastikan gambar teks punya 3 channel (kalau 2D/grayscale, di-stack jadi RGB).
  - Untuk setiap piksel (loop penuh):
    - Ambil RGB foto dan RGB teks.
    - Jika jumlah RGB teks melewati threshold tertentu, lakukan blending:
      - `foto = w1*foto + w2*teks` dengan `w2 = teks_opacity`.
  - Output: foto yang sudah ditempeli watermark teks.

---

## Pertemuan 5 — Contrast / color enhancement berbasis aturan per-pixel
Inti: tingkatkan kontras/warna dengan threshold intensitas dan normalisasi channel pada piksel yang “berbeda warna”.

Isi:
- `a_contrast_color_enhancement.py`
  - Input default: `gunung_1.jpeg`.
  - Aturan utama:
    - Kalau rata-rata intensitas piksel terlalu gelap (< `lower_contrast_threshold`) → jadi hitam.
    - Kalau terlalu terang (> `upper_contrast_threshold`) → jadi putih.
    - Kalau antar-channel beda besar (threshold selisih/rasio) → lakukan normalisasi:
      - Kurangi nilai minimum channel (shift ke nol).
      - Skala supaya nilai maksimum mendekati 254 (stretching).
  - Hasil: peningkatan kontras dan penonjolan warna pada area yang memenuhi kondisi.

---

## Pertemuan 6 — Pelangi sintetis + “glass effect” overlay ke foto
Inti: buat layer pelangi secara matematis (lingkaran konsentris berwarna) lalu overlay ke gambar asli dengan opacity dan threshold.

Isi:
- `a_efek-kaca_pelangi.py`
  - Input default: `kode_gabungan\gunung_fuji.jpg`.
  - Buat `Gambar_Pelangi` (canvas RGB) ukuran sama dengan gambar asli.
  - Gambar pelangi sebagai lingkaran konsentris (cek jarak kuadrat ke pusat `(a1,b1)` dibanding radius `r1..r8`) dan set warna per radius.
  - Gabungkan ke gambar asli:
    - Untuk setiap piksel, kalau piksel pelangi “cukup berwarna” (jumlah RGB >= threshold) → blending `w1*asal + w2*pelangi`.
  - Simpan output gambar baru.

---

## Pertemuan 7 — Transformasi geometri + grayscale + rescale/pooling
Inti: implementasi operasi dasar spasial dengan loop piksel: flip, rotasi, konversi grayscale, dan downsampling.

Isi:
- `a_horizontal_flip.py`
  - Input: `hakim_side.jpeg`.
  - Buat gambar baru, isi `flipped[y,x] = image[y, col-1-x]` (mirror kiri-kanan).
  - Tampilkan original vs hasil.
- `b_vertikal_flip.py`
  - Input: `hakim_side.jpeg`.
  - `flipped[y,x] = image[row-1-y, x]` (mirror atas-bawah).
- `c1_Rotation_90.py`
  - Rotasi 90° (implementasi manual dengan pemetaan indeks).
- `c2_Rotation_180.py`
  - Rotasi 180° (pemetaan indeks setara flip horizontal+vertikal).
- `d_RGB_to_Grayscale.py`
  - Konversi RGB → grayscale (berbasis operasi channel; implementasi spesifik ada di file).
- `e_rescale_with_pooling.py`
  - Rescale/downsampling dengan pooling (menggabungkan blok piksel menjadi representasi lebih kecil).
