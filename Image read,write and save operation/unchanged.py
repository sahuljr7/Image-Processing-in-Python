import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\boat.jpg',1)
img1 = cv2.resize(img1,(1280,700))#width ,height
print(img1)
cv2.imshow("original",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image

#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
img2 = cv2.imread('C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\boat.jpg',0)
img2 = cv2.resize(img2,(1280,700))#width ,height
cv2.imshow("Gray Scale Image",img2)
print("Image in gray scale==\n",img2)

#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
img3 = cv2.imread('C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\boat.jpg',-1)
img3 = cv2.resize(img3,(1280,700))#width ,height
cv2.imshow("Original Image",img3)
print("Image in original value==\n",img3)

cv2.waitKey(0)
cv2.destroyAllWindows()

