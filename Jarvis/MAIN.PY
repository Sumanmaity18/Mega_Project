import speech_recognition as sr
import pyttsx3
import webbrowser
import music
import requests
import google.generativeai as genai

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi="your api key"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):

    genai.configure(api_key="your api key")
    model = genai.GenerativeModel("gemini-2.5-flash")
    response = model.generate_content(command)
    return response.text      

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r= requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={news api}")
        data = r.json()
        if data["status"] == "ok":
            print("Top Us headlines:\n")
            for i, article in enumerate(data["articles"]):
                speak(f"{i+1}.{article['title']}")
    else:
        output = aiProcess(c)
        speak(output) 

if __name__ == "__main__":
    speak("Hello my name is jarvis........")
    while True:
        r = sr.Recognizer()
        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=5, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "hello"):
                speak("ya")
                with sr.Microphone() as source:
                    print("jarvis Active..")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print("error; {0}".format(e))
