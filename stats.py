def get_num_words(text: str) -> int:
    return text.split().__len__()

def get_char_dict(text: str) -> dict:
    chars = dict()
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

