# Image conversion project colored image into grayscale.
import cv2
# First process is to read image
# convert image into grayscale
img1 = cv2.imread("C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\boat.jpg", 0)
img1 = cv2.resize(img1, (560, 700))
# img1 = cv2.flip(img1, 0)  # it accept 3 parameters 0,-1,1
cv2.imshow("converted image==", img1)
k = cv2.waitKey(0) & 0xFF
if k == ord("q"):
    cv2.destroyAllWindows()

elif k == ord("s"):
    cv2.imwrite("C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\ouput.png", img1)  # it accept name of image and data
    cv2.destroyAllWindows()
