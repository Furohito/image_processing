import numpy as np 
import matplotlib.pyplot as plt 

# user entries
nama_file_foto = 'Foto_Family.jpg'
nama_file_teks = 'Selamat_Idulfitri_1447_H.jpg'
glass_opacity = 0.2
teks_opacity = 0.8 

# main program
foto = plt.imread(nama_file_foto)
foto = foto.copy()
teks = plt.imread(nama_file_teks)

# === PERBAIKAN 1: pastikan teks jadi RGB (3 channel) ===
if len(teks.shape) == 2:
    teks = np.stack((teks,)*3, axis=-1)

row, col, depth = foto.shape
print(row)


w2 = teks_opacity
w1 = 1 - w2

for y in range(0, row):  # mengunjungi pixel ke pixel baris
    print(y)
    for x in range(0, col):  # mengunjungi pixel ke pixel kolom
        r1 = foto[y, x, 0]; g1 = foto[y, x, 1]; b1 = foto[y, x, 2]
        r2 = teks[y, x, 0]; g2 = teks[y, x, 1]; b2 = teks[y, x, 2]

        # === PERBAIKAN 2: threshold untuk skala float (0–1) ===
        if float(r2) + float(g2) + float(b2) >= 100:
            foto[y, x, 0] = w1 * r1 + w2 * r2
            foto[y, x, 1] = w1 * g1 + w2 * g2
            foto[y, x, 2] = w1 * b1 + w2 * b2

plt.figure(1)
plt.imshow(foto)

plt.figure(2)
plt.imshow(teks)
plt.show()



# # buat efek kaca
# y1 = 0; y2 = row
# x1 = round(0.48 * col); x2 = col

# area_kaca = foto[y1:y2, x1:x2]
# # foto[y1:y2, x1:x2] = (area_kaca * transparansi_kaca).astype(np.uint8)
# foto[y1:y2, x1:x2] = foto[y1:y2, x1:x2] * (1 - glass_opacity)

# tebal_bingkai = round(tebal_bingkai * row)  # Konversi ke piksel
# foto[y1:y1+tebal_bingkai, x1:x2] = warna_bingkai  # Bingkai kanan Atas
# foto[y2-tebal_bingkai:y2, x1:x2] = warna_bingkai  # Bingkai kanan Bawah
# foto[y1:y2, x1:x1+tebal_bingkai] = warna_bingkai  # Bingkai kanan Kiri
# foto[y1:y2, x2-tebal_bingkai:x2] = warna_bingkai  # Bingkai kanan Kanan

# # bingkai
# warna_bingkai = (220, 220, 220)  # Abu-abu terang
# tebal_bingkai = 0.02  # Tebal bingkai dalam piksel

# transparansi kaca
# transparansi_kaca = 0.5