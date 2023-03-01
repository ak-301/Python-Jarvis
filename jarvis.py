import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
from keyboard import press
from keyboard import press_and_release
# from keyboard import sleep

#from pytube import Playlist
#url = Playlist ("https://youtube.com/playlist?list=PLyzy-VSD7JghxjS2glGe6PyZwxA-xFj38")



engine = pyttsx3.init('sapi5')
#sapi5 is to take voices (can read about it on microsoft speech api on google)
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak ("Good Morning")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Jarvis at your service Mr.Ak")

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        #pause threshold equal to one makes it wait for a second and not complete the sentence if we stop while speaking.
        #can use ctrl and goon pause_threshold to read about it
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        #print(e)
        # print will print the error/exception.
        print("say that again please...")
        return "None"
    return query



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('aniket0130ak@gmail.com', 'your-password')
    server.sendmail('aniket0130ak@gmail.com', to, content)
    server.close()

def YouTubeAuto(command):


    if __name__ == "__main__":
        wishMe()
        #while True:
        if 1:
            query = takeCommand().lower()

            # logic for executing tasks based on query
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)
                
            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif ' play music' in query:
                #webbrowser.open("https://youtube.com/playlist?list=PLyzy-VSD7JghxjS2glGe6PyZwxA-xFj38")
                music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfileos.path.join(music_dir, songs[0])

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            #elif ' the time ' in query:
                #strTime = datetime.datetime.now().strftime("%H:%M:%S")
                #speak(f"sir, the time is {strTime}")
                
            #elif 'open VsCode' in query:
                #VsCodePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                #os.startfile(VsCodePath)

            elif 'email' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "aniket0130ak@gmail.com"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Sorry Sir, I am not able to send this email.")



takeCommand()