import io
import eel
import json

from text_to_speech import speak

speak("Some shit")

data = json.loads(open('../backend/intents.json').read())

@eel.expose
def get_num():
    return len(data['root'])

@eel.expose
def get_question(val):
    if val >= len(data['root']):
        return ""
    else:
        question = data['root'][val]['question'][-1]
        intent = data['root'][val]['intent']
        widget = data['root'][val]['type']
        if widget == 'required' or widget == 'optional':
            if "enter" in question.lower() and "address" in question.lower():
                response = "multi_textbox"
            elif "date" in question.lower(): 
                response = "date"
            elif "upload" in question.lower():
                response = "camera"
            elif "email" in question.lower():
                response = "email"
            elif "number" in question.lower() or "age" in question.lower():
                response = "number"
            else:
                response = "textbox"
                   
        elif widget == 'radio':
            options = data['root'][val]['options']
            name = data['root'][val]['name']
            response = "radio:" + name + "/" + ",".join(options)
            
        elif widget == 'choice':
            name = data['root'][val]['name']
            options = data['root'][val]['options']
            response = "dropdown:" + name + "/" + ",".join(options)
        
        elif widget == 'checkbox':
            name = data['root'][val]['name']
            options = data['root'][val]['options']
            response = "checkbox:" + name + "/" + ",".join(options)
    return [question, response]

eel.init('web')
eel.start('main.html', size=(1000, 600))
#eel.start('main.html', mode='chrome', cmdline_args=['--kiosk'])
