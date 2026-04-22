import numpy as np
import matplotlib.pyplot as plt 

image_path = "Looking Right.jpg"
img = plt.imread(image_path)

row, col, depth = img.shape
array_img2 = np.zeros((col, row, depth), dtype=np.uint8)

for y in range(row):
    for x in range(col):
        array_img2[col - 1 - x, y] = img[y, x]

plt.figure(0)
plt.imshow(img)

plt.figure(1)
plt.imshow(array_img2)
plt.show()