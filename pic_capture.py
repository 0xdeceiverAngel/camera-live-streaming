import cv2
import datetime
import time
cap = cv2.VideoCapture(0)
while(1):


    # get a frame
    ret, frame = cap.read()
    # show a frame
    #cv2.imshow("capture", frame)
    times = datetime.datetime.now()
    loca="/home/u/pic/"+str(time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()))+".jpg"
    #loca="/home/u/pic/"+str(times.year)+"-"+str(times.month)+"-"+str(times.day)+"-"+str(times.hour)+"-"+str(times.minute$    print(loca)
    cv2.imwrite(loca, frame)
    time.sleep(1)
cv2.destroyAllWindows()