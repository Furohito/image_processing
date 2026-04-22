import numpy as np 
import matplotlib.pyplot as plt 

#user entries
nama_file = 'macbook'

#main program
gambar = plt.imread(nama_file + '.jpeg')
# plt.imshow(gambar)
plt.figure(1)
plt.imshow(gambar[:,:,0], cmap='gray')
plt.figure(2)
plt.imshow(gambar[:,:,1], cmap='gray')
plt.figure(3)
plt.imshow(gambar[:,:,2], cmap='gray')
plt.axis('off')
plt.show()


