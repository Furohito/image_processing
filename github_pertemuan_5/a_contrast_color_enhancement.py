import matplotlib.pyplot as plt
import numpy as np

# USER ENTRIES
file = "gunung_1"

nama_file = file + ".jpeg"

col_dif = 40.0 # color difference threshold of every pixel
col_rat = 1.6  # color ratio threshold of every pixel
lower_contrast_threshold = 40.0
upper_contrast_threshold = 230.0

# MAIN PROGRAM
OrigPic = plt.imread(nama_file)
row, col, depth = OrigPic.shape

plt.figure("Before")
plt.imshow(OrigPic)

pic = OrigPic.copy()
avg_all = np.mean(pic, axis=(0,1,2))
print(avg_all)

# Looping through every pixel
for y in range(0, row):
    for x in range(0, col):
        a, b, c = float(pic[y,x,0])+1, float(pic[y,x,1])+1, float(pic[y,x,2])+1
        if (a+b+c)/3 < lower_contrast_threshold:
            pic[y,x] = (0,0,0)
        if (a+b+c)/3 > upper_contrast_threshold:
            pic[y,x] = (255,255,255)
            
        if (abs(a-b)>col_dif or abs(a-c)>col_dif or abs(b-c)>col_dif
            or a/b>col_rat or b/a>col_rat or a/c>col_rat
            or c/a>col_rat or b/c>col_rat or c/b>col_rat):
            MIN = min(pic[y,x])
            pic[y,x] = pic[y,x] - MIN
            # print("row-", y, ":", pic[y,x])
            MAX = max(pic[y,x])
            if MAX > 0: # Tambahan proteksi agar tidak division by zero
                k = 254/MAX
                pic[y,x] = pic[y,x] * k

plt.figure("After")
plt.imshow(pic)
plt.show()
