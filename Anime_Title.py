print("Welcome to a very rated 18+ (if you allow it of course ho ho ho) Anime Title Generator!")
startbutton = input("To start of I need to see if you're stoopid or not. Type rEadY if you are ready. ")
while startbutton != "rEadY":
    startbutton = input("Oh you're so stooopid eh? Come on you can learn from it! Type rEadY now! ")
    while startbutton != "rEadY":
        print("Wow you're so stoopid bruhdah. Forda reals. Come back again when you can follow instructions. ")
        exit()

print("Excellent that you're not that stoopid eh? Go on <3.")

#Random Ass Japanese word
a = input('What is a random Japanese word you know of? ')

#Describe yourself in 1 adjective
b = input('How would you define yourself in one word? ')

#Girl or Boy, Sexually
c = input('Random Noun: ')

#magical creature
d = input("what's your favorite magical creature? ")

#random profession
e= input("Give me a random profession ")

#What would be your story setting?
f = input("Where would you like this to happen? ")

"""
Below is my practice for f string threads, string methods, delaying an effect of the code and of course probability. 
Thanks again kuya Din!

"""

import random
from threading import Timer

def loading(delay):
    print(f"{a}: My {b} self gets a {c} that has a {d} for a {e}! SCREW THIS {(f.upper())} !!!")
    if random.random() < 0.5:
        print(f"I don't know about you but that's a stupid ass name. Ciao!")
    else:
        print(f"That's a great title man! Great job!")

 
if __name__ == '__main__':
 
    delay = 5        # in 5 seconds
 
    print('It may take some time to make your long ass title. Chutto Mate!')
 
    # call loading() after 5 seconds
    t = Timer(delay, loading, [delay])
    t.start()
 
    print('Generating...')  