from string import ascii_lowercase as letters

def get_num_words(text: str) -> int:
    return text.split().__len__()

def get_char_dict(text: str) -> dict:
    lower_text = text.lower()
    return {letter : lower_text.count(letter) for letter in set(lower_text)}
