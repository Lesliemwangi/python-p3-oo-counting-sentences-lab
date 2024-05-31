import re


class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        if not self._value:
            return False
        return self._value.endswith('.')

    def is_question(self):
        if not self._value:
            return False
        return self._value.endswith('?')

    def is_exclamation(self):
        if not self._value:
            return False
        return self._value.endswith('!')

    def count_sentences(self):
        if not self._value:
            return 0

        sentences = re.split(r'[.!?]+', self._value)
        num_sentences = len(
            [sentence for sentence in sentences if sentence.strip()])
        return num_sentences
