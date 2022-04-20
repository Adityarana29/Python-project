import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Jarvis Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = takeCommand()
            results = wikipedia.summary(query, sentences=3)  #Done
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:         #Done
            webbrowser.open("youtube.com")

        elif 'open google' in query:          #Done
            webbrowser.open("google.com")

        elif 'open stack overflow' in query:   #Done
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir =r'C:\Users\Dell\Music\Song'
            songs = os.listdir(music_dir)   #DONE
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'play movie' in query:
            movie_dir =r'D:\Users\Dell\Videos\MOVIES\Anime\Beautiful Movie'
            movies = os.listdir(movie_dir)
            print(movies)    
            os.startfile(os.path.join(movie_dir, movies[0]))       #Done

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")
            print(strtime)           #Done

        elif 'open code' in query:
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
