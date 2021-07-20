import datetime
import webbrowser
import psutil
import pyttsx3
import speech_recognition as sr
import wikipedia
import user_info

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    moment = ""
    if hour >= 0 and hour < 12:
        moment = "morning"
    elif hour >= 12 and hour < 18:
        moment = "afternoon"
    else:
        moment = "evening"
    speak(f"Good {moment} {USER['name']}")
    speak("I am your assistant. Please tell me what to do")


def takeCommand():
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
        print("Say that again please...")
        return "None"
    return query

def createNewUser():
    user = {
        "name":"",
        "dob":"",
        "gender":"",
    }
    for key in user.keys():
        while(True):
            speak(f"Please share your good {key}")
            value =  takeCommand().lower()
            speak(f"Please confirm your name is {key}")
            res = takeCommand().lower()
            if 'yes' in res:
                user[key] = value
                break
    user_info.createNewUser(user)
    return user

def validateUser():
    user = user_info.getUser()
    global USER
    if(user):
      
       USER = user
    else:
        USER = createNewUser()

if __name__ == "__main__":
    validateUser()
    wishMe()
    while True:
        query = takeCommand().lower()

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

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Maam, the time is {strTime}")
        elif "how much power left" in query or "how much we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Maam the {percentage} of battery left")
