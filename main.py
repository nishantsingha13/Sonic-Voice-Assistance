import os
import smtplib
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import  wikipedia


engine = pyttsx3.init('sapi5')  # Windows API to fetch the inbuilt voice of Windows
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()  # Run speech and wait for another

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir, Please tell me how may I help you")

def takecommand():
    # It takes microphone input from the user, converts it into a string, and gives output

    r = sr.Recognizer()  # Corrected: Initialize the recognizer class
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Pause after each statement
        r.energy_threshold=100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognize what you said using Google
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again, please...")
        return "None"
    return query
def sendEmail(to,content):#smtplib
    server=smtplib.SMTP("smntp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("nishantsinghal43@gmail.com")
    server.sendmail("nishantsinghal43@gmail.com",to,content)

if __name__ == "__main__":
    wishme()
    while True:
         query=takecommand().lower()

         #logic for executing the tasks based on query
         if 'wikipedia' in query:
            speak("searching Wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

         elif 'open youtube' in query:
             webbrowser.open("youtube.com")
         elif 'open google' in query:
             webbrowser.open("google.com")
         elif 'open github' in query:
             webbrowser.open("github.com")
         elif 'open compiler' in query:
             webbrowser.open("https://www.programiz.com/cpp-programming/online-compiler/")

         #elif 'play music' in query:
             #music_dir=''
             #songs=os.listdir(music_dir)
             #print(songs)
             #os.startfile(os.path.join(music_dir,songs[0]))
         elif 'the time' in query:
             strTime=datetime.datetime.now().strftime("%H:%M:%S")
             speak(f"Sir,the time is {strTime}")
         elif 'thanks' in query or 'thank you' in query:  # Combined thanks queries
             speak("You're welcome, Sir")
         elif 'open charm' in query:
             codepath="C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2023.2.1.lnk"
             os.startfile(codepath)

         elif 'email to nishant' in query:
             try:
                 speak("what should I say?")
                 content=takecommand()
                 to="nishantsinghal43@gmail.com"
                 sendEmail(to,content)
                 speak("Email has been sent!")
             except Exception as e:
                 print(e)
                 speak("sorry sir.I am not able to send email at this time")