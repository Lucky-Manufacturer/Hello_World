rn = 7

while True:
    guess = int(input("Guess the number! "))

    if guess < rn:
        print("Too low! ")
    elif guess > rn:
        print("Too high! ")
    else:
        print("You're Correct! ")
