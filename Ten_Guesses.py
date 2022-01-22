"""
LESSON: 2.4 - While Loops
EXERCISE: Ten Guesses
"""
#### ---- SET UP ---- ####

# Have Player 1 enter an object in lower-case letters.
# Assign to the variable answer.
answer = input("Player 1: Enter an object in lower-case letters. ")

# BONUS: Do you remember what this line of code does?
# ---> TEST AFTER THIS LINE <--- #
print("\n" * 100)

# Assign the value 10 to the variable num_guess
print("Let's play ten guesses! ")
print("Each time you guess you can ask the other player a yes/no question out loud and then guess again! ")
print()
num_guess = 10

#### ---- MAIN LOOP ---- ####

# WHILE num_guess is GREATER THAN 0
while num_guess > 0:

    # Get Player 2's guess and assign it to guess
    guess = input("Player 2: What is your guess? ")


    #### ---- CORRECT GUESS ---- ####

    # IF guess is EQUAL TO answer
    if guess == answer:
        

        # Print a congratulations message
        print("Congratulations! You got it!")

        # BREAK out of the guessing loop
        # ---> TEST AFTER THIS LINE <--- #
        break


    #### ---- INCORRECT GUESS ---- ####

    # ELSE
    else:

        # Decrement num_guess by 1
        # ---> TEST AFTER THIS LINE <--- #
        num_guess -= 1

        # Print an "incorrect guess" message
        print("Incorrect guess. Ask the other player a yes/no question and try again.")

        # IF there are more than 0 num_guess left
        if num_guess > 0:

            # Print how many guesses they have remaining
            # (Hint: num_guess variable)
            print("You have " + str(num_guess) + " guesses remaining. ")

            # Print a blank line for spacing
            # ---> TEST AFTER THIS LINE <--- #
            print()

            # Get input using the prompt "Player 2, ask
            # Player 1 a yes-or-no question about their
            # object. (Hit enter once they've answered.)"
            guess = input("Player 2, ask Player 1 a yes-or-no question about their object. (Hit enter once they've answered.)")

        # Print a blank line for spacing
        # ---> TEST AFTER THIS LINE <--- #
        print()


#### ---- FINAL OUTPUT ---- ####

# IF num_guess is 0
if num_guess == 0:

    # Tell the user they did not guess it in time
    print("Sorry, you lost!")
    print("Start another game to play again!")

    # Print what the correct answer was
    # ---> TEST AFTER THIS LINE <--- #
    print("The correct answer was " + str(answer) + " !")


# Turn in your Coding Exercise.

