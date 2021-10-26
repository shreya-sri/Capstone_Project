import json

#data = json.loads(open('intents.json').read())
data = json.loads(open('helper_functions/intents_test.json').read())
states_and_cities = json.loads(open('helper_functions/intents_test.json').read())

def CreateQuestions(aadhar_data):
    with open("web/questions.html", "w") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">

<head>
    <title>Welcome!</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="css/main.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link rel="stylesheet" href="css/keyboard.css">
    <link rel="preconnect" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@300&display=swap" rel="stylesheet">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
    <script type="text/javascript" src="/eel.js"></script>
    <script type="text/javascript" src="js/keyboard.js"></script>
    <script type="text/javascript" src="js/main.js"></script>
    <script type="text/javascript" src="js/questions.js"></script>
</head>

<body onload="show_tab(0);">
    <form id="regForm">""")
        f.write("\n")
        keys = list(aadhar_data.keys())
        keys.remove("Photo")
        n = len(keys)
        i = len(keys)
        while i > 0:
            if keys[i-1] == "Photo":
                continue
            f.write("""        <div class="tab animated fadeInTop" id="{}">""".format(n-i))
            f.write("\n")
            f.write("""            <h1 id="question" style="color: rgb(102, 252, 241); font-size: 3.125vw; text-align: center;"> Please enter your """ +  keys[i-1] + "</h1>")
            f.write("\n")
            if keys[i-1] == "Address":
                    f.write("""            <textarea class="txtbox use-keyboard-input" id="response" style="height: 12.5vw;">{}</textarea>""".format(aadhar_data['Address']))
            elif keys[i-1] == "Date of Birth":
                f.write("""            <input type="date" required class="txtbox use-keyboard-input" value="{}" id="response">""".format(aadhar_data['Date of birth']))
            else:
                f.write("""            <input type="text" required class="txtbox use-keyboard-input" value ="{}" required id="response">""".format(aadhar_data[keys[i-1]]))
            f.write("\n")
            f.write("""        </div>""")
            f.write("\n")
            i -= 1

        for i in range(len(data['root'])):
            question = data['root'][i]['question'][-1]
            widget = data['root'][i]['type']
            f.write("""        <div class="tab animated fadeInTop" id="{}">""".format(n+i))
            f.write("\n")
            question_string = """            <h1 id="question" style="color: rgb(102, 252, 241); font-size: 3.125vw; text-align: center;">""" +  question + "</h1>"
            f.write(question_string)
            f.write("\n")
            if widget == 'required':
                if "enter" in question.lower() and "address" in question.lower():
                    f.write("""            <textarea class="txtbox use-keyboard-input" required id="response" style="height: 12.5vw;"></textarea>""")
                elif "date" in question.lower(): 
                    f.write("""            <input type="date" required class="txtbox use-keyboard-input" id="response">""")
                elif "upload" in question.lower():
                    f.write("""            <video  class="video use-keyboard-input" id="response" title="{}" width="480" height="360" autoplay></video>
        <p class="capture">Press c to Capture</p>""".format(question.split(" ")[3]))
                elif "email" in question.lower():
                    f.write("""            <input type="email" required class="txtbox use-keyboard-input" id="response">""")
                elif "number" in question.lower() or "age" in question.lower():
                    f.write("""            <input type="number" required class="txtbox use-keyboard-input" id="response">""")
                else:
                    f.write("""            <input type="text" required class="txtbox use-keyboard-input" id="response">""")
                f.write("\n")
            
            elif widget == 'optional':
                if "enter" in question.lower() and "address" in question.lower():
                    f.write("""            <textarea class="txtbox use-keyboard-input" id="response" style="height: 12.5vw;"></textarea>""")
                elif "date" in question.lower(): 
                    f.write("""            <input type="date" class="txtbox use-keyboard-input" id="response">""")
                elif "upload" in question.lower():
                    f.write("""            <video  class="video use-keyboard-input" id="response" title="{}" width="480" height="360" autoplay></video>
        <p class="capture">Press c to Capture</p>""".format(question.split(" ")[3]))
                elif "email" in question.lower():
                    f.write("""            <input type="email" class="txtbox use-keyboard-input" id="response">""")
                elif "number" in question.lower() or "age" in question.lower():
                    f.write("""            <input type="number" class="txtbox use-keyboard-input" id="response">""")
                else:
                    f.write("""            <input type="text" class="txtbox use-keyboard-input" id="response">""")
                f.write("\n")

            elif widget == 'radio':
                options = data['root'][i]['options']
                name = data['root'][i]['name']
                for j in range(len(options)):
                    f.write("""            <label class="label-radio" style="color: rgb(255, 255, 255); font-size: 3.125vw;">
            <input type="radio" id="response" class="radio-input" name="{n}" value="{v}" required>{v}
        </label>""".format(n = name, v = options[j]))
                    f.write("\n")
                
            elif widget == 'choice':
                name = data['root'][i]['name']
                options = data['root'][i]['options']
                f.write("""            <select name="{}" required class="dropdown" id="response">""".format(name))
                f.write("\n")
                f.write("""                <option value="" style="color: rgb(0, 0, 0); font-size: 1.25vw; text-align: center;">Select</option>""")
                f.write("\n")
                for j in range(len(options)):
                    f.write("""                <option value="{v}" style="color: rgb(0, 0, 0); font-size: 1.25vw; text-align: center;">{v}</option>""".format(v = options[j]))
                    f.write("\n")
                f.write("""            </select>""")
                f.write("\n")
            
            elif widget == 'checkbox':
                name = data['root'][i]['name']
                options = data['root'][i]['options']
                for j in range(len(options)):
                    f.write("""            <label class="label-checkbox" style="color: rgb(255, 255, 255)">
            <input type="checkbox" id="response" name="{n}" value="{v}" required>{v}
        </label>""".format(n = name, v = options[j]))
                    f.write("\n")
            f.write("""        </div>""")
            f.write("\n")
        f.write("""        <button class="prev-button" type="submit" style="display: none;" onclick="next_prev(-1);">Previous</button>
        <button class="next-button" type="submit" onclick="next_prev(1);">Next</button>
    </form>
    <div id="myModal" class="modal">
        <div class="modal-content">
            <span class="close" onclick="close_popup();">&times;</span>
            <p style="color: rgb(102, 252, 241); font-size: 2.5vw; text-align: center;">Confirm Submission?</p>
            <button class="prev-button" style="margin-top: 0; margin-left: 10%; margin-right: 0; padding: 0.625vw 0.625vw; font-size: 1.25vw;" onclick="close_popup();">Go back</button>
            <button class="next-button" style="margin-top: 0; margin-left: 0; margin-right: 10%; padding: 0.625vw 0.625vw; font-size: 1.25vw;" onclick="submit_form();">Confirm</button>
        </div>
    </div>
</body>""")

def Cities(state):
    cities = states_and_cities[state]
    return cities