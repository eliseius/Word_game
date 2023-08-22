import sys

from logics import check_for_matches, output_guessed_letter
from utils import get_all_short_words, get_nouns_with_definition, get_random_word, print_words_user
from settings import NUMB_LETTERS_IN_WORD, NUMB_TRY


def greet_user():
    print('Игра началась. Слово загадано.')
    print(f'У вас {NUMB_TRY} попыток отгадать слово.')


def get_user_word():
    while True:
        print('\nНапишите слово:')
        word_user = input()
        if len(word_user) == NUMB_LETTERS_IN_WORD:
            word_check = check_correctly_word(word_user)
            if word_check is not None:
                return word_check
        else:
            print(f'Слово должно быть из {NUMB_LETTERS_IN_WORD} букв')


def check_correctly_word(word):
    word_check = {word}
    if word_check & set(get_all_short_words()):
        return word
    else:
        print('Такого слова не существует. Проверьте правильность написания.')
        return None


def transform_words_user (words_user):
    list_letters_user = [list(word.upper()) for word in words_user]
    return list_letters_user


def check_right_word(words_user, word):
    for element in words_user:
        if element == word:
            print('\nПодравляем, вы угадали слово!!')
            end_game()


def print_random_word(word):
    print('\nВы не отгадали слово!\n')
    dictionary = get_nouns_with_definition()
    specification = dictionary.get(word)
    print(f'Загаданное слово')
    print_words_user([word])
    print(f'Значение\n{specification}')


def end_game():
    print('\nХотите начать заново? да/нет')
    response = input().lower()
    if response == 'да':
        main()
    elif response == 'нет':
        sys.exit()
    else:
        print('Ответ не распознан. Введите да или нет')
        end_game()


def play(letters_word_random):
    words_user = []
    for torture in range(NUMB_TRY):
        word_user = get_user_word()
        words_user.append(word_user)
        print_words_user (words_user)
        list_letters_user = transform_words_user(words_user)
        check_right_word(list_letters_user, letters_word_random)
        indices_letters_guess, joint_letters = check_for_matches(list_letters_user, letters_word_random)
        if (torture + 1) != NUMB_TRY:
            output_guessed_letter(indices_letters_guess, letters_word_random, joint_letters)


def main():
    greet_user()
    word_random, letters_word_random = get_random_word()
    play(letters_word_random)
    print_random_word(word_random)
    end_game()

if __name__ == '__main__':
    main()
