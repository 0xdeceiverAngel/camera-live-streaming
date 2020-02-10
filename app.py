
import datetime
from flask import Flask, render_template, Response
import cv2
import threading
app = Flask(__name__)
camera = cv2.VideoCapture(0)
frame=None
# use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
def Capturepic():
    while True:
        success,frame_read = camera.read()  # read the camera frame
        cv2.putText(frame_read,str(datetime.datetime.now()), (0,50 ), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
        ret,buffer = cv2.imencode('.jpg', frame_read,encode_param)
        global frame 
        frame = buffer.tobytes()
        f=open('live_pic.jpg','w+b')
	f.write(frame)
        f.close()
#cv2.putText(encode_param, 'text', (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
#  1, (0, 255, 255), 1, cv2.LINE_AA)
def gen_frames():  # generate frame by frame from camera
    while True:
	
	yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result		
	
	

@app.route('/b59c4546a8548be0c63b860e3018abeb3d2aa0ca08de83ab775ab31ea04124d7/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/b59c4546a8548be0c63b860e3018abeb3d2aa0ca08de83ab775ab31ea04124d7')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    thre=threading.Thread(target=Capturepic)
    thre.start()
    app.run(host='0.0.0.0',port=57631)
