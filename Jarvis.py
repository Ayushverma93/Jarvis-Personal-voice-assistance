# convert text to speach.
import pyttsx3
#  
import speech_recognition as sr
#
import webbrowser
#
import datetime
#
import pyjokes

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        #  Remove unwanted noise
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Not Understand")
            
def speechtx(x):
        engine = pyttsx3.init()
        # Get the property form engine and for voices
        voices = engine.getProperty('voices')
        # Set voice of male.(voice[0],id).
        engine.setProperty('voice',voices[0].id)
        # rate is used for set the speed of voices.
        rate = engine.getProperty('rate')
        engine.setProperty('rate',120)
        # say is used for speak the text value.
        engine.say(x)
        engine.runAndWait()
        
if __name__ == '__main__':
     
    # if sptext().lower() == "hey peter" :
        data1=sptext().lower() 
        
        if "your name" in data1:
            name = "my name is Ayush"
            speechtx(name)
            
        elif "old are you" in data1:
            age = "i am two years old"
            speechtx(age)
            
        elif 'time' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
            
        elif 'youtube' in data1:
            webbrowser.open("https://www.youtube.com/")
            
        elif "joke" in data1:
            joke_1 = pyjokes.get_joke(language="en",category="neutral")
            print(joke_1)
            speechtx(joke_1)   
        
        elif "music" in data1:
            webbrowser.open("https://www.youtube.com/watch?v=zRtPUIumXcY")
            
            
            
            
            
            
            
            
            
            
    # else:
        # print("thanks")