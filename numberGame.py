import random 

print("Welcome! to the Number Guessing Game")
print("I would be choosing a number between 1 and 100 and You have to guess it")
# diff = ""
def askDifficulty():
    print("Select the difficulty level You wish to play in \n 1. Easy \n 2. Medium \n 3. Hard")
    diff = int(input("Please enter the difficulty"))
    return diff
Diff = askDifficulty()
match Diff:
    case 1:
        Diff = "Easy"
        attempt = 6
    case 2:
        Diff = "Medium"
        attempt = 5
    case 3:
        Diff = "Hard"
        attempt = 3
    case _:
        print("restart and choose a valid difficulty using the numbers 1 or 2 or 3")
        exit()

print(f"you have selected {Diff}, you have {attempt} attempts")
print("I have now chosen a number, Please start guessing")
number = random.randrange(1, 100)
c = 0
guessed = False
while c != attempt:
    guess = int(input())
    c += 1
    if guess == number:
        print(f"Congratulations!! You have guessed the number in {c} attempts")
        guessed = True
        break
    else:
        if guess > number:
            print(f"{guess} is too high")
        elif guess < number:
            print(f"{guess} is too low")

if not guessed:
    print(f"Better luck Next time!!!! The number was {number}")

input("/n Press enter to exit.....")
