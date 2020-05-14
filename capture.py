import numpy as np
import cv2
import os

cap = cv2.VideoCapture('The Tokyo 2020 Kinetic Sports Pictograms.mp4')
no = 0
while(cap.isOpened()):
    ret, frame = cap.read()  # ret返回布尔量

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imwrite('%05d.jpg' % no, gray)
    no += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()