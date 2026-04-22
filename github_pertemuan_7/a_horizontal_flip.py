import numpy as np
import matplotlib.pyplot as plt

#user entries
image = plt.imread('hakim_side.jpeg')

#function for flip the image horizontally
def horizontal_flip(image):
    row, col, depth = image.shape
    flipped = np.zeros((row, col, depth), dtype=np.uint8)
    for y in range(row):
        for x in range(col):
            flipped[y, x] = image[y, col - 1 - x]
    return flipped

flipped_img = horizontal_flip(image)

#show the flipped image
plt.figure(1)
plt.imshow(image)
plt.title("Original Image")
plt.axis("off")

plt.figure(2)
plt.imshow(flipped_img)
plt.title("Horizontally Flipped")
plt.axis("off")
plt.show()

