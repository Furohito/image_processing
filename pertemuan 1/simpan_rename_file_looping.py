import numpy as np 
import matplotlib.pyplot as plt 

dir = "pertemuan 1/gambar/" #sesuaikan dengan lokasi folder anda
nama_file = "bendera_merah_putih" #sesuaikan dengan nama file anda

pic = plt.imread(dir + nama_file + ".jpg")

for i in range(0, 20):
    plt.imsave(dir + nama_file + str(i) + ".jpg", pic)
    
for i in range(1, 6):
    pic = plt.imread(dir + nama_file + str(i) + ".jpg")
    plt.figure(nama_file + "(" + str(i) + ").jpg")
    plt.imshow(pic)
    plt.ion()
    plt.pause(1)

plt.show()