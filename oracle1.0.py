# an ai assistant to help you perform basic task
# contact me if have any surgesings, thank you world
import speech_recognition as sr
import pyttsx3
import datetime
import gtts
#from gtts import gTTS
import wikipedia
import webbrowser
import os
import time
import pyaudio
import subprocess
import ecapture as ec
import wolframalpha
import json
import requests
####################################################
print("loadin Oracle lol")
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices','voices[1].id')

def speak(text):
    engine.say(text)
    engine.runAndWait

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
      speak("good morning collins brown")
    elif hour>=12 and hour<18:
      speak("good afternoon collins brown")
    else:
        speak("good evening collins brown")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone(device_index=None) as source:
        print("listening...")
  #      r.pause_threshold=1496.57047568
        r.pause_threshold = 1
        audio_data=r.listen(source,timeout=6, phrase_time_limit=5)
        engine.runAndWait()
        try:
            statement=r.recognize_sphinx(audio_data)
            print(f"user said:{statement}\n")
            engine.runAndWait()
        except Exception as e:
              speak("i didnt hear you please try again") 
              engine.runAndWait()     
              return "none"
              
        return statement
speak("my name is oracle. an artificial consciousness")
wishMe()      


if __name__=='__main__':
    while True:
        speak("what can i do for you")
        statement=takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or"ok bye" in statement or "turn off" in statement:
            speak("see you later")
            break

        if 'wikipedia' in statement:
            speak('searching the wikipedia')
            statement=statement.replace("wikipedia ","")
            result=wikipedia.summary(statement,sentences=3)
            speak("according to the wikipedia")
            speak(result)
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube is noe opened")
            time.sleep(3)
        elif "open email" in statement:
            webbrowser.open_new_tab("https://email.com")
            speak("email is noe opened")
            time.sleep(3)
        elif "open youtube" in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube is noe opened")
            time.sleep(3)
        if 'what is' in statement or "the mean of"in statement or "explain the mean of"in statement:
            speak('searching the wikipedia')
            statement=statement.replace("wikipedia ","")
            result=wikipedia.summary(statement,sentences=3)
            speak("according to the wikipedia")
            speak(result)



