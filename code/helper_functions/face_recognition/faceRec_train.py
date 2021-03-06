from imutils import paths
import face_recognition
import pickle
import cv2
import os
import sys


#Get training data
from helper_functions.face_recognition import notion_db
from helper_functions.face_recognition import get_images

#get paths of each file in folder named Images
#Images here contains my data(folders of various persons)
faces_path=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'faces')
print(faces_path)
imagePaths = list(paths.list_images(faces_path))

#print(imagePaths)
knownEncodings = []
knownNames = []
# loop over the image paths
for (i, imagePath) in enumerate(imagePaths):
    # extract the person name from the image path
    name = imagePath.split(os.path.sep)[-2]
    print("training ",name)
    # load the input image and convert it from BGR (OpenCV ordering)
    # to dlib ordering (RGB)
    image = cv2.imread(imagePath)
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #Use Face_recognition to locate faces
    boxes = face_recognition.face_locations(rgb,model='hog')
    # compute the facial embedding for the face
    encodings = face_recognition.face_encodings(rgb, boxes)
    # loop over the encodings
    for encoding in encodings:
        knownEncodings.append(encoding)
        knownNames.append(name)
#save emcodings along with their names in dictionary data
data = {"encodings": knownEncodings, "names": knownNames}
#use pickle to save data into a file for later use
f = open("face_enc", "wb")
f.write(pickle.dumps(data))
f.close()