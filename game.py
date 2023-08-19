import sys

from utils import check_correctly_word, get_random_word, print_random_word
from settings import NUMB_LETTERS_IN_WORD, NUMB_TRY


def greet_user():
    print('Игра началась. Слово загадано. Попробуйте угадать.')
    print(f'У вас {NUMB_TRY} попыток отгадать слово.')


def get_user_word():
    while True:
        print('Напишите слово:')
        word_user = input()
        if len(word_user) == NUMB_LETTERS_IN_WORD:
            word_check = check_correctly_word(word_user)
            if word_check is not None:
                return word_check
        else:
            print(f'Слово должно быть из {NUMB_LETTERS_IN_WORD} букв')


def output_word (words_user):
    for word in words_user:
        word_split = list(word.upper())
        format_word = '  '.join(word_split)
        print(format_word)


def transform_words_user (words_user):
    list_letters_user = []
    for word in words_user:
        word_split = list(word.upper())
        list_letters_user.append(word_split)
    return list_letters_user


def check_right_word(words_user, word):
    for element in words_user:
        if element == word:
            print('Подравляем, вы угадали слово!!')
            end_game()


def logics(words_user, word):
    indices_letters_guess = set()
    for element in words_user:
        for letter in element:
            for let in word:
                if letter == let:
                    index = word.index(letter)
                    indices_letters_guess.add(index)
                    word[index] = ' '
    return indices_letters_guess


def print_guessed_letter(set_index, word):
    if set_index:
        for elem in set_index:
            letter_guess = word[elem]
            print(f'Есть совпадение буква {letter_guess}')
    else:
        print('Совпадений нет.')

    
def end_game():
    print('Хотите начать заново? да/нет')
    response = input().lower()
    if response == 'да':
        main()
    elif response == 'нет':
        sys.exit()
    else:
        print('Ответ не распознан. Введите да или нет')
        end_game()


def main():
    greet_user()
    word_random = get_random_word()
    letters_word_random = list(word_random.upper())
    words_user = []
    for _ in range(NUMB_TRY):
        copy_letters_word_random = letters_word_random.copy()
        word_user = get_user_word()
        words_user.append(word_user)
        output_word (words_user)
        list_letters_user = transform_words_user(words_user)
        check_right_word(list_letters_user, letters_word_random)
        indices_letters_guess = logics(list_letters_user, copy_letters_word_random)
        print_guessed_letter(indices_letters_guess, letters_word_random)
    print_random_word(word_random)
    end_game()


if __name__ == '__main__':
    main()
