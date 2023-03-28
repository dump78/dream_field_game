import random
import re


class TextCleaner:
    """Класс удаляет из исходного списка слов лишние символы"""

    def __init__(self, text):
        self.text = text

    def clean_text(self):
        self.text = re.sub(r'[^а-яА-ЯёЁ\s]', '', self.text)
        return self.text

class DreamFieldGame:
    """Класс реализует логику игры 'Поле чудес'"""

    def __init__(self):
        with open('russian_nouns.txt', 'r', encoding='utf-8') as text:
            text = str(text.readlines())
            text_cleaner = TextCleaner(text)
            self.words_list = text_cleaner.clean_text().split()

        self.wrong_letters = []
        self.tries_num = 15
        self.guessed_word = random.choice(self.words_list)
        self.game_result = ['-' for _ in range(len(self.guessed_word))]

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

    def take_guess(self, guess):
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
