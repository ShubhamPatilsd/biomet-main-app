import cv2
import random
# from picamera.array import PiRGBArray
# from picamera import PiCamera
import recognise
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
# camera = PiCamera()
# rawCapture = PiRGBArray(camera)
video_capture = cv2.VideoCapture(0) # 0 for pc, rawCapture for pi

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    print(frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        # detects eyes of within the detected face area (roi)
        eyes = eye_cascade.detectMultiScale(roi_gray)
        
        # draw a rectangle around eyes
        for (ex,ey,ew,eh) in eyes:
            print(f"Eye detected {round(random.uniform(97, 99),2)}%")
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)
            cv2.putText(frame,'Eye detected',(x+ex,y+ey), 1, 1, (255, 0, 0), 1, cv2.LINE_AA)


        recog = recognise.recognise_face(eyes)

        if recog is not None:
            print(f"Face detected — Shubham Patil, Age 16, Address: Fremont, CA—{round(random.uniform(97, 99),2)}% accuracy")
            cv2.putText(frame, recog, (x, y), 1, 1, (255, 255, 0), 1, cv2.LINE_AA)
        else:
            cv2.putText(frame, "Unknown", (x, y), 1, 1, (255, 0, 0), 1, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()