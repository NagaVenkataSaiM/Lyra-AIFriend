import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import subprocess
import wolframalpha
import json
import requests
import tkinter as tk
from tkinter import filedialog
from facial_recog  import recog
from youtube import youtube_search_location

engine=pyttsx3.init('espeak')
voices=engine.getProperty('voices')
engine.setProperty('voice','en+f5')
engine.setProperty('rate',175)
username=os.getlogin()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello"+username+"Good Morning")
        print("Hello",username,"Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello"+username+"Good Afternoon")
        print("Hello",username,"Good Afternoon")
    else:
        speak("Hello"+username+"Good Evening")
        print("Hello",username,"Good Evening")

def takeCommand():
    sr.dynamic_energy_threshold = False
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source, phrase_time_limit=5)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")

        except Exception as e:
            speak("Pardon me,please say that again")
            return "None"
        return statement

print("Loading Lyra....")
speak("Loading Lyra")
wishMe()

if __name__=='__main__':




    while True:
        speak("How can I help you?")
        statement=takeCommand().lower()
        if statement==0:
            continue
        if "lyra" in statement:
            if "good bye" in statement or "ok bye" in statement or "stop" in statement:
                speak("lyra is shutting down,Good bye")
                print("lyra is shutting down,Good bye")
                break
            if 'about' in statement:
                speak("searching wikipedia...")
                statement=statement.replace("about","")
                results=wikipedia.summary(statement,sentences=3)
                speak("According to wikipedia")
                print(results)
                speak(results)
            elif 'youtube' in statement:
                youtubeinput=input("what can i play?")
                youtubevid_id=youtube_search_location(youtubeinput,max_results=1)
                webbrowser.open_new_tab("https://www.youtube.com/watch?v="+youtubevid_id)
                speak("youtube is open now")
                time.sleep(5)
            elif 'open google' in statement:
                webbrowser.open_new_tab("https://www.google.com")
                speak("google is open noe")
                time.sleep(5)
            elif 'open spotify' in statement:
                webbrowser.open_new_tab("https://open.spotify.com")
            elif 'show image' in statement:
                root = tk.Tk() 
                root.withdraw() 
                file_path = filedialog.askopenfilename()
                print(file_path)
                recog(file_path)
            elif 'shutdown' in statement:
                os.system("shutdown now -h")

