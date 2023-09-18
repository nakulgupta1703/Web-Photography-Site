import datetime
from re import T
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import webbrowser
from googletrans import Translator
import os
import pyjokes
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    #It defines a speak function that makes erza speak the command given to it.
    engine.say(audio)
    engine.runAndWait()

def wishme():
    #It greets the user according to the time.
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        print("Good Morning")
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        print("Good Afternoon")
        speak("Good Afternoon")
    else :
        print("Good Evening")
        speak("Good Evening")

    speak("I am Erza! How may i help you.")
    print("I am Erza! How may i help you.")

def takeCommand():
    # It take moicrophone input from the user and return string output.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... ")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recongnizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :\n{query}\n")
    except Exception as e:
        print("Please say that again...")

        return "None"
    return query


class Functions:
    query = ''
    def _init_(self):
            self.query = takeCommand().lower()

    def wiki(self):
        speak("Searching Wikipedia")
        self.query = self.query.replace("wikipedia","")
        try:
            results = wikipedia.summary(self.query,sentences =2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except Exception as e:
            speak("Not able to find")

    def websites(self):
        if 'youtube' in self.query:
            webbrowser.open('youtube.com')
        elif 'google' in self.query:
            webbrowser.open('google.com')
        elif 'gfg' in self.query:
            webbrowser.open('geeksforgeeks.org')

    def translate(self):
        self.query = self.query.replace("translate","")
        translator = Translator()
        out =translator.translate(self.query,src="en",dest="hi")
        print(out.text)

    def date_time(self):
        str_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f" the time is {str_time}")

    def spotify(self):
        dcpath = "C:\\Users\\shubh\\AppData\\Roaming\\Spotify\\Spotify.exe"
        speak("Opening spotify.")
        os.startfile(dcpath)

    def jokes(self):
        joke = pyjokes.get_joke()
        speak(joke)



if _name_ =="_main_":
    wishme()
    while True: 
        obj = Functions()
        if 'wikipedia' in obj.query:
            obj.wiki()

        elif 'spotify' in obj.query:
            obj.spotify()

        elif 'open' in obj.query:
            obj.websites()

        elif 'translate' in obj.query:
            obj.translate()

        elif 'time' in obj.query:
            obj.date_time()

        elif 'joke' in obj.query:
            obj.jokes()

        elif 'quit' in obj.query:
            break
        