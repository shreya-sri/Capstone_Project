import json
from PyQt5 import QtCore, QtGui, QtWidgets
from Create_Widgets import CreateWidgets

data = json.loads(open('../backend/intents.json').read())
#states_and_cities = json.loads(open('../backend/states_and_cities.json').read())
#print(list(set( dic['name'] for dic in states_and_cities if dic['state'] == 'Karnataka')))
#print(list(set( dic['state'] for dic in states_and_cities)))
#print(len(set( dic['state'] for dic in states_and_cities)))

def Get_Question_and_Widget(i):
    question = data['root'][i]['question']
    intent = data['root'][i]['intent']
    widget = data['root'][i]['type']
    response_widgets = []
    
    question_text = CreateWidgets.create_Label()
    question_text.setText(question[-1])
    
    if widget == 'required' or widget == 'optional':
        
        if "enter" in question[-1].lower() and "address" in question[-1].lower():
            response_widget = CreateWidgets.create_MultiTextBox()
            
        elif "upload" in question[-1].lower():
            response_widget = CreateWidgets.create_Button()
            response_widget.setText("Upload")
        
        else:
            response_widget = CreateWidgets.create_TextBox()
            reg_ex = QtCore.QRegExp("[0-9]+")
            if intent == "age":
                response_widget.setMaxLength(3)
                input_validator = QtGui.QRegExpValidator(reg_ex, response_widget)
                response_widget.setValidator(input_validator)
            elif intent == "number":
                input_validator = QtGui.QRegExpValidator(reg_ex, response_widget)
                response_widget.setValidator(input_validator)
                if "phone" in question[-1].lower() or "mobile" in question[-1].lower():
                    response_widget.setMaxLength(10)    
                    
            
        response_widgets.append(response_widget)
        
        
    elif widget == 'radio':
        for option in data['root'][i]['options']:
            radio = CreateWidgets.create_Radio()
            if len(option) > 10:
                option = option[:10] + "\n" + option[11:]
            radio.setText(option)
            response_widgets.append(radio)
        
    elif widget == 'choice':
        dropdown = CreateWidgets.create_DropDown()
        dropdown.addItem("Select")
        if "state" not in question[-1].lower() and "city" not in question[-1].lower():
            dropdown.addItems(data['root'][i]['options'])
        response_widgets.append(dropdown)
    
    elif widget == 'checkbox':
        for option in data['root'][i]['options']:
            checkbox = CreateWidgets.create_CheckBox()
            if len(option) > 31:
                option = option[:31] + "\n" + option[32:]
            checkbox.setText(option)
            response_widgets.append(checkbox)
            
    return question_text, response_widgets

    
    