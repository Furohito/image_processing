import numpy as np
import matplotlib.pyplot as plt

# USER ENTRY
dir = ""
file_input = "hangeul"   # nama file tanpa ekstensi
ext = ".jpeg"

row_crop = 0.05
col_crop = 0.05
m, n, ch = 20, 20, 3
th = 105

def preprocessing(dir, file_input, ext, th):
    pic_ori = plt.imread(dir + file_input + ext)
    row, col = pic_ori.shape[0], pic_ori.shape[1]

    # CROP
    row_margin = round(row_crop * row)
    col_margin = round(col_crop * col)
    pic_crop = pic_ori[row_margin:row-row_margin, col_margin:col-col_margin, :]

    # DOWNSIZE (AVERAGE POOLING)
    pic_asal = pic_crop.astype(np.float16)
    row_asal, col_asal, _ = pic_asal.shape

    pic_res = np.zeros((m, n, ch), dtype=np.float16)

    delta_row = round(row_asal / m)
    delta_col = round(col_asal / n)

    i_res = -1
    for i_asal in range(0, row_asal - delta_row, delta_row):
        i_res += 1
        j_res = -1
        for j_asal in range(0, col_asal - delta_col, delta_col):
            j_res += 1

            block = pic_asal[i_asal:i_asal+delta_row, j_asal:j_asal+delta_col]
            pic_res[i_res, j_res] = np.mean(block, axis=(0, 1))

    # GRAYSCALE
    average = np.mean(pic_res, axis=2)
    pic_gs = np.stack([average]*3, axis=2)

    # INVERT (hitam jadi putih)
    pic_inv = 255 - pic_gs

    # THRESHOLD
    pic_bin = np.where(pic_inv < th, 0, 255)
    pic_bin = np.stack([pic_bin[:,:,0]]*3, axis=2)

    return pic_ori, pic_crop, pic_res, pic_gs, pic_inv, pic_bin

# MAIN (single image)
pic_ori, pic_crop, pic_res, pic_gs, pic_inv, pic_bin = preprocessing(dir, file_input, ext, th)

pic_bin = pic_bin.astype(np.uint8)
# plt.imsave(file_input + "_ready" + ext, pic_bin)

# DISPLAY
plt.figure("ori"); plt.imshow(pic_ori)
plt.figure("crop"); plt.imshow(pic_crop)
plt.figure("resize"); plt.imshow(pic_res.astype(np.uint8))
plt.figure("grayscale"); plt.imshow(pic_gs.astype(np.uint8))
plt.figure("invert"); plt.imshow(pic_inv.astype(np.uint8))
plt.figure("binary"); plt.imshow(pic_bin)

plt.show()