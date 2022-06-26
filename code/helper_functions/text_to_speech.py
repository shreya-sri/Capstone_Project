# -*- coding: utf-8 -*-

from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from pydub import effects

def speak(mytext, language):
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
    #print(type(myobj))
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("output.mp3")


    return "output.mp3"


if __name__=='__main__':
        
    speech = speak("Welcome! Would you like to use our voice assistant?")
    song = AudioSegment.from_mp3(speech)
    song = effects.speedup(song, 1.2, 150, 25)
    play(song)





