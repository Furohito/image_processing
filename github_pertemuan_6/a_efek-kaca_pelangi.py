#This program has been written by Mohamamd Nasucha, Ph.D.
print ("\033c")
import matplotlib.pyplot as plt
import numpy as np

#USER ENTRIES
nama_file_asal = "kode_gabungan\\gunung_fuji"
opacity_pelangi = 0.1
opacity_gambar_asal = 1.0-0.2

#MAIN PROGRAM
gambar_asal = plt.imread(nama_file_asal + ".jpg")
plt.figure("Gambar Asal")
plt.imshow(gambar_asal)

#Menyamakan Ukuran Gambar Pelangi dan Gambar Asal
row, col, ch = gambar_asal.shape
rowmax = round(row)
colmax = round(col)

#Titik Pusat, Batas-batas dan Warna Pelangi yang Akan Di-create
a1, b1 = round(1.4*rowmax), round(-0.35*colmax)        #titik pusat
r1     = round(2.0*rowmax); warna_1 = [255, 0, 0]
r2     = round(0.93*r1); warna_2 = [255, 140, 0]
r3     = round(0.90*r1); warna_3 = [255, 255, 0]
r4     = round(0.88*r1); warna_4 = [0, 255, 0]
r5     = round(0.86*r1); warna_5 = [0, 0, 255]
r6     = round(0.84*r1); warna_6 = [140, 0, 255]
r7     = round(0.82*r1); warna_7 = [255, 0, 255]
r8     = round(0.80*r1); warna_hitam = [0, 0, 0]

#Create Gambar Pelangi
Gambar_Pelangi = np.zeros(shape=(rowmax+1, colmax+1, 3), dtype=np.uint8)
batas_bawah = round(rowmax)

for i in range(batas_bawah-r1, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r1**2:
            Gambar_Pelangi[i,j,:] = warna_1

for i in range(batas_bawah-r2, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r2**2:
            Gambar_Pelangi[i,j,:] = warna_2

for i in range(batas_bawah-r3, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r3**2:
            Gambar_Pelangi[i,j,:] = warna_3

for i in range(batas_bawah-r4, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r4**2:
            Gambar_Pelangi[i,j,:] = warna_4

for i in range(batas_bawah-r5, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r5**2:
            Gambar_Pelangi[i,j,:] = warna_5

for i in range(batas_bawah-r6, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r6**2:
            Gambar_Pelangi[i,j,:] = warna_6

for i in range(batas_bawah-r7, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r7**2:
            Gambar_Pelangi[i,j,:] = warna_7

for i in range(batas_bawah-r8, batas_bawah ):
    for j in range(0, colmax):
        if (i-a1)**2 + (j-b1)**2 <= r8**2:
            Gambar_Pelangi[i,j,:] = warna_hitam
plt.figure("Gambar Pelangi")
plt.imshow(Gambar_Pelangi)

#Gabungkan Kedua Gambar dengan "Glass Effect"
Gambar_Hasil = gambar_asal.copy()

w2 = opacity_pelangi
w1 = 1- w2
for y in range(0, rowmax):
    print(y)
    for x in range(0, colmax):
        r1 = gambar_asal[y,x,0]; g1 = gambar_asal[y,x,1]; b1 = gambar_asal[y,x,2]
        r2 = Gambar_Pelangi[y,x,0]; g2 = Gambar_Pelangi[y,x,1]; b2 = Gambar_Pelangi[y,x,2]
        if float(r2) +float(g2) + float(b2) >= 100: 
            Gambar_Hasil[y,x,0] = w1*r1 + w2*r2
            Gambar_Hasil[y,x,1] = w1*g1 + w2*g2
            Gambar_Hasil[y,x,2] = w1*b1 + w2*b2

plt.figure("Gambar_Hasil")
plt.imshow(Gambar_Hasil)

plt.imsave(nama_file_asal + "new.jpg", Gambar_Hasil)
plt.show()