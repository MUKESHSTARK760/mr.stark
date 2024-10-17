from tkinter import font
import webbrowser as wb
import speech_recognition as sr
import pyttsx3

def main1():
     r=sr.Recognizer()
     with sr.Microphone() as source:
        print("say something....")
        audio=r.listen(source)
    try:
      print("Reconizing Now...")