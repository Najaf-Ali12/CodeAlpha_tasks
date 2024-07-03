import speech_recognition as sr
#import pyaudio
import datetime
import pyttsx3
import os
import webbrowser
engine=pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def Speak(audiovoice):
    #engine.say( "How are you ,AI engineer Najaf Ali Alkhani?")
    print(audiovoice)
    engine.say(audiovoice)
    engine.runAndWait()
def greet():
    hour=int(datetime.datetime.now().time().hour)
    if hour>=5 and hour<=10:
         Speak("Good Morning Sir ")
    elif hour>10 and hour<16:
         Speak("Good Afternoon Sir")
    elif hour>=16 and hour<=19:
         Speak("Good Evening Sir")
    else:
         Speak("Good Night Sir")
    Speak("Iam your Personal Assistant")    
def askinfo():
    Speak("What is your name Sir?")
    name=Take_Voice_Command()
    Speak("Welcome"+name)
    Speak("How can i serve you Sir")
def Take_Voice_Command():
    r=sr.Recognizer()
    text=""
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold=0.5
        try:
            audio=r.listen(source,timeout=5,phrase_time_limit=1)
            print("Undestanding your voice please wait....")
            text=r.recognize_google(audio,language='en-in')                                 #i forcely used recognize_google() it was google_cloud
            print(text)
        except Exception as e:
            Speak("Sir! I cannot Understand what you are saying,Sorry!")
        return  text
##cmd=input("Enter what you want to listen from the robot:")
##Speak(cmd)
if __name__=="__main__":
    greet()
    askinfo()
    work=Take_Voice_Command().lower()
    while True:
        if "how are you" in work:
            Speak("Iam fine Alhumdulilah .Thanks alot")
            Speak("And what about you sir")
        elif "fine" in work or "good" in work or "Iam fine" in work or "Alhumdulilah"  in work:
            Speak("It is good to know that you are fine")
        elif "not well" in work or "ill" in work or"sick" in work or "iam not well" in work or "iam not feeling well" in work:
            Speak("Sorry to hear that you are not well, May Allah protect you from every harm")  
        elif "I love you" in work or "love you" in work: 
            Speak("OH MY GOD! I love you too")
        elif "open Youtube" in work:
            link="https://www.youtube.com"
            os.startfile(link)
        elif "open Google" in work:
            link="https://www.google.com/"
            os.startfile(link)
        elif "open Google Classroom" in work:
            link="https://classroom.google.com/"
            os.startfile(link)
        elif "open notepad" in work:                    #correct way to open an app installed on pc told by youtuber
            path="c:\\windows\\system32\\notepad.exe"
            os.startfile(path)
        elif "close notepad" in work:
            os.system("TASKKILL /F /IM notepad.exe")
        elif "open Chrome" in work or "open google chrome" in work:
            url="www.britannica.com"                                        #correct way to open a browser told by youtuber
            chrome_path="C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
            webbrowser.get(chrome_path).open(url)
        elif "close chrome" in work:    
            os.system("TASKKILL /F /IM chrome.exe")
        elif "bye"in work or "good bye" in work:
            Speak("See you soon")
            exit()
        elif "shut down" in work or "shut down my laptop" in work or "shut down laptop" in work:
            os.system("shutdown /s /t 0")
        elif "restart" in work or "restart my laptop" in work or "restart laptop" in work:
            os.system("shutdown /r /t 0")
        else:
            Speak("I can't understand, Would you mind Speak again!")