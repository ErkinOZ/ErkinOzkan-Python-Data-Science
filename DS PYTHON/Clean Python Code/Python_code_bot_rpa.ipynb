import pandas as pd
import numpy as np
import pyttsx3

yes_responses = ['Yes', 'yes', 'agree', 'good', 'okay', 'ok', 'sure']
no_responses = ['no', 'No', 'don\'t need', 'no thanks', 'not now', 'busy', 'Occupied']
repeat_responses = ['repeat', 'can you repeat please', 'Again']

def hello_logic(name):
    if name:
        engine = pyttsx3.init()
        engine.say(f'Hello {name}, good day! This is company X, we are conducting a satisfaction survey regarding our services. Is it a good time to talk?')
        engine.runAndWait()
        response = input(f'Hello {name}, good day! This is company X, we are conducting a satisfaction survey regarding our services. Is it a good time to talk?')
        
        for i in yes_responses:
            if response == i:
                recommend_main(response)
        
        for j in no_responses:
            if response == j:
                hangup_wrong_time(response)
        
        for n in repeat_responses:
            if response == n:
                hangup_repeat(response)

def recommend_main(response):
    engine = pyttsx3.init()
    engine.say('Would you recommend our company to your friends? Please rate from 0 to 10, where 0 means you would not recommend and 10 means you would definitely recommend.')
    engine.runAndWait()
    rating = int(input('Would you recommend our company to your friends? Please rate from 0 to 10, where 0 means you would not recommend and 10 means you would definitely recommend.'))
    
    if rating <= 8:
        hangup_negative(rating)
    if rating == 9 or rating == 10:
        hangup_positive(rating)

def hangup_negative(rating):
    if rating:
        engine = pyttsx3.init()
        engine.say('I understand. Thank you for your time. All the best.')
        engine.runAndWait()
        print('I understand. Thank you for your time. All the best.')

def hangup_positive(rating):
    if rating:
        engine = pyttsx3.init()
        engine.say('Great! Thank you for your time. All the best!')
        engine.runAndWait()
        print('Great! Thank you for your time. All the best!')

def hangup_repeat(response):
    hello_logic(response)

def hangup_wrong_time(response):
    engine = pyttsx3.init()
    engine.say('Sorry for the inconvenience. All the best.')
    engine.runAndWait()
    print('Sorry for the inconvenience. All the best.')

while True:
    name = input('What is your name?: ')
    hello_logic(name)
    break
