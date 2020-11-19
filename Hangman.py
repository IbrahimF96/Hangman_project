import random
import sys

print("Welcome! Lets play Hangman!")
words = ["abductions", "abridgment", "admixtures"
,"backfields", "blueprints", "chivalrous", "complexity", "cyberpunks", "desolating", "duplicator","earthlings", "fluoridate","flustering","fornicates","godfathers","humanizers","ideographs","journalism","languished","logarithms","mendacious","neighborly","outlandish","palindrome","philanders"
,"proclaimed","randomizes","shrinkable","sublimated","truckloads","upholstery","vanquished","vulcanizes","wanderlust","womanizers" ]

word = random.choice(words)
guesses = "_"*len(word)
print("Here is the word you have to guess: \n {}".format(guesses))
lives = 5
letters_guessed = ""
while lives > 0:
    character_check = input("")
    if character_check in letters_guessed:
        print("You've already picked this character!")
    else:
        if character_check in word and character_check != word:
            a = word.index(character_check)
            guesses = guesses[:a] + word[a] + guesses[a+1:]
            print(guesses)
        if guesses == word or character_check == word:
            print("Winner! You have correctly guessed the word!")
            sys.exit()
        elif character_check not in word:
            lives -= 1
            if lives == 0:
                print("You lose! It was {}".format(word))
                sys.exit()
            print(guesses)
            print("You've only got {} live(s) left!".format(lives))
        letters_guessed += character_check + " "
        print("The letters you have guessed so far are:\n {}".format(letters_guessed))



