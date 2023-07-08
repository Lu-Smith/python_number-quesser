import random

top_of_range = input("Type a number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a nunber larger than 0 next time.")
        quit()

else:
    print("Next time, please type a number.")
    quit()

random_number = random.randint(0, top_of_range)

while True:
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess <= 0:
            print("Please type a number larger than 0.")
            quit()
    else:
        print("Please write a number next time.")
        quit()
    
    if user_guess == random_number:
        print("You got it!")
    else:
        print("You got it wrong. Please, try again.")
    break