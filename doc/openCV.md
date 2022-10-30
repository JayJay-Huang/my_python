## 產生雜訊圖
```py
import cv2
import numpy as np

img = np.random.randint(0, 256, size=[200, 200, 3], dtype=np.uint8)
cv2.imshow("demo", img)
cv2.waitKey(0)
```
demo 2:
```py
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
```
## 灰階
```py
import cv2
img = cv2.imread("./data/img.jpg", 0)
cv2.imshow('img', img)
cv2.waitKey()
```
## 設定值處理: threshold
```py
import cv2
img = cv2.imread("./data/img.jpg")
t,rst = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('img', img)
cv2.imshow('rst', rst)
cv2.waitKey()

cv2.destroyAllWindows()
```
## Otsu
```py
import cv2
img = cv2.imread("./data/img.jpg", 0)
t1, thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
t2, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imshow('img', img)
cv2.imshow('thd', thd)
cv2.imshow('otsu', otsu)

cv2.waitKey()
cv2.destroyAllWindows()
```