import numpy as np
import matplotlib.pyplot as plt

# USER ENTRIES
nama_file = "bunga"
threshold = 30       # Ambang batas kepekatan awal (selisih RGB)
faktor_naik = 7.0    # Dikali 2 biar makin ngejreng (saturasi naik)
faktor_turun = 0.5   # Dikali 0.5 biar makin pudar (saturasi turun)

# MAIN PROGRAM
# Load gambar dan langsung ubah ke float biar perhitungannya aman dari error limit 0-255
GbrAsal = plt.imread(nama_file + ".jpeg").astype(float)
row, col, depth = GbrAsal.shape

plt.figure("Gambar Asal")
plt.imshow(GbrAsal.astype(np.uint8)) # Kembalikan ke uint8 khusus buat ditampilin

Gbr = GbrAsal.copy()

# Looping pakai konsep 
for y in range(0, row):
    for x in range(0, col):
        
        R = Gbr[y,x,0]
        G = Gbr[y,x,1]
        B = Gbr[y,x,2]
        
        # 1. Cari nilai tengah/abu-abu (Grayscale)
        gray = (R + G + B) / 3.0
        
        # 2. Cari seberapa "pekat" warna asli pixel ini
        # Kalau selisih max dan min besar, berarti warnanya solid/ngejreng
        kepekatan = max(R, G, B) - min(R, G, B)
        
        # 3. Logika Threshold lo masuk di sini
        if kepekatan > threshold:
            faktor = faktor_naik   # Yang udah lumayan pekat, kita gas makin neon!
        else:
            faktor = faktor_turun  # Yang agak kusam, kita sikat deketin ke abu-abu!
            
        # 4. Terapkan rumus saturasi RGB
        new_R = gray + faktor * (R - gray)
        new_G = gray + faktor * (G - gray)
        new_B = gray + faktor * (B - gray)
        
        # 5. Pastikan nilai mentok di batas 0 dan 255 (Clipping)
        Gbr[y,x,0] = min(max(new_R, 0), 255)
        Gbr[y,x,1] = min(max(new_G, 0), 255)
        Gbr[y,x,2] = min(max(new_B, 0), 255)

# Convert balik ke integer 8-bit (0-255) biar pyplot bisa baca warnanya dengan benar
Gbr = Gbr.astype(np.uint8)

plt.figure("Gambar Hasil Saturasi Murni RGB")
plt.imshow(Gbr)

plt.show()