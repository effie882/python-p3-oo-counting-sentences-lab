#!/usr/bin/env python3

class MyString:
    def __init__(self, value: str = '') -> None:
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ''
        else:
            self._value = value

    @property
    def value(self) -> str:
        return self._value

    @value.setter
    def value(self, new_value: str) -> None:
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self) -> bool:
        return self.value.endswith(('.', '!', '?'))

    def is_question(self) -> bool:
        return self.value.endswith('?')

    def is_exclamation(self) -> bool:
        return self.value.endswith('!')

    def count_sentences(self) -> int:
        import re
        sentences = re.split(r'[.!?]+', self.value)
        return len([s for s in sentences if s.strip()])
