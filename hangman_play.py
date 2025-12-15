import random

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list

from hangman_art import logo
from hangman_art import stages


def play_game():
    print(logo)


    lives = 6
    chosen_word = random.choice(word_list)
    print(chosen_word)

    placeholder = "_"
    blank = placeholder * len(chosen_word)
    #word_length = len(chosen_word)
    #for position in range(word_length):
    #    placeholder += "_"
    print("Word to guess: " + blank)

    game_over = False
    guessed_letters = []

    while not game_over:

            print(f"**************************** {lives}/6 LIVES LEFT****************************")
            print("Lives:", "❤️" * lives + "🖤" * (6 - lives))
            guess = input("Guess a letter: ").lower()

            if guess in guessed_letters:
                print(f"⚠️ you already guessed latter : {guess}, 'Guess another one'.")
                continue

            display = ""

            for letter in chosen_word:
                if letter == guess:
                    display += letter
                    print(f"🎉 Nice! '{guess}' is in the word!")
                    guessed_letters.append(guess)
                elif letter in guessed_letters:
                    display += letter
                else:
                    display += "_"

            print("Word to guess: " + display)

            if guess not in chosen_word:
                lives -= 1
                print(f"❌ you've guessed letter: {guess}, that's not in the word, you lost a life.")

                if lives == 0:
                    game_over = True
                    print("ohh..no. you lost all of your lives.")
                    print("💀 GAME OVER 💀")
                    print(f"right word was: {chosen_word} ")


            if "_" not in display:
                game_over = True
                print("🏆🎉 YOU WIN! 🎉🏆")

            print(stages[lives])
while True:
    play_game()
    user_mind = input("🔁want to play again?(y/n)").lower()

    if user_mind != "y":
        print("Goodbye 👋")
        break
    print("NEW GAME STARTED")



