import cv2
import random
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import recognise

from facedb import FaceDB

# Create a FaceDB instance
db = FaceDB(
    path="facedata",
)


faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# camera = PiCamera()
# rawCapture = PiRGBArray(camera)
video_capture = cv2.VideoCapture(0) # 0 for pc, rawCapture for pi

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()


    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('k'):
        print(frame)
        # name
        face_id = db.add("Shubham", img=frame)

        print(face_id)

    
    if cv2.waitKey(1) & 0xFF == ord('r'):
        result = db.recognize(img=frame)
        print(result)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()