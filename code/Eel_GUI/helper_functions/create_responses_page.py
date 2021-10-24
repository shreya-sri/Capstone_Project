import json

#data = json.loads(open('intents.json').read())
data = json.loads(open('../responses.json').read())
#states_and_cities = json.loads(open('helper_functions/intents_test.json').read())

def CreateResponsesPage():
    with open("../web/show_responses.html", "w") as f:
        f.write("""<!DOCTYPE html>
<html lang="en">

<head>
    <title>Responses</title>
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

<body>
    <div class="div1 animated fadeInTop">
        <h1 style="color: #66fcf1; font-size: 4.5vw; text-align: center;">Your Responses</h1>
        <table>""")
        f.write("\n")
        for i in data:
            question = i
            response = data[i]
            f.write("""            <tr>
                <td>""")
            f.write("""<h1 id="question" style="color: rgb(102, 252, 241); font-size: 1.5625vw;">""" +  question + "</h1>")
            f.write(" </td>")
            f.write("\n")
            f.write("""                <td>""")
            f.write("""<h1 id="question" style="color: rgb(102, 252, 241); font-size: 1.5625vw;">""" +  response + "</h1>")
            f.write("""</td>
            </tr>""")
            f.write("\n")
        f.write("""        </table>
        <button class="continue" type="submit" style="display:block;" onclick="next_prev(1);">Submit</button>
        <div id="myModal" class="modal">
            <div class="modal-content">
                <span class="close" onclick="close_popup();">&times;</span>
                <p style="color: rgb(102, 252, 241); font-size: 2.5vw; text-align: center;">Confirm Submission?</p>
                <button class="prev-button" style="margin-top: 0; margin-left: 10%; margin-right: 0; padding: 0.625vw 0.625vw; font-size: 1.25vw;" onclick="close_popup();">Go back</button>
                <button class="next-button" style="margin-top: 0; margin-left: 0; margin-right: 10%; padding: 0.625vw 0.625vw; font-size: 1.25vw;" onclick="submit_form();">Confirm</button>
            </div>
        </div>
    </div>
</body>""")

if __name__ == "__main__":
    CreateResponsesPage()