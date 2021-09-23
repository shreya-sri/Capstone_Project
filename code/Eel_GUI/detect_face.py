import cv2
import os

def DetectFace():
    
    #Load the cascade
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    #To capture video from webcam
    cap = cv2.VideoCapture(0)
    
    #To use a video file as input 
    #cap = cv2.VideoCapture('filename.mp4')
    
    #Variable to give a cue when a face is first detected
    count = 0
    
    while True:
        #Read the frame
        _, img = cap.read()
        
        #Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
        if count == 0:
            if len(faces)> 0: #Len of faces is >0 only when a face is detected, else it is just "()"
                print("Face detected")
                count += 1  #Frames are continuously read from live webcam, so the above statement is printed only once when the face is intially detected
                break
            
        #Draw the rectangle around each face
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
        #Display
        cv2.imshow('img', img)
    
        
        #Stop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
        
    # Release the VideoCapture object
    cap.release()
    cv2.destroyAllWindows()
    return 1

if __name__=="__main__":
    DetectFace()
    #os.system('app.py')

