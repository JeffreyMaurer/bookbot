def get_num_words(text: str) -> int:
    delimiters = [' ']
    list1 = text.split('\n')
    list2 = []
    for delimiter in delimiters:
        for item in list1:
            new_list = item.split(delimiter)
            for new_item in new_list:
                if new_item == '':
                    continue
                list2.append(new_item)
        list1 = list2
        list2 = []
    count = len(list1)
    return count

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