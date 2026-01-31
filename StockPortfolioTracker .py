import random

words = ["python", "apple", "banana", "orange", "grapes"]

word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("Welcome to Hangman Game!")
print("Guess the word, one letter at a time.")

print("_ " * len(word))

while wrong_guesses < max_wrong:
    guess = input("\nEnter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")
        print(f"Remaining chances: {max_wrong - wrong_guesses}")


    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print(display_word.strip())


    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word)
        break


if wrong_guesses == max_wrong:
    print("\nGame Over! The word was:", word)
