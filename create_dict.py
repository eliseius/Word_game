import json

from constants import BAD_INDEX, BAD_SIGN, CONSONANTS


def get_word_list_row():
    with open('russian_nouns.txt', 'r', encoding='utf-8') as file:
        word_list_row = []
        for line in file:
            word_list_row.append(line[:-1])
    return word_list_row


def filter_word(list_row):
    list_words_for_game = []
    all_words_for_check = []
    for word in list_row:
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
    with open('russian_nouns_with_definition.json', 'r', encoding='utf-8') as file:
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
    with open('dictionary.json', 'w', encoding='utf-8') as file:
        json.dump(dict, file, ensure_ascii=False, indent=4)

    with open('all_short_words.json', 'w', encoding='utf-8') as file:
        json.dump(all_words, file, ensure_ascii=False, indent=4)


def main():
    list_words_row = get_word_list_row()
    short_list_word, all_words = filter_word(list_words_row)
    word_definition_row = get_nouns_with_definition()
    selest_dict = selest_word_definition(short_list_word, word_definition_row)
    dictionary = filter_list(selest_dict)
    write_dictionaries(dictionary, all_words)


if __name__ == '__main__':
    main()
    