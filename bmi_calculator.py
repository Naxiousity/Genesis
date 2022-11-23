#bmi calculator setup

# Greet user! Try to use \n in this line.

verify = input("G'day human! You're here to check your BMI status eh? Come on right in!\n Wait a minute, are you sure you're here for a BMI check? ")
while verify.capitalize() != "Yes":
    verify = input("Perhaps you've made a mistake. Try saying yes or no. ")
    while verify.capitalize() != "Yes":
        print("Get yo ass out of here foo. Try again later! ")
        exit()

#Let the user see what

unit = input("Would you like to use Metric (kg and cm) or English (lbs and in) in your units? ")
while unit.capitalize() != "Metric" and unit.capitalize() != "English":
    unit = input("I don't understand. Metric units or English units? ")

#this is me trying the while, try, except with continue and break

if unit == "Metric":
    while True:
        try:
            weight = int(input("Please put your weight here (kilogram): "))
        except ValueError:
            print("Sorry, I don't understand that. (Use numbers) ")
            continue
        if weight < 0:
            print("No negative numbers here kid. ")
            continue
        try:
            height = int(input("How tall are you? (cm) "))
        except ValueError:
            print("Sorry, I don't understand that. (Use numbers) ")
        if height < 0:
            print("No negative numbers here kid. ")
            continue
        else:
            break
    bmi = (weight)/(height**2)


if unit == "English":
    while True:
        try:
            weight = int(input("Please put your weight here (lbs): "))
        except ValueError:
            print("Sorry, I don't understand that. (Use numbers) ")
            continue
        if weight < 0:
            print("No negative numbers here kid. ")
            continue
        try:
            height = int(input("How tall are you? (in) "))
        except ValueError:
            print("Sorry, I don't understand that. (Use numbers) ")
        if height < 0:
            print("No negative numbers here kid. ")
            continue
        else:
            break
    bmi = (weight*703)/(height**2)

# For additional info in regards to the BMI scale.

type = input(f"This is your BMI: {bmi} \n \n Would you like to see what type you are? (Yes/No) ")
while type.capitalize() != "Yes" and type.capitalize() != "No":
    type = input("Are you sure about that? Just say Yes or No. ")
    while type.capitalize() != "Yes" and type.capitalize() != "No":
        print("Thank you for taking my BMI Calculator!")
        exit()

if type.capitalize() == "Yes":
    if bmi < 18.5:
        print("You are underweight! Try to gain some weight okay? (Can't do something about your height sadly.)")
    elif 18.5 <= bmi <= 24.9: 
        print("Well done you're normal! Keep up the great work! Love ya! :* ")
    elif 25.0 <= bmi <= 29.9:
        print("Oh boy, a bit of stress eating much eh? You are overweight! Lay off the snacks and rehydrate once in a while <3 ")
    else:
        print("Good Lord almighty! You're obese my good human! Come and let's go to a gym eh.")