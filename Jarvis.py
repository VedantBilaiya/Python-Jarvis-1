import pyttsx3
import speech_recognition as sr
import datetime
import os
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

# Text To Speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# Speech To Text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=1, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said: {query}")

    except Exception as e:
        speak("Say that again please")
        return "none"
    return query

# To wish according to the time
def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am jarvis sir, please tell me how may i help you?")


if __name__ == "__main__":
    WishMe()

    while True:
        query = takeCommand().lower()

        if 'open notepad' in query:
            nPath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(nPath)
            speak("Opening Notepad")

        if 'open vs code' in query:
            vPath = "C:\\Users\\parnika\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(nPath)
            speak("Opening Visual Studio Code")

        if 'open cmd' in query or 'open command prompt' in query:
            os.system('start cmd')
            speak("Opening Command Prompt")

        if 'open youtube' in query:
            webbrowser.open('www.youtube.com')
            speak("Opening YouTube")

        if 'open google' in query:
            webbrowser.open('www.google.com')
            speak("Opening Google")

        if 'open whatsapp' in query:
            webbrowser.open('www.whatsapp.com')
            speak("Opening Whatsapp")

        if 'open github' in query:
            webbrowser.open('www.github.com')
            speak("Opening GitHub")
        