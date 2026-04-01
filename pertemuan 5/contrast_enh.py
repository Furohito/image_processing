import numpy as np
import matplotlib.pyplot as plt

#USER ENTRIES
nama_file = "bunga"
delta_contrast = float(40)
threshold = 127

#MAIN PROGRAM
GbrAsal = plt.imread(nama_file + ".jpeg")
row, col, depth = GbrAsal.shape

plt.figure("Gambar Asal")
plt.imshow(GbrAsal)

Gbr = GbrAsal.copy()
print(Gbr[100,100])

for y in range(0, row):
    for x in range(0, col):
        if (float(Gbr[y,x,0]) + float(Gbr[y,x,1]) + float(Gbr[y,x,2]))/3 > threshold:
            Gbr[y,x,0] = min (float((Gbr[y,x,0]) + delta_contrast), 255)
            Gbr[y,x,1] = min (float((Gbr[y,x,1]) + delta_contrast), 255)
            Gbr[y,x,2] = min (float((Gbr[y,x,2]) + delta_contrast), 255)
        if (float(Gbr[y,x,0]) + float(Gbr[y,x,1]) + float(Gbr[y,x,2]))/3 <= threshold:
            Gbr[y,x,0] = max (float((Gbr[y,x,0]) - delta_contrast), 0)
            Gbr[y,x,1] = max (float((Gbr[y,x,1]) - delta_contrast), 0)
            Gbr[y,x,2] = max (float((Gbr[y,x,2]) - delta_contrast), 0)

plt.figure("Gambar Hasil")
plt.imshow(Gbr)

plt.show()