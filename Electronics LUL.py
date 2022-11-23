#Circuit Calculator

##multiplication
def multiplication(x,y):
    return x*y
##division
def division(x,y):
    return x/y

## Greeting Function
def welcome_message():
    """Greet and user verification"""
    while True:
        try:
            mess_1 = input("Welcome aboard matey! Let's do some calculating shiz shall we? ")
        except ValueError:
            print("You grazy or what? Type Yes/No stoopid. ")
            continue
        if mess_1.capitalize() == "Yes" :
            break
        elif mess_1.capitalize() == "No": 
            print("kekbye tnx for wasting my time u sad excuse of a man. ")
            exit()
        else:
            print("Try again u mofo. Yes/No only ")
            continue

## Variable confirm function
def confirm_variables():
    while True:
        try:
            confirm1 = input("Do you have the variables ready for me to compute? Yes/No ")
        except ValueError:
            print("You grazy or what? Type Yes/No stoopid. ")
            continue
        if confirm1.capitalize() == "Yes" :
            print("Great! Let's continue. ")
            break
        elif confirm1.capitalize() == "No": 
            print("kekbye just die. ")
            exit()
        else:
            print("Try again u dumbo. Yes/No only ")
            continue

### Start of my interface
print(welcome_message())
print("This is a simple calculator that helps you solve Voltage, Resistance and Current. ")
confirm_variables()

while True:
    print("That's great! Now let's see what you need: \n A. Voltage \n B. Resistance \n C. Current \n D. None ")
    choice = input("Select a letter. ")
    if choice.capitalize() in 'A' 'B' 'C' 'D':
        if choice.capitalize() == 'A' :
            print("As you wish, let's go with Voltage.")
            try:
                Resistance = float(input("Give me your resistance boi. "))
                Current = float(input("Now your Current. "))
                Voltage = float(multiplication(Resistance,Current))
                print(f"Here's your voltage boi. {Voltage}")
            except ValueError:
                print("You can't use math on words dumb bish. Use numbers la. ")
        elif choice.capitalize() == 'B' :
            print("As you wish, let's go with Resistance.")
            try:
                Voltage1 = float(input("Give me your Voltage boi. "))
                Current1 = float(input("Now your Current. "))
                Resistance1 = float(division(Voltage1,Current1))
                print(f"Here's your voltage boi. {Resistance1}")
            except ValueError:
                print("You can't use math on words dumb bish. Use numbers la. ")
        elif choice.capitalize() == 'C' :
            print("Current! Let's do it.")
            try:
                Voltage2 = float(input("Give me your Voltage boi. "))
                Resistance2 = float(input("Now your Current. "))
                Current2 = float(division(Voltage2,Resistance2))
                print(f"Here's your voltage boi. {Current2}")
            except ValueError:
                print("You can't use math on words dumb bish. Use numbers la. ")
        elif choice.capitalize() == 'D' :
            print("Stop wasting my time foo. Ciao.")
            exit()
    else:
        print("Not what I had in mind. Try again. A/B/C/D")
        break

print("Trial complete. Head to the next level with Stanford here. ( ͡° ͜ʖ ͡°) ")
print("Ciao ciao mi amigo. ")





### End of my interface

    







