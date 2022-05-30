#How to use android device camera as webcam in Opencv.

import cv2

camera = "http://192.168.0.107:8080/video"
#connect your laptop and android device with same network either wifi or hotspot
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   #Here parameter 0 is a path of any video use for webcam
cap.open(camera)
print("check===",cap.isOpened())

#it is 4 byte code which is use to specify the video codec
#Various codec --
#DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*'MP4V')  # *"XVID"
#It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\output.mp4",fourcc,20.0,(640,480))

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame
    if ret == True:
        frame = cv2.resize(frame, (700, 700))
        cv2.imshow('Colorframe', frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press to exit
            break

# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()