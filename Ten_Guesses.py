answer = input("Player 1: Enter an object in lower-case letters. ")

print("\n" * 100)

print("Let's play ten guesses! ")
print("Each time you guess you can ask the other player a yes/no question out loud and then guess again! ")
print()
num_guess = 10

while num_guess > 0:
    guess = input("Player 2: What is your guess? ")

    if guess == answer:
        print("Congratulations! You got it!")
        break

    else:
        num_guess -= 1
        print("Incorrect guess. Ask the other player a yes/no question and try again.")

        if num_guess > 0:
            print("You have " + str(num_guess) + " guesses remaining. ")
            print()
            guess = input("Player 2, ask Player 1 a yes-or-no question about their object. (Hit enter once they've answered.)")

        print()

if num_guess == 0:
    print("Sorry, you lost!")
    print("Start another game to play again!")
    print("The correct answer was " + str(answer) + " !")
