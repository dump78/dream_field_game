import random
from text_cleaner import TextCleaner


class DreamFieldGame:
    """Класс реализует логику игры 'Поле чудес'"""

    def __init__(self):
        words_number_list = 51300  # количество слов (строк) в исходном списке (файле)
        self.random_word_number = random.randint(0, words_number_list)  # случайный номер слова (строки файла)
        with open('russian_nouns.txt', 'r', encoding='utf-8') as text:
            for word_number, word in enumerate(text):
                if word_number == self.random_word_number:
                    self.guessed_word = word
                    text_cleaner_obj = TextCleaner(word)
                    self.guessed_word = text_cleaner_obj.clean_text()
        self.wrong_letters = []  # список использованных неверных букв
        self.tries_num = 15  # количество попыток
        self.game_result = ['-' for _ in range(len(self.guessed_word))]  # исходное маскированное слово

    def main(self):
        print(*"Поле чудес")
        print("У вас есть 15 попыток, чтобы угадать слово")
        self.play_game()

    def play_game(self):
        while True:
            if self.game_result == list(self.guessed_word):
                print("Вы угадали слово!")
                print(f"Загаданное слово: {self.guessed_word}")
                break
            elif self.tries_num == 0:
                print("Вы проиграли!")
                print(f"Загаданное слово: {self.guessed_word}")
                break
            print(f"\n{''.join(self.game_result)}")
            self.take_guess(input("Введите букву: ").lower())

    def take_guess(self, guess: str) -> None:
        if len(guess) == 0 or len(guess) > 1:
            print("Введите одну букву")
        elif not guess.isalpha():
            print("Введите одну букву на русском языке")
        elif guess not in self.guessed_word:
            if guess in self.wrong_letters:
                print("Вы уже вводили эту букву\nЭтой буквы нет в загаданном слове")
            else:
                self.wrong_letters.append(guess)
                self.tries_num = self.tries_num - 1
                print(f"Этой буквы нет в загаданном слове\nУ вас осталось {self.tries_num} попыток")
        elif guess in self.game_result:
            print("Вы уже вводили эту букву")
        else:
            indices = [index for index, letter in enumerate(self.guessed_word) if guess == letter]
            for index in indices:
                self.game_result[index] = guess


if __name__ == '__main__':
    while True:
        option = input("Введите 'играть' для начала игры, 'выход' чтобы выйти и нажмите Enter: ").lower()
        if option == "играть":
            DreamFieldGame().main()
        else:
            break
