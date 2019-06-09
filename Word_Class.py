import random


class Word:
    @staticmethod
    def get_random_word():
        with open('include/words.txt') as file:
            data = file.read()

        data = data.replace("\n", "")
        data = data.replace(" ", "")
        data = data.split(",")
        choose_word = random.choice(data)
        for i in range(0, len(data)):
            if data[i] == choose_word:
                Place_in_array = i + 1
                print(
                    "There are %s words in the file and the selected word is in the index %s"
                    % (len(data), Place_in_array))
        return choose_word
