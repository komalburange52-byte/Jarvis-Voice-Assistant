import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib


engine =pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voices',voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)  
    if hour>=0 and hour<12:
        speak("good morning!")

    elif hour>=12 and hour<18:
        speak("good aferenoon")
  
    else:
        speak("good evening")          
    
speak("i am jarvis mam.please tell me how may i help you")   

def takecommand():
    #it take microfone input from the user and returns strig output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")       
        r.pause_threshold=1
        audio=r.listen(source) 
        print("got it now recognizing")
    try:
        print("recognizing...")
        query=r.recognize_google(audio)
        print("i said",query)

    except Exception as e:
        print(e)
        print("say that again please...")
        return"none"    
    return query

def sendEmail(to,contact):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('komalburange52@gmail.com','komal@2005')
    server.sendEmail('raviburange52@gmail.com',to,contact)
    server.close()    
    


if __name__=="__main__":
  # speak("harry is a good boy")
   wishme()
   while True:
     query = takecommand().lower()

     if 'wikipedia' in query:
         speak('searching wikipedia...')
         query=query.replace("wikipedia","")
         results=wikipedia.summary(query,sentences =2)
         speak("according to wikipedia")
         print(results)
         speak(results)
    
     elif 'open youtube' in query:
         webbrowser.open("youtube.com")
   
     elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")

     elif 'open google' in query:
         webbrowser.open("google.com")    
    
     elif 'play music' in query:
         music_dir='D:\\Non critical\\songs\\favorite songs2'
         songs=os.listdir(music_dir)
         print(songs)
         os.startfile(os.path.join(music_dir,songs[0]))


     elif 'the time' in query:
         strTime=datetime.datetime.now().strftime("%h:%m:%s") 
         speak(f"sir the time is{strTime}")   

     elif 'open code' in query:
         codePath= "C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath)

     elif 'email to komal' in query:
         try:
             speak(("what should i take")) 
             contact=takecommand()
             to="komalburange52@gmail.com"
             sendEmail(to,contact) 
             speak("email has been send")

         except Exception as e:
             print(e)
             speak("sorry my freind komal ,i cant not able to send this email")
