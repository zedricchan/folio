import random
name = input("Hello! May I know your name? ")
print("Hello {}! Nice to meet you! ".format(name))
flag = True #checkpoint for while loop
while flag:
    thing = input("What happened? ")
    feeling = input("How are you feeling right now? ")
    if feeling == 'happy' or feeling == 'very good' or feeling == 'cant be better':
        print("Oh! I'm glad you're feeling this way!")
        elaborate = input("Would you share more about this joyful event? ")
        print("Oh wow! That must have been incredible!")
        flag = False
    elif feeling == 'sad' or feeling == 'i need help' or feeling == 'im not okay' or feeling == 'im not doing well':
        print("Aww...I'm sorry to hear that. ")
        elaborate = input("Would you tell me more about it? I'll listen. ")
        tell = input(("hmmm...I am just a robot after all...have you told someone about it?"))
        if tell == 'yes':
            print("Good, it's good to open up your problems with people!")
            flag = False
        else:
            print("Hmmm...maybe you should find someone to listen...you gotta let things out mate!")
            more = input(("But i'll listen for now. Would you share more about it? "))
            print("hmmm..i see..hey man I'm proud that you were willing to open up to me. ")
            print("You got this man I believe in you!" )
            flag = False
    elif feeling == 'nervous' or feeling == 'anxious':
        print("oooh! What are you nervous about? ")
        input()
        print("ahh...chill mate, it'll be alright! Take a deep breath! ")
        print("Hey man if you never try, you never know!")
        flag = False
    end = input(("Is there anything more you wanna talk about? "))
    if end.lower() == "no" or end.lower() == 'goodbye' or end.lower() == 'nah':
        print("Okayyy Goodbye!")
        flag = False
    elif end.lower() == 'yes' or end.lower() == 'yeah':
        print("I'm here to listen! ")
        flag = True


