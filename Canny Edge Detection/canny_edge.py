import cv2
import numpy as np

#load image into gray scale
img = cv2.imread("C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\building.jpg")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#canny(img,thresh1,thres2)thresh 1 and thresh2 at different lvl
canny = cv2.Canny(img_gray,20,150)
cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("canny==",canny)
cv2.waitKey(0)
cv2.destroyAllWindows()