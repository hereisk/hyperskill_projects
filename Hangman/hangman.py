import random
import string

word_list = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(word_list)
world = list(word)
displayed_word = "-" * len(word)
attempts = 0
past_guesses = []

print("H A N G M A N\n")

user_choice = input('Type "play" to play the game, "exit" to quit: ')
print()

if user_choice == "play":
    while attempts != 8:
        print(displayed_word)
        displayed_word = list(displayed_word)
        user_input = (input("Input a letter: "))
        if len(user_input) != 1:
            print("You should input a single letter")
        elif user_input not in string.ascii_lowercase:
            print("It is not an ASCII lowercase letter")
        elif user_input in past_guesses:
            print("You already typed this letter")
        elif user_input not in word:
            print("No such letter in the word")
            attempts += 1
            past_guesses += user_input
        else:
            past_guesses += user_input
            if user_input in word:
                for i in word:
                    if user_input == i:
                        displayed_word[word.index(i)] = user_input
        displayed_word = "".join(str(i) for i in displayed_word)
        if "-" not in displayed_word:
            print("You guessed the word" + displayed_word + "!\nYou survived!")
            break
        if attempts == 8:
            print("You are hanged!")
            break

        print()
else:
    exit()
