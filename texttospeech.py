import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('voice', voices[1].id)
def tts(string):
    engine.say(string)
    engine.runAndWait()

