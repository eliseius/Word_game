import json
import random


def get_nouns_with_definition():
    with open('dictionary.json', 'r', encoding='utf-8') as file:
        dictionary = json.load(file)
    return dictionary


def get_random_word():
    dictionary = get_nouns_with_definition()
    words = []
    for key in dictionary.keys():
        words.append(key)
    return random.choice(words)


def get_all_short_words():
    with open('all_short_words.json', 'r', encoding='utf-8') as file:
        all_short_words = json.load(file)
    return all_short_words


def check_correctly_word(word):
    all_short_words = get_all_short_words()
    word_check = []
    word_check.append(word)
    if set(word_check) & set(all_short_words):
        return word
    else:
        print('Такого слова не существует. Проверьте правильность написания.')
        return None


def print_random_word(word):
    dictionary = get_nouns_with_definition()
    specification = dictionary.get(word)
    print(f'Загаданное слово {word}')
    print(f'Значение\n{specification}')
