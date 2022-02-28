import random

WORDS = ['adios', 'reino', 'balon', 'palas', 'palos']
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = random.choice(WORDS)
playerInput = ''.join(random.choices(ALPHABET, k=5))
playerCheck = [0,0,0,0,0] # 0: false, 1: true, 2: not in correct place
tries = 6
attempts = 0
while word != playerInput and tries > 0:
    attempts += 1
    for piIndex in range(0, len(playerInput)):
        if playerInput[piIndex] == word[piIndex]:
            playerCheck[piIndex] = 1
        elif playerInput[piIndex] in word:
            playerCheck[piIndex] = 2
        elif playerInput[piIndex] not in word and playerInput[piIndex] in ALPHABET:
            ALPHABET.remove(playerInput[piIndex])
    for pcIndex in range(0, len(playerCheck)):
        replacements = []
        if playerCheck[pcIndex] == 0 or playerCheck[pcIndex] == 2:
            s = list(playerInput)
            s[pcIndex] = ''.join(random.choices(ALPHABET, k=1))
            playerInput = "".join(s)
        if playerCheck[pcIndex] == 2:
            replacements.append(pcIndex)
    
    # Replace playerChecks' 2s
    if len(replacements) > 1:
        for rpIndex in range(0, len(replacements)-1):
            s = list(playerInput)
            aux = s[replacements[rpIndex+1]]
            s[replacements[rpIndex+1]] = s[replacements[rpIndex]]
            s[replacements[rpIndex]] = aux
            playerInput = "".join(s)
    print(ALPHABET)
    print(playerInput)
    print(playerCheck)
    print(attempts)
