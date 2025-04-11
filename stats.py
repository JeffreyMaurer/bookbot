def get_num_words(text: str) -> int:
    return text.split().__len__()

def get_char_dict(text: str) -> dict:
    chars = dict()
    for c in text:
        c = c.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars

def sort_on(dict):
    return dict.values()

def sort_dict(input: dict) -> dict:
    def sort_on(key):
        return input[key]
    l = list(input)
    l.sort(reverse = True, key = sort_on)
    ret_val = []
    for item in l:
        ret_val.append({item: input[item]})
    return ret_val