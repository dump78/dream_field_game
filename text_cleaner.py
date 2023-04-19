import re


class TextCleaner:
    """Класс удаляет из исходного слова все символы, кроме русских букв"""

    def __init__(self, cleaned_word):
        self.cleaned_word = cleaned_word

    def clean_text(self):
        self.cleaned_word = re.sub(r'[^а-яА-ЯёЁ]', '', self.cleaned_word)
        return self.cleaned_word
