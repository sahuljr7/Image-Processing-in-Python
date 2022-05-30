#Capture  video from webcam and save it

import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
print(cap)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
        frame = cv2.resize(frame, (700, 450))
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gray Frame", gray)
        cv2.imshow('Colorframe', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press to exit
            break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()