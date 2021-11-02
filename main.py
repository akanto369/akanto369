from random import *
user_pass= input("Enter Your Password : ")
password = ["i","j","k","l","m","n","o","p","q","r","S","t","u","v","w","x","a","b","c","d","e","f","g","h","y","z"]
guess = ""
while(guess!=user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0,25)]
        guess= str(guess_letter)+str(guess_letter) + str(guess_letter) 
        print(guess)
print("This is your passwored ", guess)
