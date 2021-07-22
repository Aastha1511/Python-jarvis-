def searchOnWiki(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)


def openInBrowser(query):
    pass


def getBattery(query):
    battery = psutil.sensors_battery()
    percentage = battery.percent
    speak(f"Maam the {percentage} of battery left")


def closeTheApp(query):
    exit()


ACTIONS = {
    'wikipedia': searchOnWiki,
    'open': openInBrowser,
    'time': getTime,
    'power battery': getBattery,
}


def action(query):
    if 'wikipedia' in query:
        searchhOnWiki(query)
    elif 'open' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Maam, the time is {strTime}")
    elif "how much power left" in query or "how much we have" in query or "battery" in query:
