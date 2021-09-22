import eel
import json
import simpleaudio as sa
from questions_helper import CreateQuestions, Cities
from text_to_speech import speak
from speech_to_text import Speech_to_Text

response_dict = dict()

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
    else:
        ReadQuestion("invalid response")
        ListenResponse()

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

eel.init('web')
eel.start('main.html', size=(1000, 600))
#eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])
