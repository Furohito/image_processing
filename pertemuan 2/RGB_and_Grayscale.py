import numpy as np 
import matplotlib.pyplot as plt 

#user entries
nama_file = 'macbook'

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
plt.axis('off')
plt.show()


