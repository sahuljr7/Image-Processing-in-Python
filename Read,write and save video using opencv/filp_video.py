# Capture  video from webcam and save it

import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # Here parameter 0 is a path of any video use for webcam
print("check===", cap.isOpened())

# it is 4 byte code which is use to specify the video codec
# Various codec --
# DIVX, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")  # *"XVID"
# It contain 4 parameter , name, codec,fps,resolution
output = cv2.VideoWriter("C:\\Users\\Vishal\\PycharmProjects\\pythonProject\\Image Processing\\Data\\flip.avi", fourcc, 20.0, (640, 480))

while (cap.isOpened()):
    ret, frame = cap.read()  # here read the frame

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # here flip is used to lip the video at recording time
        frame = cv2.flip(frame, 0)
        output.write(frame)

        cv2.imshow('Colorframe', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # press to exit
            break
    else:
        break

# Release everything if job is finished
cap.release()
output.release()
cv2.destroyAllWindows()