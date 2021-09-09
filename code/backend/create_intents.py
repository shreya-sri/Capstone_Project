import re
import json

f = open("questions.txt", "r")
text = f.read()
f.close()

sample = """[required] First name:
[optional] Middle name:
[optional] Last name:
[optional] Father's name:
[optional] Mother's name:
[required] Date of birth:
[required] Age:
[required] Mobile No.
[required] Email ID:
[choice] Gender:
---------
Other
Male
Female
Transgender
Gender non-Conforming"""

def clean_and_format(text):
    text = re.sub("<02,00,000", "less than two lakh", text)
    text = re.sub("02,00,000-05,00,000", "two to five lakh", text)
    text = re.sub(">05,00,000", "above five lakh", text)
    text = re.sub(":", "", text)
    text = re.sub("[^\w\s\'\[]]", " ", text)
    lines = text.split("\n")
    
    while ("" in lines):
        lines.remove("")
    
    for line in lines:
        if "--" in line:
            lines.remove(line)
    
    new_text = []
    
    for line in lines:
        sentence = line.split()
        
        if sentence[0][0] == '[':
            sentence[1:len(sentence)+1] = [' '.join(sentence[1:len(sentence)+1])]
        
        else:
            sentence[0:] = [" ".join(sentence[0:])]
        new_text.append(sentence)
    
    return new_text


def create_intents(text):
    intents_list = []
    questions = clean_and_format(text)
    
    for i in range(len(questions)):
        intents = dict()
        
        if "required" in questions[i][0]:
            intents['type'] = "required"
            
            if "name" in questions[i][1].lower():
                intents['intent'] = "name"
            elif "date" in questions[i][1].lower():
                intents['intent'] = "date"
            elif "age" in questions[i][1].lower().split():
                intents['intent'] = "age"
            elif "no." in questions[i][1].lower() or "number" in questions[i][1].lower():
                intents['intent'] = "number"
            elif "email" in questions[i][1].lower():
                intents['intent'] = "email"
            elif "upload" in questions[i][1].lower():
                intents['intent'] = "file"
            else:
                intents['intent'] = "text"
                
            if "Upload" in questions[i][1] or "Enter" in questions[i][1]:
                temp = questions[i][1].split(' ', 1)
                intents['question'] = ["Please " + temp[0] + " your " + temp[1] + ". This field is required."]
            else:
                intents['question'] = ["Please enter your " + questions[i][1] + ". This field is required."]
        
        elif "optional" in questions[i][0]:
            intents['type'] = "optional"
            
            if "name" in questions[i][1].lower():
                intents['intent'] = "name"
            elif "date" in questions[i][1].lower():
                intents['intent'] = "date"
            elif "age" in  questions[i][1].lower().split():
                intents['intent'] = "age"
            elif "no." in questions[i][1].lower() or "number" in questions[i][1].lower():
                intents['intent'] = "number"
            elif "email" in questions[i][1].lower():
                intents['intent'] = "email"
            elif "upload" in questions[i][1].lower():
                intents['intent'] = "file"
            else:
                intents['intent'] = "text"
                
            if "Upload" in questions[i][1] or "Enter" in questions[i][1]:
                temp = questions[i][1].split(' ', 1)
                intents['question'] = ["Please " + temp[0] + " your " + temp[1] + "."]       
            else:
                intents['question'] = ["Please enter your " + questions[i][1] + "."]
       
        elif "choice" in questions[i][0]:
            intents['type'] = "choice"
            intents['intent'] = "select"
            j = i+1
            temp = []
            
            while (j):
                if j == len(questions)-1 or '[' in questions[j][0]:
                    break
                temp.append(questions[j][0])
                j+=1
            
            
            if "Upload" in questions[i][1] or "Enter" in questions[i][1]:
                temp2 = questions[i][1].split(' ', 1)
                intents['question'] = ["Please select your " + temp2[1] + "."]
                intents['options'] = [i for i in temp]
            else:
                intents['question'] = ["Please select your " + questions[i][1] + "."]
                intents['options'] = [i for i in temp]
        
        elif "radio" in questions[i][0]:
            intents['type'] = "radio"
            intents['intent'] = "selelct"
            j = i+1
            temp = []
            
            while (j):
                if (j == len(questions)-1 or '[' in questions[j][0]):
                    break
                temp.append(questions[j][0])
                j+=1
            
            intents['question'] = ["Please select your " + questions[i][1] + ". Select one of the following."]
            intents['options'] = [i for i in temp] 
        
        elif "checkbox" in questions[i][0]:
            intents['type'] = "checkbox"
            intents['intent'] = "multiselect"
            j = i+1
            temp = []
            
            while (j):
                if j == len(questions)-1 or '[' in questions[j][0]:
                    break
                temp.append(questions[j][0])
                j+=1
            
            intents['question'] = ["Please select your " + questions[i][1] + ". You can select more than option."]
            intents['options'] = [i for i in temp] 
        
        else:
            continue
        
        intents_list.append(intents)
    
    return intents_list


intents_list = create_intents(text)

intents_dict = {"root": intents_list}
#print(intents_dict)

f = open("intents.json", "w")
json.dump(intents_dict, f, indent=4)
f.close()

