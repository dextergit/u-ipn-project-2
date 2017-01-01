# IPND Stage 2 Final Project

"""
References:
1. ipnd-starter-code-master.zip: fill-in-the-blanks.py and fill-in-the-blanks.pyc
2. https://storage.googleapis.com/supplemental_media/udacityu/7710122499/madlibs_generator.py
"""

waiting_for_user_input = True
game_level = 0
guess_items_in_level = ""
string_to_guess = ""
answers = ""

def get_rules(_game_level):
# Sets the rules of the game. Inputs game level. Outputs game parameters including max number of guesses and answers.

    if game_level == "1":
        _max_guesses = 4
        _string_to_guess = "A ___1___ in ___2___ is created with the ___3___ ___4___."
        _guess_items_in_level = [0, 1, 2, 3]
        _answers = ["function", "Python", "def", "keyword"]
        _game_description = "Easy"
    elif game_level == "2":
        _max_guesses = 3
        _string_to_guess = "You specify the inputs a ___1___ takes by adding ___2___ separated by ___3___ between the ___4___."
        _guess_items_in_level = [0, 1, 2, 3]
        _answers = ["function", "variables", "commas", "parentheses"]
        _game_description = "Medium"
        pass
    elif game_level == "3":
        _max_guesses = 2
        _string_to_guess = "___1___s by default return ___2___ if you don't specify the value to return. Return ___3___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions."
        _guess_items_in_level = [0, 1, 2, 3]
        _answers = ["Function", "None", "values", "list"]
        _game_description = "Hard"
        pass

    return [_max_guesses, _string_to_guess, _guess_items_in_level, _answers, _game_description]

def user_output(_message):
# Standardizes print output. Inputs string to pass to print function. Outputs message to screen.
    print ""
    print _message
    print ""

def integrate_answer(_guess, _array_to_guess, _guess_item):
# Integrates the answer into the guess string. Inputs the guess, guess array (derived from guesss string), and guess item (string to replace with user's guess). Outputs modified guess array.

    for i in _array_to_guess:
        # print(i + " " + _guess_item)
        if _guess_item in i:
            # print "replace: " + i + " with " + _guess
            a = _array_to_guess.index(i)
            _array_to_guess[a] = _array_to_guess[a].replace(_guess_item, _guess)

            return _array_to_guess

# Main --

user_output("Welcome to the IPN Game.")

while waiting_for_user_input:

    game_level = raw_input("Select a Level (1, 2, 3): ")

    if game_level == "1":
        waiting_for_user_input = False
    elif game_level == "2":
        waiting_for_user_input = False
    elif game_level == "3":
        waiting_for_user_input = False
    else:
        user_output("You picked a level that does not exist.")

rules = get_rules(game_level)

max_guesses = rules[0]
string_to_guess = rules[1]
guess_items_in_level = rules[2]
answers = rules[3]
game_description = rules[4]
score = 0

user_output("You picked Level " + game_level + " - " + game_description  + ".")

array_to_guess = string_to_guess.split()
playing = True

for guess_item in guess_items_in_level:
    waiting_for_user_input = True
    guess_counter = 0

    while waiting_for_user_input and playing:

        user_output(string_to_guess)

        guess = raw_input("Guess an answer for ___" + str(guess_item + 1) + "___: ")

        if guess == answers[guess_item]:
            user_output("Correct!")
            score += 1
            waiting_for_user_input = False
            array_to_guess = integrate_answer(guess, array_to_guess, "___" + str(guess_item + 1) + "___")
            string_to_guess = " ".join(array_to_guess)

        else:
            guess_counter +=1
            print "Wrong answer. Guesses left: " + str(max_guesses - guess_counter) + "."
            if guess_counter >= max_guesses:
                print "Game over."
                playing = False
                break

if score == len(guess_items_in_level):
    user_output("You won!--> " + string_to_guess)
