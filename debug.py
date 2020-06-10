import random

msg = "Hello Worldf"

# practice writing if else
# if msg == "Hello World":
#   print(msg)
# else:
#   print("I don't know the message")

# # I made a function
# def friendlyMsg(name):
#   return f'Hello, {name}! Have a great day!'

# print(friendlyMsg("james").upper())
# print(friendlyMsg("clayton"))


# accepting user input
print("What's your name")
name = str(input())

# Random Number Guessing Game
rand = random.randint(1, 10)
print(f"Alright {name}, Guess a number between 1 and 10")
x = 0
while x < 3:
    numberGuessed = int(input())
    if numberGuessed == rand:
        print(f"YOU GOT IT. THE NUMBAH WAS {rand}")
        break
    elif numberGuessed < rand:
        print(f"Guess a higher number than {numberGuessed}")
        x += 1
    elif numberGuessed > rand:
        print(f"guess a lower number {numberGuessed}")
        x += 1

if x == 3:
    print("You've lost!")
