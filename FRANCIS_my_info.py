print('Hello! My name is Francis Nicole Lopez Raut') #this is my name and the whole sentence between the ' ' is a string type variable
age = 24 #here I put age as my variable and 24 as its definition. It should be an integer automatically. it's also my age :*
str(age) #I did this to convert my integer to string because you cannot concatenate integer to a string
print('I am ' + str(age) + ' years old') #showing you my age
print("My birthday is on August 24, 1998") #here I showed you that ' ' and " " are interchangeable in function. This is automatically a string.
decipoint = 6.9 #A float is technically a number with a decimal point. 3.0 is a float. 30 is an integer.
print( str(decipoint) + " is my favorite decimal number *wink wink* ") #it is important to leave a space especially if you want to put a variable in a str sentence. So I placed a space after my first " " here.
"""
This can
also be
considered as 
a comment
"""
answer = input("Is it raining today? Why don't you tell me then. (True/False) ") #I'm sorry I made the boolean part as a while loop sir HAHAHAHA thanks for the practice!
while answer != "True" and answer != "False": #I want to have these exact words as my choices. != is to denote that anything BUT this answer is for the code block below it.
    answer = input("I don't know what you mean. Say it again? (True/False) ")#This is because some users are stoooopid and will put ANYTHING that is not even in the choices.
if answer == "True": #If True comes out, the one below would show up.
    print("That's great for cuddles don't you think so ;) ")
else: #else if False, this one would
    print('Aw, time to hang my clothes again')
"""
Boolean is basically True or False sir. Thanks <3

"""
