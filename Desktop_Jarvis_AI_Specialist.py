import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import time
import smtplib
import subprocess
import json
import requests
import wolframalpha
import psutil
import sys
import pyjokes
import pyautogui
from sys import platform
import getpass


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Preetha!")
    elif hour >= 12 and hour < 15:
        speak("Good afternoon Preetha!")
    else:
        speak("Good Evening Preetha!")

    speak("Please tell me how may I help you?!")


def screenshot():
    img = pyautogui.screenshot()
    img.save('path of folder you want to save/screenshot.png')


def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)

    battery = psutil.sensors_battery()
    speak("battery is at")
    speak(battery.percent)


def joke():
    for i in range(5):
        speak(pyjokes.get_jokes()[i])


def takeCommand():
    ''' This will take microphone input from the user and returns string output '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"

    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-emailiD', 'YourPasword')
    server.sendmail('your-emailID', to, content)
    server.close()


speak("LOADING YOUR PERSONAL AI ASSISTANT JARVIS!")
wishMe()
if __name__ == '__main__':
    if platform == "linux" or platform == "linux2":
        chrome_path = '/usr/bin/google-chrome'

    elif platform == "darwin":
        chrome_path = 'open -a /Applications/Google\ Chrome.app'

    elif platform == "win32":
        chrome_path = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'
    else:
        print('Unsupported OS')
        exit(1)

    # wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'voice' in query:
            if 'female' in query:
                engine.setProperty('voice', voices[1].id)
            else:
                engine.setProperty('voice', voices[0].id)
            speak("Hello Sir, I have switched my voice. How is it?")

        elif 'jarvis are you there' in query:
            speak("Yes Mam, at your service")

        elif 'cpu' in query:
            cpu()

        elif 'joke' in query:
            joke()

        elif 'screenshot' in query:
            speak("taking screenshot")
            screenshot()

        elif 'your name' in query:
            speak('My name is JARVIS')
        elif 'stands for' in query:
            speak('J.A.R.V.I.S stands for JUST A RATHER VERY INTELLIGENT SYSTEM')

        elif 'shutdown' in query:
            if platform == "win32":
                os.system('shutdown /p /f')
            elif platform == "linux" or platform == "linux2" or "darwin":
                os.system('poweroff')

        elif 'remember that' in query:
            speak("what should i remember sir")
            rememberMessage = takeCommand()
            speak("you said me to remember"+rememberMessage)
            remember = open('data.txt', 'w')
            remember.write(rememberMessage)
            remember.close()

        elif 'do you remember anything' in query:
            remember = open('data.txt', 'r')
            speak("you said me to remember that" + remember.read())

        elif 'sleep' in query:
            sys.exit()

        elif "good bye" in query or "ok bye" in query or "stop" in query:
            speak("JARVIS is shutting down.. Good bye")
            print("JARVIS is shutting down.. Good bye")
            break

        elif "open YouTube" in query:
            webbrowser.open_new("https://www.youtube.com")
            time.sleep(5)

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
            time.sleep(5)

        elif 'open stackoverflow' in query:
            webbrowser.open("https://stackoverflow.com")
            time.sleep(5)

        elif 'play music' in query:
            music_dir = 'C:\Music\MyMusic'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, The time is{strTime}")

        elif "open visual studio code" in query:
            speak("Opening your visual studio code Preetha")
            codePath = "C:\\Users\\cprit\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open Gmail" in query:
            speak("Opening your gmail Ashish")
            webbrowser.open_new_tab("https://www.gmail.com")
            time.sleep(5)

        elif "send email to myself" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "your-emialID-here"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry. Iam not able to send this Email.")

        elif "Weather" in query:
            api_key = '8ef61edcf1c576d65d836254e11ea420'
            base_url = 'https://api.openweathermap.org/data/2.5/weather?'
            speak("What is the city name?")
            city_name = takeCommand()
            complete_url = base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("the temperature in kelvin units is " + str(current_temperature) + "\nhumidity in percentage is" +
                      str(current_humidity)+"\n weather descripton" + str(weather_description))
                print("the temperature in kelvin units is " + str(current_temperature) + "\nhumidity in percentage is" +
                      str(current_humidity)+"\n weather descripton" + str(weather_description))
            else:
                speak("city not found")
                print("city not found")

        elif "who are you" in query or "what can you do" in query:
            speak("Iam JARVIS version 1 point 0 your personal assistant. I can perform the following task like opening YouTube, Gmail, Google chrome and stack overflow. Also, I can Predict current time, take a photo, search Wikipedia to abstract required data, predict weather in different cities, get top headline news from Times of India and can answer computational and geographical questions too.")

        elif "news" in query:
            news = webbrowser.open_new_tab(
                "https://timesofindia.indiatimes.com/home/headlines")
            speak("Here are some headlines from times of India for you - Happy Reading")
            time.sleep(7)

        elif "search" in query:
            query = query.replace("search", " ")
            webbrowser.open_new_tab("statement")
            time.sleep(5)

        elif "ask" in query:
            speak("My versions are still under upgradation progress to enable more cool features. But you can try asking me computational and geographical questions now. Sure, I will answer those. What do you want to ask?")
            question = takeCommand()
            app_id = "R2K75H-7ELALHR35X"
            client = wolframalpha.Clent('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)

       


time.sleep(3)
