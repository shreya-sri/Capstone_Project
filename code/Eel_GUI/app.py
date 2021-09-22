import eel
import json
from questions_helper import CreateQuestions, Cities
from text_to_speech import speak
import simpleaudio as sa
import os
import getpass
import shutil
import time


response_dict = dict()
temp = "C://temp"

@eel.expose
def ReadQuestion(text):
    speech = speak(text)
    wave_obj = sa.WaveObject.from_wave_file(speech)
    play_obj = wave_obj.play()
    play_obj.wait_done()

@eel.expose
def CreateQuestionsPage():
    CreateQuestions()

@eel.expose
def GetCities(state):
    return Cities(state)

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
    user=getpass.getuser()
    
    file=file+".png"
    
    #path = "C://temp"
    
    src=os.path.join("C://Users/{}/Downloads/".format(user),file)
    
    dst=os.path.join(temp,file)
    
    #os.rename(src, dst)
    shutil.move(src, dst) 


eel.init('web')
eel.start('main.html', size=(1000, 600))
#eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])
