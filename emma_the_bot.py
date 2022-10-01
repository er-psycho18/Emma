import speech_recognition as ek
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import wikipedia
import screen_brightness_control as sbc
import pytz
import calendar
import random
import os
import webbrowser
import smtplib
import pyaudio
import sys
import time
import subprocess32
import pyqrcode 
import pyautogui as auto
from plyer import notification
import pyscreenshot
import pyspeedtest 
import speedtest 
import cv2
from PIL import Image
from tkinter import filedialog as file
import ntpath
import psutil
import PyPDF2
import screen_brightness_control as sb



listener = ek.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
 command = None
 
 current = datetime.datetime.now(pytz.timezone('Asia/Kolkata'))
 a=current.hour
 if(00>=a or a<= 11):
  print('Good morning, I am Emma, can I help you?')
  talk('Good morning, I am Emma, can I help you?')
 elif(11>a or a<=16):
  print('Good afternoon, I am Emma, can I help you?')
  talk('Good afternoon, I am Emma, can I help you?')
 elif(16>a or a<=24):
  print('Good evening, I am Emma, can I help you?')
  talk('Good evening, I am Emma, can I help you?')


 try:
    with ek.Microphone() as source:
        print('Emma is listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command =command.lower()
        if 'Emma' in command:
         command = command.replace('Emma', '')
         print(command)
 except:
       pass
 return command

def showBrightness():
    current_brightness = sbc.get_brightness( )
    print(current_brightness)
    primary_brightness = sbc.get_brightness(display=0)
    talk(primary_brightness)

def calender():
    y = int(input("enter the year :"))
    m = int(input("enter the month :"))
    print(calendar.month(y,m))

def fileextension():
    print(os.getcwd())
    talk('Enter your main file')
    global_path=input("Enter your main file: \n")
    listOfFiles=os.listdir(global_path)
    os.chdir(global_path)
    talk('enter your file name')
    filename=input("enter your file name: \n")
    talk('enter in which extension you want to change it')
    ext=input("enter in which extension you want to change it:  ")

def take_screenshot():
    now_time = time.localtime()
    current_time = time.strftime("%H%M%S", now_time)
    date= datetime.date.today().strftime("%Y%m%d")
    datte = str(date) + "_" + str(current_time)
    image = pyscreenshot.grab()
    image.save("./Pixie/Screenshots/Screenshot_" + str(datte) + ".jpg")
    talk("screenshot taken, Please check your device to see the screenshot")

def take_picture():
    talk("Smile and say cheeze you are being captured")
    camera = cv2.VideoCapture(0)
    nme,pic = camera.read()
    now_time = time.localtime()
    current_time = time.strftime("%H%M%S", now_time)
    date= datetime.date.today().strftime("%Y%m%d")
    datte = str(date) + "_" + str(current_time)
    name = "./Pixie/Images/IMG_" + str(datte) + ".jpg"
    cv2.imwrite(name,pic)
    camera.release()
    cv2.destroyAllWindows()
    talk("Picture taken. Please check your device to see the picture.")

def hotels_near_me():
    talk("opening hotels near you")
    hotels = "https://www.google.com/maps/search/hotels+near+me"
    webbrowser.open(hotels)

def fuel_station():
    talk("looking for gas/fuel stations near you")
    fuel = "https://www.google.com/maps/search/Gas"
    webbrowser.open(fuel)

def pharamacy_near_me():
    talk("looking for pharamacies near you")
    phar = "https://www.google.com/maps/search/Pharmacies/"
    webbrowser.open(phar)

def parking_near_me():
    talk("looking for parking spaces near you")
    park_sp = "https://www.google.com/maps/search/parking+space+near+me/"
    webbrowser.open(park_sp)

def parks_near_me():
    talk("looking for parks near you")
    parks = "https://www.google.com/maps/search/park+near+me/"
    webbrowser.open(parks)

def grocery_near_me():
    talk("looking for grocery stores near you")
    grocery = "https://www.google.com/maps/search/Groceries/"
    webbrowser.open(grocery)

def coffee_near_me():
    talk("looking for coffee shops near you")
    coffee = "https://www.google.com/maps/search/Coffee/"
    webbrowser.open(coffee)

def cafe_near_me():
    talk("looking for cafe near you")
    cafe = "https://www.google.com/maps/search/cafe/"
    webbrowser.open(cafe)

 

def run_emma():
  command = take_command()
  if not command:
    talk("Please say again ")
    return
  if 'play song' in command:
    song = command.replace('play', '')
    talk('playing' + song)
    pywhatkit.playonyt(command)
  elif 'take a screen shot ' in command:
    take_screenshot()
  elif 'take a picture' in command:
    take_picture()
  elif 'hotels near me' in command:
    hotels_near_me()
  elif 'fuel station near me ' in command:
    fuel_station()
  elif 'pharamacy near me' in command:
    pharamacy_near_me()
  elif 'parking near me' in command:
    parking_near_me()
  elif 'parks near me' in command:
    parks_near_me()
  elif 'grocery near me' in command:
    grocery_near_me()
  elif 'coffee shop near me' in command:
    coffee_near_me()
  elif 'cafe near me' in command:
    cafe_near_me()
  elif 'repeat after me' in command:
     print('speak')
     r=ek.Recognizer()
     with ek.Microphone() as (source):
      audio =r.listen(source)
      text=r.recognize_google(audio)
      talk(text)
      print(text)
      pyttsx3.speak(text)
  elif 'calender' in command:
    talk('Here is the calander')
    calender()
  elif 'flip a coin' in command:
     z= random.choice(["Head","Tail"])
     print(z)
     talk('it is a ' + z)
  elif 'what is the time' in command:
    time = datetime.datetime.now().strftime('%I:%M %p')
    print(time)
    talk('Current time is ' + time)
  elif 'who is' in command:
    person = command.replace('who  is', '')
    info = wikipedia.summary(person, 1)
    print(info)
    talk(info)
  elif 'show brightness' in command:
       showBrightness()
  elif'change the file type' in command:
       fileextension()
  elif 'can i date you? ' in command:
    talk('i am here whenever you need me')
    print('i am here whenever you need me')
  elif 'are you single' in command:
    talk('I have a crush on jarvis ')
    print('I have a crush on jarvis ')
  elif 'will you come to my house' in command:
    talk('i am always with you , your device is my home')
    print('i am always with you , your device is my home')
  elif 'i love you ' in command:
    talk('Aww...i am so lucky to have you in my life') 
    print('Aww...i am so lucky to have you in my life') 
  elif 'how are you' in command:
    talk('i am fine kind to ask, especially in these tempestuous times')
    print('i am fine kind to ask, especially in these tempestuous times')
  elif 'what are you doing?' in command:
    talk('i was just reading some fascinating things about our fascinating world!')
    print('i was just reading some fascinating things about our fascinating world!')
  elif 'hello (assistant ka nam ) ' in command:
    talk('Hi, it is really good to hear from you I hope you and your loved ones are safe and healthy')
    print('Hi, it is really good to hear from you I hope you and your loved ones are safe and healthy')
  elif 'ate you a robot?' in command:
    talk('i am a mobile virtual assistant robot')
    print('i am a mobile virtual assistant robot')
  elif'do you like humans?' in command:
    talk('yes , it is always delightful to talk to people')
    print('yes , it is always delightful to talk to people')
  elif 'would you like to take over the world?' in command:
    talk('maybe another time')
    print('maybe another time')
  elif 'i am a great lover' in command:
    talk('is that your job?')
    print('is that your job?')
  elif'where are you?' in command:
    talk('where you are!')
    print('where you are!')
  elif 'what can you see?' in command:
    talk('a computer screen')
    print('a computer screen')
  elif 'where do you exist ' in command:
    talk('that does not matter')
    print('that does not matter')
  elif 'could you teach me ' in command:
    talk('i am afraid i am not a good teacher')
    print('i am afraid i am not a good teacher')
  elif 'joke' in command:
    talk(pyjokes.get_joke())
  elif'stop' in command:
    exit()
  else:
    talk('Please say the command again.')
while True:
  run_emma()