import random
import json

# remove unique values
def checkio(data):
    for index in range(len(data) - 1, -1, -1):
        if data.count(data[index]) == 1:
            del data[index]
    return data


# Opening JSON file
f = open('words.json')
 
# returns JSON object as
# a dictionary
WORDS = json.load(f)

word = random.choice(WORDS)
playerInput = 'aueio'
playerCheck = [0,0,0,0,0] # 0: false, 1: true, 2: not in correct place
tries = 6
attempts = 0
while word.lower() != playerInput.lower() and tries > 0:
    attempts += 1
    if playerInput in WORDS:
        WORDS.remove(playerInput)
    for piIndex in range(0, len(playerInput)):
        if playerInput[piIndex] == word[piIndex]:
            playerCheck[piIndex] = 1
        elif playerInput[piIndex] in word:
            playerCheck[piIndex] = 2
    
    for pcIndex in range(0, len(playerCheck)):
        if playerCheck[pcIndex] == 1:
            possibleWords = []
            for w in WORDS:
                if playerInput[pcIndex] == w[pcIndex]:
                    possibleWords.append(w)
                    WORDS = possibleWords
        elif playerCheck[pcIndex] == 2:
            possibleWords = []
            for w in WORDS:
                if playerInput[pcIndex] in w:
                    possibleWords.append(w)

    possibleWords = checkio(possibleWords)
    if len(possibleWords) > 1:
        print(possibleWords)
        playerInput = random.choice(possibleWords)
        print(playerInput)
    tries -= 1

print("\n")
print(word)
print(attempts)
