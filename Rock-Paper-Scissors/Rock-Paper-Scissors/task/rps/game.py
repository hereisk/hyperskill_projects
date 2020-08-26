import random

basic_winning_options = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
basic_losing_options = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
basic_options = ["rock", "paper", "scissors"]

score = 0
ranking = {"Tim": 0, "Jane": 0, "Alex": 0}
name = input("Enter your name: ")
if name not in ranking:
    ranking[name] = 0
print("Hello, " + name)

advanced_options = input()
print("Okay, let's start")

if len(advanced_options) == 0:
    while True:
        user_input = input()
        if user_input == "!exit":
            print("Bye")
            break
        elif user_input == "!rating":
            print(ranking[name])
        elif user_input in basic_options:
            ai_option = random.randint(0, 2)
            if ai_option == 0:
                ai_option = basic_options[0]
            elif ai_option == 1:
                ai_option = basic_options[1]
            elif ai_option == 2:
                ai_option = basic_options[2]

            if ai_option == basic_winning_options[user_input]:
                print("Well done. Computer chose " + ai_option + " and failed")
                ranking[name] += 100
            elif ai_option == basic_losing_options[user_input]:
                print("Sorry, but computer chose " + ai_option)
            else:
                print("There is a draw " + ai_option)
                ranking[name] += 50
        else:
            print("Invalid input")

else:
    advanced_options = advanced_options.split(",")
    while True:
        user_input = input()
        if user_input == "!exit":
            print("Bye")
            break
        elif user_input == "!rating":
            print(ranking[name])
        elif user_input in advanced_options:
            ai_option = advanced_options[random.randint(0, len(advanced_options) - 1)]
            temp_list_back = advanced_options[
                             (advanced_options.index(user_input) + 1): len(advanced_options)].copy()
            temp_list_front = advanced_options[
                              0: advanced_options.index(user_input)].copy()
            advanced_winning_options = temp_list_back + temp_list_front
            if user_input == ai_option:
                print("There is a draw " + ai_option)
                ranking[name] += 50
            elif (advanced_winning_options.index(ai_option) + 1) > (len(advanced_winning_options) / 2):
                print("Well done. Computer chose " + ai_option + " and failed")
                ranking[name] += 100
            else:
                print("Sorry, but computer chose " + ai_option)
        else:
            print("Invalid input")
