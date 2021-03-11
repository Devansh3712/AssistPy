'''
Module for taking user voice input
and converting text to speech
'''

#Importing modules
try:
    import pyttsx3
    import speech_recognition as sr

except:
    print('Speech Recognition and TTS modules not setup')
    exit()

#Class for taking user voice input
class Listen:

    def speech_to_content():

        #Initializing Speech Recognition object
        obj = sr.Recognizer()

        with sr.Microphone() as source:

            try:
                audio     = obj.record(source, duration = 10)
                converted = obj.recognize_google(audio)
                return converted

            except:
                raise Exception('Error in Speech Recognition')

#Class for converting text to speech
class Speak:

    def __init__(self, content):
        self.content = content

    def text_to_speech(self):

        #Initialize Text to Speech object
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)

        try:
            #Convert the content to speech
            engine.say(self.content)
            engine.runAndWait()

        except:
            raise Exception('Error in Text to Speech')

'''
AssistPy
Devansh Singh, 2021
'''