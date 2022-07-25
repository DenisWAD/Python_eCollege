import random

num_guesses = 1
guessed_correctly = False

name = input("Hi there, let's play a game. What is your name?")
random_number = random.randint(1,10)
print(random_number)

while guessed_correctly == False:

    try :
        guess = int(input("What is your guess?"))
    except ValueError :
        print("Please only guess a number!")
    except :
        print("Something went wrong, please try again")
    else :
        print(guess)
        if random_number == guess :
            print(f"Yes!! You guessed the correct number! It was {random_number}")
            print(f"You guessed correctly in {num_guesses} attempts")
            guessed_correctly = True
        else :
            print("Please guess again!")
            num_guesses += 1

print("Thanks for playing, that was fun!")


    
