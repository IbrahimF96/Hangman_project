import random

words = ["abductions", "abridgment", "admixtures"
,"backfields", "blueprints", "chivalrous", "complexity", "cyberpunks", "desolating", "duplicator","earthlings", "fluoridate","flustering","fornicates","godfathers","humanizers","ideographs","journalism","languished","logarithms","mendacious","neighborly","outlandish","palindrome","philanders"
,"proclaimed","randomizes","shrinkable","sublimated","truckloads","upholstery","vanquished","vulcanizes","wanderlust","womanizers" ]

i = random.randint(0, len(words) - 1)

word = words[i]
guesses = "_"*len(word)
print(guesses)
lives = 0
while lives < 5:
    character_check = input("")
    if character_check in word and character_check != word:
        a = word.index(character_check)
        guesses = guesses[:a] + word[a] + guesses[a+1:]
        print(guesses)
    if guesses == word or character_check == word:
        print("Winner!")
        break
    elif character_check not in word:
        print(lives)
        lives += 1
if lives == 5:
    print("You lose! It was {}".format(word))




