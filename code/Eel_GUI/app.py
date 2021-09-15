import eel
import json
from playsound import playsound
from questions_helper import CreateQuestions, Cities
from text_to_speech import speak

response_dict = dict()

@eel.expose
def ReadQuestion(text):
    speech = speak(text)
    playsound(speech)

@eel.expose
def CreateQuestionsPage():
    CreateQuestions()

@eel.expose
def GetCities(state):
    Cities(state)

@eel.expose
def SendData(question, response):
    response_dict[question] = response
    #print(response_dict)

@eel.expose
def SaveData():
    with open("responses.json", "w") as f:
        json.dump(response_dict, f, indent=4)

eel.init('web')
eel.start('main.html', size=(1000, 600))
#eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])
