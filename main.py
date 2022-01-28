import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

# print("Initializing Jarvis...")

MASTER = "Jaden"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

#Speak function will pronounce the string put into it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# This function will wish you per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>= 0 and hour<12:
        speak("Good Morning " + MASTER)

    elif hour>= 12 and hour<18:
        speak("Good Afternoon " + MASTER)

    else:
        speak("Good Evening " + MASTER)

    speak("How may I help you?")
    # speak("I am Jarvis. How may I help you?")

# This function will take command from the microphone
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print("Say that again please")
        query = None

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('jadenhutchinson29@gmail.com', 'Bboy@thepiano10')
    server.sendmail('michealbeethoven@gmail.com', to, content)
    server.close()
    
#Main program starts here
# speak("Initializing Jarvis...")
wishMe()
query = takeCommand()
 
# Logic for executing Tasks as per the query
if 'wikipedia' in query.lower():
    speak('Searching wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences =2)
    speak(results)
    print(results)

elif 'open youtube' in query.lower():
    url = 'youtube.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open google' in query.lower():
    url = 'google.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open facebook' in query.lower():
    url = 'facebook.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open twitter' in query.lower():
    url = 'twitter.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'open instagram' in query.lower():
    url = 'instagram.com'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)

elif 'play music' in query.lower():
    songs_dir = "C:\\Users\\Jadenhutchinson\\Music\\PLAYLIST1"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[0]))

elif 'play another one bites the dust' in query.lower():
    songs_dir = "C:\\Users\\Jadenhutchinson\\Music\\PLAYLIST1"
    songs = os.listdir(songs_dir)
    print(songs)
    os.startfile(os.path.join(songs_dir, songs[2]))

elif 'the time' in query.lower():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"{MASTER} the time is {strTime}")
    print(strTime)

elif 'open code' in query.lower():
    codePath = "C:\\Users\\Jadenhutchinson\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codePath)

elif 'email Jordan' in query.lower():
    try:
        speak("What should I send...")
        content = takeCommand()
        to = "michealbeethoven@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent successfully")

    except Exception as e:
        print(e)
        
    