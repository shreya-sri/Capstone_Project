import eel
import json
import os
import shutil
import base64
from pydub import AudioSegment, effects
from pydub.playback import play
from helper_functions.questions_helper import CreateQuestions, Cities
#from helper_functions.create_responses_page import CreateResponsesPage
from helper_functions.text_to_speech import speak
from helper_functions.speech_to_text import Speech_to_Text
from helper_functions.face_detection.detect_face import DetectFace
from helper_functions.aadhar_detection.detect_aadhar import DetectAadhar
from helper_functions.responses_to_json import create_json_db
#from database.query_aadhar_db import queryAadhar
from helper_functions.face_recognition.faceRec import faceRec

from helper_functions.face_recognition import faceRec_train

response_dict = dict()
downloads_path = os.path.join(os.path.expanduser('~'), 'downloads')
temp = os.path.join(os.path.expanduser('~'), 'temp')

db_path = os.path.join(os.getcwd(), 'helper_functions/face_recognition/db.json')


@eel.expose
def ReadQuestion(text):
    speech = speak(text)
    audio = AudioSegment.from_mp3(speech)
    audio = effects.speedup(audio, 1.2)
    play(audio) 


@eel.expose
def ListenResponse():
    text =  Speech_to_Text()
    if (text):
        return text
    else:
        print("No response")
        return None
    #else:
    #    ReadQuestion("invalid response")
    #    ListenResponse()


def genFace(camera):
    while True:
        frame = camera.get_frame()
        if(camera.count==0):
            yield frame
        else:
            yield 1

def genAadhar(camera):
    f=0 #frame number
    while True:
        f+=1
        #print(f)
        frame = camera.get_frame()
        if(camera.aadhar_number==0):
            if(f%15==0):
                #print(f)
                ReadQuestion("Aadhar not detected.")
            yield frame
        else:
            yield camera.aadhar_number

@eel.expose
def aadhar_video():
    ReadQuestion("Please hold your Aadhar card up to the camera.")

    x = DetectAadhar()
    y = genAadhar(x)
    
    for each in y:
        #print(each)
        if(type(each)==str):
            #each is holding the aadhar number
            print("OCR aadhar: ",each)
            face=faceRec("face.jpg")
            print("Face:",face)
            if face == each:
                RetrieveData(each)
                response_dict["Aadhar_number"]=each
                eel.nextPage()()
                break
            else:
                ReadQuestion("Aadhar and face don't match.")
                eel.restart()()
                break
            #print(face," detected in aadhar")
            #print(each," is the actual aadhar")
        else:
            # Convert bytes to base64 encoded str, as we can only pass json to frontend
            blob = base64.b64encode(each)
            blob = blob.decode("utf-8")
            eel.updateImageSrc(blob)()


@eel.expose
def face_video():
    x = DetectFace()
    y = genFace(x)
    for each in y:
        #print(each)
        if(type(each)==int):
            eel.nextPage()()
            break
        else:
            # Convert bytes to base64 encoded str, as we can only pass json to frontend
            blob = base64.b64encode(each)
            blob = blob.decode("utf-8")
            eel.updateImageSrc(blob)()


def RetrieveData(id):
    data = json.loads(open(db_path).read())
    data_dict = data[id]
    CreateQuestions(data_dict)

@eel.expose
def CreateQuestionsPage():
    CreateQuestions()

@eel.expose
def GetCities(state):
    return Cities(state)

@eel.expose
def CheckBox(disability,response):
    responses=response.split()
    for i in responses:
        if(i in disability):
            return 1
    return 0

@eel.expose
def SendData(question, response):
    response_dict[question] = response
    #print(response_dict)

@eel.expose
def GetResponses():
    return response_dict
    #with open("responses.json", "w") as f:
    #    json.dump(response_dict, f, indent=4)
    #eel.sleep(1)
    #CreateResponsesPage()

@eel.expose
def SaveData():
    create_json_db(response_dict)



@eel.expose
def CreateTemp():
    #path = "C://temp"
    try:
        os.mkdir(temp)
    except:
        pass

@eel.expose
def print_terminal(val):
    print(val)

@eel.expose
def DeleteTemp():
    #path = "C://temp"
    shutil.rmtree(temp)

@eel.expose
def AddFile(file):
    eel.sleep(1)
    
    file=file+".png"
    
    #path = "C://temp"
    
    src=os.path.join(downloads_path,file)
    
    dst=os.path.join(temp,file)
    
    #os.rename(src, dst)
    shutil.move(src, dst) 


eel.init('web')
eel.start('detect_face.html', mode='chrome', cmdline_args=['--kiosk'])
#eel.start('user_agreement.html', mode='chrome', cmdline_args=['--kiosk'])

