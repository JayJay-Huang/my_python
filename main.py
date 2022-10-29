import cv2
import numpy as np

img = np.random.randint(0, 256, size=[200, 200, 3], dtype=np.uint8)
for i in range(100, 150):
    for j in range(100, 150):
        img.itemset((i, j, 0), 0)
        img.itemset((i, j, 1), 0)
        img.itemset((i, j, 2), 0)
cv2.imshow("demo", img)
cv2.waitKey(0)
