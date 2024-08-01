import random

def guess_number(number):
    random_number = random.randint(1, number)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess the number between 1 and {number}\n"))
        if guess < random_number:
            print(" guessed number is low ")
        if guess > random_number:
            print(" guessed number is high ")
    print(" Yes you guessed correct number ")

#guess_number(10)

def computer_guess(number):
    feedback = False
    while feedback == False:
        guess_number = random.randint(1, number)
        print(f" guessed number is {guess_number}")
        feedback = bool(int(input(" \n Is it correct? ")))
        
    print(" Yes You guessed correct number ")

#computer_guess(10)

def computer_guess1(number):
    low = 1
    high = number
    feedback = ""
    while feedback != "c":
        guess_number = random.randint(low, high)
        print(f" guessed number is {guess_number} \n")
        feedback = input(f" guessed number is high or low or correct ".lower())
        if feedback == "h":
            high = guess_number - 1
        elif feedback == "l":
            low = guess_number + 1

    print(" guessed number is correct ")
computer_guess1(10)