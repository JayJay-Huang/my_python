import cv2
import numpy as np

img = np.random.randint(0, 256, size=[200, 200, 3], dtype=np.uint8)
cv2.imshow("demo", img)
cv2.waitKey(0)
