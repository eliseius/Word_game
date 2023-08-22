import json
import random

from settings import NUMB_LETTERS_IN_WORD


def get_nouns_with_definition():
    with open('dictionary.json', 'r', encoding='utf-8') as file:
        dictionary = json.load(file)
    return dictionary


def get_random_word():
    dictionary = get_nouns_with_definition()
    words = [key for key in dictionary.keys()]
    word_random = random.choice(words)
    letters_word_random = list(word_random.upper())

    return word_random, letters_word_random


def get_all_short_words():
    with open('all_short_words.json', 'r', encoding='utf-8') as file:
        all_short_words = json.load(file)
    return all_short_words


def create_list_empty():
    list_empty = []
    for _ in range(NUMB_LETTERS_IN_WORD):
        list_empty.append(' ')
    return list_empty


def print_words_user (words_user):
    for word in words_user:
        word_split = list(word.upper())
        format_word = '  '.join(word_split)
        print(format_word)


if __name__ == '__main__':
    pass