import numpy as np
import matplotlib.pyplot as plt

#USER ENTRIES
nama_file = "bunga"
delta_I = 50

#MAIN PROGRAM
GbrAsal = plt.imread(nama_file + ".jpeg")
row, col, depth = GbrAsal.shape
plt.figure("Gambar Asal")
plt.imshow(GbrAsal)
Gbr = GbrAsal.copy()
for y in range(0, row):
    for x in range(0, col):
        Gbr[y, x, :] = Gbr[y, x, :] + delta_I

plt.figure("Gambar Hasil")
plt.imshow(Gbr)

plt.show()

