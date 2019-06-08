class hangman_print:

    @staticmethod
    def print_hangman():
        with open('include/hangman_welcome.txt') as file:
            data = file.read()
            print(data)
        print(
            "Welcome to Hangman! A word will be chosen at random and you must try to guess the word correctly letter by letter before you run out of attempts. Good luck! "
        )

    @staticmethod
    def Beautiful_printing(person_arr):
        WordToPrint = str(person_arr)
        WordToPrint = WordToPrint.replace("[", "")
        WordToPrint = WordToPrint.replace("]", "")
        WordToPrint = WordToPrint.replace(",", " ")
        WordToPrint = WordToPrint.replace("'", "")
        print(WordToPrint)
        print(" ")
