import numpy as np 
import matplotlib.pyplot as plt 

#user entries
nama_file = 'kucing'

#main program
array_gambar2 = plt.imread(nama_file + '.jpeg')
# plt.imshow(array_gambar2)
plt.figure(1)
plt.imshow(array_gambar2[:,:,0], cmap='gray')
plt.figure(2)
plt.imshow(array_gambar2[:,:,1], cmap='gray')
plt.figure(3)
plt.imshow(array_gambar2[:,:,2], cmap='gray')

plt.figure(4)
plt.imshow(array_gambar2[:,:,:])

gambar = array_gambar2.copy()
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


