# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:24:15 2021

@author: Pranav
"""

#pip install --upgrade google-cloud-texttospeech


#import simpleaudio as sa
#import mpg321
#import subprocess

#from playsound import playsound
#from pydub import AudioSegment

from gtts import gTTS

# This module is imported so that we can 
# play the converted audio
#import os

def speak(mytext):

    # The text that you want to convert to audio
    #mytext = 'succ ma pp!'
    
    # Language in which you want to convert
    language = 'en'
    
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)
    #print(type(myobj))
    
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save("output.mp3")

    # Playing the converted file
    #os.system("mpg321 output.mp3")
    
    #sound = AudioSegment.from_mp3("output.mp3")
    #sound.export("output.wav", format="wav")
    #import subprocess
    #subprocess.call(['ffmpeg', '-i', 'output.mp3',
     #               'output.wav'])

    return "output.mp3"


if __name__=='__main__':
    
    speech = speak('test audio')

    #playsound(speech)

    #wave_obj = sa.WaveObject.from_wave_file(speech)
    #play_obj = wave_obj.play()
    #play_obj.wait_done()


'''
import os
from google.cloud import texttospeech
from google.cloud import texttospeech_v1


os.environ['GOOGLE_APPLICATION_CREDENTIALS']="key.json"



def speak(text):
    # Instantiates a client
    client = texttospeech.TextToSpeechClient()
    
    
    # Set the text input to be synthesized
    synthesis_input = texttospeech.SynthesisInput(text=text)
    
    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.VoiceSelectionParams(
        language_code="en-IN", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
    )
    
    # Select the type of audio file you want returned
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16
    )
    
    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )
    
    #write audio to file
    with open("output.wav", "wb") as f:
        f.write(response.audio_content)
    

    return "output.wav"
    
    
'''



