import speech_recognition as sr
 
 
def Speech_to_Text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Done")
        try:
            val = r.recognize_google(audio)
            print("Text: " + r.recognize_google(audio))
        except Exception as e:
            val = 0
            print("Error :  " + str(e))
    return val
 
 
if __name__ == "__main__":
    Speech_to_Text()