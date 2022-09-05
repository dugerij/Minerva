
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia


def assistant(audio):

    engine = pyttsx3.init()
    """
    
    """
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def greeting():
    assistant("Hello, I am Minerva. How may I assist you?")

def audio_input():
    """
    """
    audio_input = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening and Processing')
        audio_input.pause_threshold = 0.7
        audio = audio_input.listen(source)

        try:
            print('Understanding')
            phrase = audio_input.recognize_google(audio, language='en-us')
            print('you said: ', phrase)

        except Exception as exp:
            print(exp)
            print("Can you please repeat that")
            return "None"

        return phrase

def theTime():
    """
    """
    time=str(datetime.datetime.now())

    print(time)
    hour = time[11:13]
    int_hr = int(hour)
    if int_hr >= 12:
        int_hr = int_hr - 12
        min = time[14:16]
        int_min = int(min)
        if int_min > 30:
            min = str(60 - int_min)
            int_hr +=1
            hour = str(int_hr)
            assistant("The time is " + min + "minutes to " + hour + "pm")
        else:
            assistant("The time is " + hour + min + "pm")

    else:
        
        min = time[14:16]
        int_min = int(min)
        if int_min > 30:
            min = str(60 - int_min)
            int_hr +=1
            hour = str(int_hr)
            assistant("The time is " + min + "minutes to " + hour + "am")
        else:
            assistant("The time is " + hour + min + "am")

def theDay():
    """
    """
    day = datetime.datetime.today().weekday() + 1

    Day_dict = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday'
    }
    if day in Day_dict:
        weekday = Day_dict[day]

    print(weekday)

    assistant("It's " + weekday)

def core_():
    greeting()
    while True:
        phrase = audio_input().lower()
        if "open_medium" in phrase:
            assistant("Opening medium.com")
            webbrowser.open("www.medium.com")
            continue
        elif "what is your name" in phrase:
            assistant("I am Minerva. Your virtual assistant")
        elif "open_google" in phrase:
            assistant("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "what day is it" in phrase:
            theDay()
            continue
        elif "what is the time" in phrase:
            theTime()
            continue
        elif "from wikipedia" in phrase:
            assistant("checking wikipedia ")
            phrase = phrase.replace("wikipedia", "")
            result = wikipedia.summary(phrase, sentences =4)
            assistant("According to wikipedia")
            assistant(result)
            continue
        elif "that will be all" in phrase:
            assistant("Until next time, Have a good day.")
            exit()

if __name__ =='__main__':
    core_()

    
