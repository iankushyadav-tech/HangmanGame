import random

WORDS = ["python", "computer", "programming", "developer", "keyboard"]

def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = 6

    print("=" * 35)
    print("       CODEALPHA HANGMAN GAME")
    print("=" * 35)
    print("Guess the word one letter at a time.")
    print(f"You can make {max_incorrect} incorrect guesses.\n")

    while incorrect_guesses < max_incorrect:
        display_word = " ".join(
            letter if letter in guessed_letters else "_" for letter in secret_word
        )
        print("Word:", display_word)
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")
        print(f"Incorrect guesses: {incorrect_guesses}/{max_incorrect}")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        guess = input("Enter one letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter (A-Z).\n")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter. Try another.\n")
            continue

        guessed_letters.append(guess)
        if guess in secret_word:
            print("Correct guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

    print("Game over! The word was:", secret_word)

if __name__ == "__main__":
    play_hangman()
