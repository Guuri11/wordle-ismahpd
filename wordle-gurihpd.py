import random
import json

MAX_TRIES = 6
INITIAL_WORD = 'orate'
WORD_LIST_FILE = 'words_isma.json'

CHAR_INCORRECT = '0'
CHAR_CORRECT = '1'
CHAR_BAD_POSITION = '2'


def main():
    word_list = load_words()
    solve(word_list)


def load_words():
    f = open(WORD_LIST_FILE, encoding='utf-8')
    return json.load(f)


def solve(word_list):
    check = show_word(INITIAL_WORD)
    
    solve_it(word_list, check, INITIAL_WORD)


def solve_it(word_list, check, last_word):
    for i in range(0, len(last_word)):
        print(f'Checking {i}, check: {check[i]}, char: {last_word[i]}')
    
        if check[i] == CHAR_INCORRECT:
            word_list = words_exclude(word_list, last_word[i])
        if check[i] == CHAR_CORRECT:
            word_list = words_filter(word_list, last_word[i], i)
        if check[i] == CHAR_BAD_POSITION:
            word_list = words_exclude_and_filter(word_list, last_word[i], i)
    
    last_word = choose_from(word_list)
    word_list.remove(last_word)
    
    check = show_word(last_word)
    solve_it(word_list, check, last_word)


def choose_from(word_list):
    # Avoid guessing with double letters, probably inefficient
    guess_list = [word for word in word_list if len(set(word)) == len(word)]
    
    return random.choice(guess_list)


def show_word(word):
    print(word)
    return input('Type result: ')


def words_exclude(word_list, containing_char):
    new_word_list = []
    
    for word in word_list:
        if containing_char in word:
            continue
        
        new_word_list.append(word)
        
    return new_word_list


def words_filter(word_list, containing_char, at_pos):
    new_word_list = []
    
    for word in word_list:
        if containing_char not in word:
            continue
        
        if not char_is_at_pos(word, containing_char, at_pos):
            continue
        
        new_word_list.append(word)
        
    return new_word_list


def words_exclude_and_filter(word_list, containing_char, at_pos):
    new_word_list = []
    
    for word in word_list:
        if containing_char not in word:
            continue
        
        if char_is_at_pos(word, containing_char, at_pos):
            continue
        
        new_word_list.append(word)
        
    return new_word_list


def char_is_at_pos(word, char, pos):
    try:
        return word.index(char) == pos
    except ValueError:
        return False


if __name__ == '__main__':
    main()
