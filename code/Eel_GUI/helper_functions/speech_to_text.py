import speech_recognition as sr
 
 
def Speech_to_Text():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        print("Done")

        try:
            print("Text: " + r.recognize_google(audio))
            return r.recognize_google(audio).lower()

        except Exception as e:
            print("Error :  " + str(e))
            return 0
    
 
 
if __name__ == "__main__":
    Speech_to_Text()

