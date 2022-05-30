import cv2

#Here with the help of videoCapture fucntion we easily ready any video.
#Here parameter is a path of any video
cap = cv2.VideoCapture("C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\valorant.mp4")
print("cap",cap)

while True:
    ret, frame = cap.read()   #here read the frame
    frame = cv2.resize(frame, (700, 450))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Colorframe', frame)
    cv2.imshow("Gray Frame", gray)
    k = cv2.waitKey(25)
    if k == ord("q"):
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()

