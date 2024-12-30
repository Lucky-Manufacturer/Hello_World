rn = 7 # the correct number. rn means "right number"

while True: # Starts an infinite loop. This will continue untill you get it correct
    guess = int(input("Guess the number! "))

    if guess < rn:
        print("Too low! ")
    elif guess > rn:
        print("Too high! ")
    else:
        print("You're Correct! ")
        break # Exit the loop when the guess os correct