import numpy as np 
import matplotlib.pyplot as plt 

#user entries
nama_file = 'gambar\\kucing'

#main program
gambar = plt.imread(nama_file + '.jpeg')
# plt.imshow(gambar)
plt.figure(1)
plt.imshow(gambar[:,:,0], cmap='gray')
plt.figure(2)
plt.imshow(gambar[:,:,1], cmap='gray')
plt.figure(3)
plt.imshow(gambar[:,:,2], cmap='gray')

plt.figure(4)
plt.imshow(gambar[:,:,:])

gambar = gambar.copy()
gambar[:,:,0] = 0 #warna merah dinolkan
plt.figure(5)
plt.imshow(gambar[:,:,:])

gambar[:,:,1] = 0 #warna hijau dinolkan
plt.figure(6)
plt.imshow(gambar[:,:,:])

gambar[:,:,2] = 0 #warna biru dinolkan
plt.figure(7)
plt.imshow(gambar[:,:,:])

plt.axis('off')
plt.show()


