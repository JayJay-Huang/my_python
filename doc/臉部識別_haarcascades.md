##

```py
import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')


def detect(filename):
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, )

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y + h, x:x + w]
        eyes = eye_cascade.detectMultiScale(roi_gray,
                                            scaleFactor=1.2,
                                            minNeighbors=3,
                                            minSize=(40, 40), )
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        for (ex, ey, ew, eh) in eyes:
            img = cv2.rectangle(img, (x + ex, y + ey), (x + ex + ew, y + ey + eh), (0, 255, 0), 2)

    cv2.imwrite('data/hero_3.jpg', img)

detect('./data/hero.jpg')
```