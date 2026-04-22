import numpy as np 
import matplotlib.pyplot as plt 

#user entries
nama_file = 'Spiderman'
#bingkai
warna_bingkai= (220, 220, 220) # Abu-abu terang
tebal_bingkai = 0.02 # Tebal bingkai dalam piksel
#transparansi kaca
transparansi_kaca = 0.5

#main program
gambar = plt.imread(nama_file + '.jpeg')

row, col, depth = gambar.shape
print(row)

#buat efek kaca
gambar = gambar.copy()
y1 = 0; y2 = row
x1 = round(0.5 * col); x2 = col

area_kaca = gambar[y1:y2, x1:x2]
# gambar[y1:y2, x1:x2] = (area_kaca * transparansi_kaca).astype(np.uint8)
gambar[y1:y2, x1:x2] = (gambar[y1:y2, x1:x2] * transparansi_kaca)

tebal_bingkai = round(tebal_bingkai * row) # Konversi ke piksel
gambar[y1:y1+tebal_bingkai, x1:x2] = warna_bingkai # Bingkai kanan Atas
gambar[y2-tebal_bingkai:y2, x1:x2] = warna_bingkai # Bingkai kanan Bawah
gambar[y1:y2, x1:x1+tebal_bingkai] = warna_bingkai # Bingkai kanan Kiri
gambar[y1:y2, x2-tebal_bingkai:x2] = warna_bingkai # Bingkai kanan Kanan


plt.imshow(gambar)

plt.show()














# array_gambar2 = plt.imread(nama_file + '.jpeg')
# # plt.imshow(array_gambar2)
# plt.figure(1)
# plt.imshow(array_gambar2[:,:,0], cmap='gray')
# plt.figure(2)
# plt.imshow(array_gambar2[:,:,1], cmap='gray')
# plt.figure(3)
# plt.imshow(array_gambar2[:,:,2], cmap='gray')

# plt.figure(4)
# plt.imshow(array_gambar2[:,:,:])

# gambar_merah = array_gambar2.copy()
# gambar_merah[:,:,0] = 0 #warna merah dinolkan
# plt.figure(5)
# plt.imshow(gambar_merah[:,:,:])

# gambar_hijau = array_gambar2.copy()
# gambar_hijau[:,:,1] = 0 #warna hijau dinolkan
# plt.figure(6)
# plt.imshow(gambar_hijau[:,:,:])

# gambar_biru = array_gambar2.copy()
# gambar_biru[:,:,2] = 0 #warna biru dinolkan
# plt.figure(7)
# plt.imshow(gambar_biru[:,:,:])

# plt.axis('off')
# plt.show()


