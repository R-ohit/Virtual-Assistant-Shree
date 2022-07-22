import datetime   
import os         
import random    
# import self as self  
import pyttsx3  
import cv2   
                    
                
import requests # IP Address    
                
import speech_recognition as sr 
                                
                            
import wikipedia    
                    
                    
import webbrowser   
                   
import sys       

from bs4 import BeautifulSoup     
import psutil  
# import cv2   
import speedtest

#  Engine used
engine = pyttsx3.init('sapi5')        

voices = engine.getProperty('voices') 
                                      
engine.setProperty('voice', voices[1].id)
                                        


#  To speak written text
def speak(audio):       
    engine.say(audio)
    engine.runAndWait()
    pass


# this function helps to take command from user
def takecommand():
    r = sr.Recognizer()  

    with sr.Microphone() as source: 
                                        
        print("Listening...")
        r.pause_threshold = 1   
        audio = r.listen(source, timeout=3, phrase_time_limit=10)  
                                

    try:  
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said : {query}\n")
        # print("You Said :", query)

    except Exception as e:       
    
        print("Please say it again...")
        return "none"               
    return query                     


def wishMe():                           
    hour = int(datetime.datetime.now().hour)                                               #
    min = int(datetime.datetime.now().minute)
    sec = int(datetime.datetime.now().second)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir")
    else:
        speak("Good Evening Sir")
    print(f"I am Shree Sir,"
          f"it's {hour} {min}")
    speak(f"I am Shree Sir,"
          f"it's {hour} {min}, Please tell me how i help you?")
def news():
    url = 'https://newsapi.org/v2/top-headlines?country=in&apiKey=b145a812d3fa4123b43baa3b49e75e15'
    main_page = requests.get(url).json()
    articles = main_page["articles"]

    head = []
    day = ["first", "second"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[1]} news is {head[1]}")


def TaskExecution():   
    speak("This is Shree, Your Assistant")
    wishMe()
    while True:

        query = takecommand().lower()   


        # logics for executing tasks, based on queries 
 
        # opening cmd prompt and notepad.
        if "open notepad" in query:  
            speak("please wait SAM while I am opening Notepad")
            path = "C:\\Windows\\System32\\notepad.exe"
            os.startfile(path)    

        elif "open command prompt" in query:
            speak("please wait SAM while I am opening Command Prompt")
            os.system("start cmd")          

        # to play music
        elif "play music" in query:             # 2nd feature
            music_dir = "D:\FALTU MUSIC"         
            songs = os.listdir(music_dir)       
                                       
            rd = random.choice(songs)        

            os.startfile(os.path.join(music_dir, rd))  
            '''for song in songs:
                 if song.endswith('.mp3'):
                      os.startfile(os.path.join(music_dir, song))'''

        # Searh ________ (anything) in wikipedia
        elif 'wikipedia' in query:  # 3rd feature
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")           

            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia.")
            # print(results)
            speak(results)

        # for opening websites (only google and youtube for now)
        elif 'open youtube' in query:  # 4th feature
            webbrowser.open("youtube.com")  
        elif 'open google' in query:
            webbrowser.open("google.com")

        # Basic Conversations                                # 5th feature
        elif "your name" in query:
            speak("My name is Shreee and How about you?") # speak funtion from sapi5(engine)
        # elif "hello" in query:
        #   speak("Hello sir may I help you")
        elif "how are you" in query:
            speak("I am fine sir what about you.")
        elif "also good" in query:
            speak("That's great to hear from you.")
        elif "thank you" in query:
            speak("It's my Pleasure sir")
        elif 'time' in query:  
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, the time is {strTime}, please follow your schedule")
            speak(f"Sir, the time is {strTime}, please follow your schedule")

        # to show ip address
        elif "ip address" in query:  # 6th feature
            ip = requests.get('https://api.ipify.org').text 

            speak(f"your IP address is {ip}")
            print(f"your IP address is {ip}")

        elif 'weather' in query:
            speak("Please wait sir, i am justifying weather conditions...")
            search = query
            # print(query)
            url2 = f"https://www.google.com/search?q={search}"
            r = requests.get(url2)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_='BNeawe').text
            speak(f"current {search} is {temp}")

        # Show battery of our laptop or computer
        elif "power" in query or "battery" in query:
            battery = psutil.sensors_battery() 
            p = battery.percent
            print(f"sir our system have {p} percent battery")
            speak(f"sir our system have {p} percent battery")
            if p>=75:
                speak("we have enough power to continue our work")
            elif p>=40 and p<=75:
                speak("we have enough power to continue our work, we should connect charger")
            elif p<=15 and p<40:
                speak("we don't have enough power to work, connect charger")
            elif p<=15:
                speak("we have very low power, please connect charging, the system will shutdown very soon.")


            elif "camera" or "webcam" in query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()




        elif "internet speed" in query:
                speak("please wait... sir i am determinig internet connectivity and its speeeed.")

                st = speedtest.speedtest()
                dl = st.download()
                up = st.upload()
                print(dl, "bits per second", up, "bits per second")
                speak(f"our downloading speed is {dl} bits per second...... "
                  f"and uploadig speed is {up} bits per second ThankYou")

        elif "sleep" or "no thanks" in query:
            speak("ok sir, I am going to sleep now, you can call me anytime.")
            break  # sys.exit()
 

if __name__ == "__main__":
    # TaskExecution()
    # wishMe()
    while True:
        permission = takecommand() 
        if "wake up" in permission: 
            
            TaskExecution()
        elif "goodbye" in permission:
            speak("thanks for using me.")
            sys.exit()  