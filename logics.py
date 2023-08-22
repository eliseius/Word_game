from utils import create_list_empty


def check_for_matches(words_user, word):
    joint_letters = create_list_empty()
    indices_letters_guess = set()
    for element in words_user:
        for letter in element:
            word_copy = word.copy()
            for letter_word in word_copy:
                if letter == letter_word:
                    index = word_copy.index(letter_word)
                    index_guess = element.index(letter)
                    indices_letters_guess.add(index)

                    if index == index_guess:
                        joint_letters[index] = letter_word

                    len_letter_word = word_copy.count(letter)
                    if len_letter_word > 1:
                        word_copy[index] = None

                    len_letter_guess = element.count(letter)
                    if len_letter_guess > 1:
                        element[index_guess] = None  
    return indices_letters_guess, joint_letters


def output_guessed_letter(set_indices, word, joint_letters):
    if set_indices:
        temp_set_excess_index = set()
        copy_joint_letters = joint_letters.copy()
        for index in set_indices:
            letter_guess = word[index]
            for letter in copy_joint_letters:
                if letter == letter_guess:
                    index_copy_total_letters = copy_joint_letters.index(letter)
                    if index == index_copy_total_letters:
                        temp_set_excess_index.add(index)
                        copy_joint_letters[index] = '*'
        set_indices.difference_update(temp_set_excess_index)
        print_guessed_letters(set_indices, word)
        print_matching_letters(joint_letters)
    else:
        print('Совпадений нет.')
        

def print_guessed_letters(set_indices, word):
    if set_indices:
        for index in set_indices:
            letter_guess = word[index]
            print(f'Буква {letter_guess} есть в загаданном слове')


def print_matching_letters(joint_letters):
    for letter in joint_letters:
        if letter != '*':
            print('Буквы с правильным расположением')
            print(change_format(joint_letters))
            break


def change_format(joint_letters):
    format_joint_letters = '  '.join(joint_letters)
    return format_joint_letters
