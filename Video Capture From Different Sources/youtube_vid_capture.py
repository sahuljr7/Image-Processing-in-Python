# Capture video from youtube
import pafy
import cv2
url = "https://www.youtube.com/watch?v=SLD9xzJ4oeU"
data = pafy.new(url )
data = data.getbest(preftype="mp4")
cap = cv2.VideoCapture()   #Here parameter 0 is a path of any video use for webcam
cap.open(data.url)

while(cap.isOpened()):
    ret, frame = cap.read()   #here read the frame

    if ret==True:
        frame = cv2.resize(frame, (700, 700))
        gray  = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        #here flip is used to lip the video at recording time
        #frame = cv2.flip(frame,0)
        #output.write(gray)

        cv2.imshow("Gray Frame",gray)
        cv2.imshow('Colorframe',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):   #press to exit
            break
    else:
        break

# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()
