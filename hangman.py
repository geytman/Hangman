from Word_Class import Word
from hangman_Photos import hangman_Photos
from hangman_print import hangman_print


def main():
    arr_new = {
        1: hangman_Photos.hangman_Photos_1,
        2: hangman_Photos.hangman_Photos_2,
        3: hangman_Photos.hangman_Photos_3,
        4: hangman_Photos.hangman_Photos_4,
        5: hangman_Photos.hangman_Photos_5,
        6: hangman_Photos.hangman_Photos_6,
        7: hangman_Photos.hangman_Photos_7
    }
    MAX_TRIES = 7
    End_Game = 0
    hangman_print.print_hangman()
    secret_word = Word.Word_Game()
    length_word = len(secret_word)  
    print(
        "You need to guess a %s-letter word. You have 7 attempts If you're wrong"
        % (length_word))
    person_arr = []
    error_person_str = ""

    for _ in range(0, length_word):
        person_arr.append("__")

    hangman_print.Beautiful_printing(person_arr)
    letter_guessed = input('Guess a letter:')
    person = check_valid_input(letter_guessed, error_person_str)

    while (MAX_TRIES != 0):

        if (not (person in secret_word)):
            error_person_str = error_person_str + person
            MAX_TRIES = MAX_TRIES - 1
            End_Game = End_Game + 1
            arr_new[End_Game]()
            if End_Game == 7:
                print("You LOSE The Word Was : %s " % (secret_word))
                print("End Game\n")
                break

        else:
            for i in range(0, length_word):
                if secret_word[i] == person:
                    person_arr[i] = person
                else:
                    continue
            error_person_str = error_person_str + person

        string_arr = ''.join(person_arr)
        if secret_word == string_arr:
            print("Well done, you won !")
            hangman_print.Beautiful_printing(person_arr)
            break

        hangman_print.Beautiful_printing(person_arr)
        letter_guessed = input('Guess a letter:')
        person = check_valid_input(letter_guessed, error_person_str)


def check_valid_input(letter_guessed, old_letters_guessed):
    while (True):
        if not (letter_guessed in old_letters_guessed):
            return letter_guessed
        else:
            print("X")
            print(old_letters_guessed)
            letter_guessed = input('Guess a letter:')


if __name__ == "__main__":
    main()