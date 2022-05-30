import cv2    #openCV use as cv2 in python

#Loads a color image. Any transparency of image will be neglected. It is the default flag.
#this function is used to read the image from location
img1 = cv2.imread('C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\boat.jpg',1)
img1 = cv2.resize(img1,(1280,700))#width ,height
print(img1)
cv2.imshow("original",img1)  #It accept two parameters 1)- Name of screen ,2) -  Image
cv2.waitKey(0)  #here parameter inside waitkey handle the life duration of an image
cv2.destroyAllWindows()
