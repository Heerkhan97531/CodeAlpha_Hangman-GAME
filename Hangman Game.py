#-------Python Intenship Project------

import random
list_of_words = ["laiba", "intern", "Pakistan", "Python", "Cyber_security"]
word = random.choice(list_of_words).lower()

guessed_letters = []
incorrect_guesses = 0
max_guesses = 6
print("\n---Welcome to Hangman Game---\n===================================")
while True:
    display = ""
    for char in word:
        if char in guessed_letters:
            display +=char +" "
        else:
            display += "-"
    print("\nWord: ",display)

    if "-" not in display:
        print("Congratulations🎉, you Won..!!")
        break

    guess = input("Enter a single letter: ").lower()
    if guess in guessed_letters:
        print("You already have to guessed, try another.")
        continue
    guessed_letters.append(guess)
    if guess in word:
        print("Correct Answer! This letter is involved into word.")
    else:
        incorrect_guesses+=1
        rermaining = max_guesses-incorrect_guesses
        print(f"THis attempt is wrong! you have {rermaining} remaining attempts.")  
    if incorrect_guesses == max_guesses:
        print("\n Game over! You lost. ")
        print("The correct word is: ", word)              

        





