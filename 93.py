import random

number = random.randint(1, 10)
chances = 5

while chances > 0:
    print(f"You have {chances} chances left")
    guess = input("Guess the number : ")

    try :
        guess = int(guess)
        if 0 < guess < 11:
            if guess == number:
                print("You won! 😎🎉")
                break
            elif guess > number:
                print(f"Try smaller than {guess}")
            else:
                print(f"Try bigger than {guess}")
            chances -= 1
        else:
            print("Entry must be between 1-10")
    except ValueError:
        print("Entry must be an integer")
else:
    print(f"Game over! The number was {number} 😂👍")
