import eel
import json
import os
import shutil
import base64
from pydub import AudioSegment, effects
from pydub.playback import play
import beepy
from helper_functions.questions_helper import CreateQuestions, Cities
from helper_functions.text_to_speech import speak
from helper_functions.speech_to_text import Speech_to_Text
from helper_functions.face_detection.detect_face import DetectFace
from helper_functions.aadhar_detection.detect_aadhar import DetectAadhar
#from database.query_aadhar_db import queryAadhar
from helper_functions.face_recognition.faceRec import faceRec


response_dict = dict()
downloads_path = os.path.join(os.path.expanduser('~'), 'downloads')
temp = os.path.join(os.path.expanduser('~'), 'temp')

db_path = os.path.join(os.getcwd(), 'helper_functions/face_recognition/db.json')


def genFace(camera):
    while True:
        frame = camera.get_frame()
        if(camera.count==0):
            yield frame
        else:
            yield 1

def genAadhar(camera):
    while True:
        frame = camera.get_frame()
        if(camera.aadhar_number==0):
            yield frame
        else:
            yield camera.aadhar_number

@eel.expose
def aadhar_video():
    x = DetectAadhar()
    y = genAadhar(x)
    
    for each in y:
        #print(each)
        if(type(each)==str):
            #each is holding the aadhar number
            print(each)
            face=faceRec("face.jpg")
            print(face)
            if face == each:
                RetrieveData(each)
                eel.nextPage()()
                break
            else:
                eel.nextPage()()
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
def ReadQuestion(text):
    speech = speak(text)
    audio = AudioSegment.from_mp3(speech)
    audio = effects.speedup(audio, 1.2)
    play(audio) 


@eel.expose
def ListenResponse():
    beepy.beep(sound=6)
    text =  Speech_to_Text()
    if (text):
        return text
    #else:
    #    ReadQuestion("invalid response")
    #    ListenResponse()

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
def SaveData():
    with open("responses.json", "w") as f:
        json.dump(response_dict, f, indent=4)
    eel.sleep(1)
    filename = 'save_to_db.py'
    exec(compile(open(filename, "rb").read(), filename, 'exec'))
    print("SaveData ends")


@eel.expose
def CreateTemp():
    #path = "C://temp"
    try:
        os.mkdir(temp)
    except:
        pass

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
eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])
#eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])

