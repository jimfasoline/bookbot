def word_count(booktext):
    num_words = len(booktext.split())
    return num_words

def character_count(booktext):
    lowered_text = booktext.lower()
    total_chars = {}
    for char in lowered_text:
        if char in total_chars:
            total_chars[char] += 1
        else:
            total_chars[char] = 1
    return total_chars

def sort_on(dict):
    return dict["num"]

def sort_chars(total_chars):
    char_list = []

    for char, count in total_chars.items():
        char_list.append({'char': char, 'num': count})

    char_list.sort(reverse=True, key=sort_on)

    return char_list

