import eel
import json
import simpleaudio as sa
from questions_helper import CreateQuestions, Cities
from text_to_speech import speak
from speech_to_text import Speech_to_Text
from detect_face import DetectFace
import os
import shutil
import time


response_dict = dict()
downloads_path = os.path.join(os.path.expanduser('~'), 'downloads')
temp = os.path.join(os.path.expanduser('~'), 'temp')



@eel.expose
def ReadQuestion(text):
    speech = speak(text)
    wave_obj = sa.WaveObject.from_wave_file(speech)
    play_obj = wave_obj.play()
    play_obj.wait_done()

@eel.expose
def ListenResponse():
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
    time.sleep(1)
    
    file=file+".png"
    
    #path = "C://temp"
    
    src=os.path.join(downloads_path,file)
    
    dst=os.path.join(temp,file)
    
    #os.rename(src, dst)
    shutil.move(src, dst) 




DetectFace()
eel.init('web')
eel.start('main.html', mode='chrome_app', size=(1000, 600))
#eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])

