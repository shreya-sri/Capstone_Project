import cv2
import os

class DetectFace(object):
    def __init__(self):
        print("init face")
        #Load the cascade
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        
        #To capture video from webcam
        self.cap = cv2.VideoCapture(0)

        self.count = 0
        
        #To use a video file as input 
        #cap = cv2.VideoCapture('filename.mp4')
        
        #Variable to give a cue when a face is first detected
                
            #Display
            #cv2.imshow('img', self.img)

        #Stop if 'q' is pressed
        #if cv2.waitKey(1) == ord('q'):
        #    break

    def __del__(self):
        print("deconstructed face detection")
        self.cap.release()

    def get_frame(self):
        
        #while True:
            #Read the frame
        _, self.img = self.cap.read()
            
            #Convert to grayscale
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
            
            #Detect the faces
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 4)
            
        if self.count == 0:
            if len(faces)> 0: #Len of faces is >0 only when a face is detected, else it is just "()"
                print("Face detected")
                self.count += 1  #Frames are continuously read from live webcam, so the above statement is printed only once when the face is intially detected
                
            #Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(self.img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        ret, jpeg = cv2.imencode('.jpg', self.img)
        return jpeg.tobytes()
    # Release the VideoCapture object
    #cap.release()
    #cv2.destroyAllWindows()
    #cv2.waitKey(1)
    #return 1

if __name__=="__main__":
    DetectFace()
    #os.system('app.py')

