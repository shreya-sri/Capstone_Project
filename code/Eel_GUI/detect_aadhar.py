import io
import cv2
import image
import re
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision_v1 import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS']="API_key.json"

# Instantiates a client
client = vision.ImageAnnotatorClient()

class DetectAadhar(object):
    def __init__(self):
        print("init aadhar")
        
        #To capture video from webcam
        self.cap = cv2.VideoCapture(0)

        self.aadhar_number = 0
    
    def detect_aadhar(self,path):
        """Detects text in the file."""
        with io.open(path, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        string = ''

        
        for text in texts:
            string+=' ' + text.description
            
        pattern=r"[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9]"
        match=re.search(pattern,string)

        return match

    def __del__(self):
        print("deconstructed aadhar detection")
        self.cap.release()

    def get_frame(self):
        
        #while True:
            #Read the frame
        _, self.img = self.cap.read()

        file = 'live.png'
        cv2.imwrite( file,self.img)        
        
        match=self.detect_aadhar(file)

        if match!=None:
            self.aadhar_number=match[0]

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

