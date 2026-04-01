import numpy as np
import matplotlib.pyplot as plt

#USER ENTRIES
nama_file = "bunga"
faktor_naik = float(7.0)   # Faktor saturasi naik (ngejreng)
faktor_turun = float(0)  # Faktor saturasi turun (pudar)
threshold = 35 #batasn

#MAIN PROGRAM
GbrAsal = plt.imread(nama_file + ".jpeg")
row, col, depth = GbrAsal.shape

plt.figure("Gambar Asal")
plt.imshow(GbrAsal)

Gbr = GbrAsal.copy()
print(Gbr[100,100])

for y in range(0, row):
    for x in range(0, col):        
        gray = (float(Gbr[y,x,0]) + float(Gbr[y,x,1]) + float(Gbr[y,x,2])) / 3
        if (float(Gbr[y,x,0]) + float(Gbr[y,x,1]) + float(Gbr[y,x,2]))/3 > threshold:
            Gbr[y,x,0] = min(max(float(gray + faktor_naik * (float(Gbr[y,x,0]) - gray)), 0), 255)
            Gbr[y,x,1] = min(max(float(gray + faktor_naik * (float(Gbr[y,x,1]) - gray)), 0), 255)
            Gbr[y,x,2] = min(max(float(gray + faktor_naik * (float(Gbr[y,x,2]) - gray)), 0), 255)
        if (float(Gbr[y,x,0]) + float(Gbr[y,x,1]) + float(Gbr[y,x,2]))/3 <= threshold:
            Gbr[y,x,0] = max(min(float(gray + faktor_turun * (float(Gbr[y,x,0]) - gray)), 255), 0)
            Gbr[y,x,1] = max(min(float(gray + faktor_turun * (float(Gbr[y,x,1]) - gray)), 255), 0)
            Gbr[y,x,2] = max(min(float(gray + faktor_turun * (float(Gbr[y,x,2]) - gray)), 255), 0)

plt.figure("Gambar Hasil")
plt.imshow(Gbr)

plt.show()



