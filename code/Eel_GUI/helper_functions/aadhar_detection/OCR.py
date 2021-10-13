#match = re.match(r"[0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9] [0-9][0-9][0-9][0-9]", string)
#match.group() will be the Aadhar Number

#export GOOGLE_APPLICATION_CREDENTIALS= "C:\Users\Sunit Koodli\OneDrive\Desktop\OCR"

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
def detect_aadhar(path):
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


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    file = 'live.png'
    cv2.imwrite( file,frame)

    # print OCR text
    match=detect_aadhar(file)

    # Display the resulting frame
    cv2.imshow('frame',frame)

    if match!=None:
        print(type(match[0]))
        break

    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
