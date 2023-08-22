import json

from pathlib import Path

from constants import BAD_INDEX, BAD_SIGN, CONSONANTS


def get_word_list_raw():
    path = get_file_path('raw', 'russian_nouns.txt')
    with open(path, 'r', encoding='utf-8') as file:
        word_list_row = []
        for line in file:
            word_list_row.append(line[:-1])
    return word_list_row


def filter_word(list_raw):
    list_words_for_game = []
    all_words_for_check = []
    for word in list_raw:
        if len(word) == 5:
            all_words_for_check.append(word)
            if set(word).isdisjoint(BAD_SIGN):
                count = 0
                for letter in list(word):
                    if letter in CONSONANTS:
                        count += 1
                if count < 4:
                    list_words_for_game.append(word)
    return list_words_for_game, all_words_for_check


def get_nouns_with_definition():
    path = get_file_path('raw', 'russian_nouns_with_definition.json')
    with open(path, 'r', encoding='utf-8') as file:
        nouns_with_definition = json.load(file)
    return nouns_with_definition


def selest_word_definition(list, dict):
    selest_dict= {}
    for word in list:
        for element in dict:
            if element == word:
                selest_dict[element] = dict[element]["definition"]
    return selest_dict


def filter_list(dict):
    filter_dict = {}
    for element in dict:
        definition = dict.get(element).split(' ')
        if BAD_INDEX.isdisjoint(set(definition)):
            filter_dict[element] = dict.get(element)
    return filter_dict


def write_dictionaries(dict, all_words):
    path = get_file_path('ready', 'dictionary.json')
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(dict, file, ensure_ascii=False, indent=4)

    path = get_file_path('ready', 'all_short_words.json')
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(all_words, file, ensure_ascii=False, indent=4)


def get_file_path(catalog, name):
    dir_path = Path.cwd()
    path = Path(dir_path, 'dictionaries', catalog, name)
    return path


def main():
    list_words_raw = get_word_list_raw()
    short_list_word, all_words = filter_word(list_words_raw)
    word_definition_raw = get_nouns_with_definition()
    selest_dict = selest_word_definition(short_list_word, word_definition_raw)
    dictionary = filter_list(selest_dict)
    write_dictionaries(dictionary, all_words)


if __name__ == '__main__':
    main()
    