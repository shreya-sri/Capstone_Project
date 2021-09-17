# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:24:15 2021

@author: Pranav
"""

#pip install --upgrade google-cloud-texttospeech

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
    
    #play
    #playsound("output.mp3")

    return "output.wav"
    
    

#speak("test audio")







'''
# Instantiates a client
client = texttospeech.TextToSpeechClient()


# Set the text input to be synthesized
synthesis_input = texttospeech.SynthesisInput(text="please")

# Build the voice request, select the language code ("en-US") and the ssml
# voice gender ("neutral")
voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", ssml_gender=texttospeech.SsmlVoiceGender.NEUTRAL
)

# Select the type of audio file you want returned
audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.MP3
)

# Perform the text-to-speech request on the text input with the selected
# voice parameters and audio file type
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)



# The response's audio_content is binary.
with open("output.mp3", "wb") as out:
    # Write the response to the output file.
    out.write(response.audio_content)
    print('Audio content written to file "output.mp3"')

'''


