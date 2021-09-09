import json
import nltk
import enchant
import re

from nltk.corpus import wordnet

intents = json.loads(open('intents.json').read())


def get_Question(i, intents):
    question = intents['root'][i]['question'][0]
    intent = intents['root'][i]['intent']
    return question, intent

def getFile():
    return "filepath"


english = enchant.Dict("en_US")

#names = json.loads(open('names.json').read())
#"shreya" in names['s']['h']

print(set([intents['root'][i]['intent'] for i in range(len(intents['root']))]))

responses = []
i = 0
print("Welcome! lets start filling the form!!")
print("\n")
while (i < len(intents['root'])):
    response_dict = dict()
    question , intent = get_Question(i, intents)
    print(question)
    response = input()
    
    if intent == "name":
        check = response.lower().split()
        if "name" in check:
            response_dict['question'] = question
            response_dict['response'] = [word for word in check if not english.check(word)]
            responses.append(response_dict)
        elif len(check) == 1 and not english.check(check[0]):
            response_dict['question'] = question
            response_dict['response'] = response
            responses.append(response_dict)
        else:
            print("invalid response")
            i-=1
        
    elif intent == "date":
        response=response.lower().split()
        months={'january':1,'february':2,'march':3,'april':4,'may':5,'june':6,'july':7,'august':8,'september':9,'october':10,'november':11,'december':12}
        
        while(True):
            try:
                day=response[0][:2]
                month=str(months[response[1]])
                year=response[2]
                
                response_dict['question'] = question
                response_dict['response'] = day+"/"+month+"/"+year
                responses.append(response_dict)
                break
            
            except:
                print('invalid response, please repeat in "dd month yyyy" format')
                i-=1
                
    elif intent == "age":
        if len(response) > 3 or response.isnumeric() == False:
            print("invalid response")
            i-=1
        else:
            response_dict['question'] = question
            response_dict['response'] = response
            responses.append(response_dict)
    
    elif intent == "email":
        check = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if not re.match(check, response):
            print("invalid response")
            i-=1
        else:
            response_dict['question'] = question
            response_dict['response'] = response
            responses.append(response_dict)
            
    elif intent == "number":
        if not response.isnumeric():
            print("invalid response")
            i-=1
        else:
            response_dict['question'] = question
            response_dict['response'] = response
            responses.append(response_dict)
            
    elif intent == "select":
        if response in intents['root'][i]['options']:
            response_dict['question'] = question
            response_dict['response'] = response
            responses.append(response_dict)
        else:
            print("invalid option. please repeat.")
            i-=1
               
    elif intent == "multiselect":
        response=response.lower()
        
        choices=[]
        
        for option in intents['root'][i]['options']:
            option=option.lower()
            if option in response:
                choices.append(option)
                
        response_dict['question'] = question
        response_dict['response'] = choices
        responses.append(response_dict)
        
    elif intent == "file":
        response=getFile()
        print("received file")
        
        response_dict['question'] = question
        response_dict['response'] = response
        responses.append(response_dict)
    
    else: 
        response_dict['question'] = question
        response_dict['response'] = response
        responses.append(response_dict)
    
    i+=1
    