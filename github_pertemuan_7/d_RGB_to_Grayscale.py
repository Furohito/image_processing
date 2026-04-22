import numpy as np 
import matplotlib.pyplot as plt 

#user entries
nama_file = 'hakim_side'

#main program
array_gambar = plt.imread(nama_file + '.jpeg')
image = array_gambar.copy()
# plt.imshow(array_gambar2)
plt.figure(1)
plt.imshow(array_gambar[:,:,0], cmap='gray')
plt.title("Red Channel")
plt.figure(2)
plt.imshow(array_gambar[:,:,1], cmap='gray')
plt.title("Green Channel")
plt.figure(3)
plt.imshow(array_gambar[:,:,2], cmap='gray')
plt.title("Blue Channel")
plt.figure(4)
plt.imshow(image, cmap='gray')
plt.title("Original Image")
plt.axis('off')
plt.show()


