def get_book_text(filepath):
    try:
        with open(filepath,"r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."


def get_num_words(content):
    all_words = content.split()
    num_words = len(all_words)
    return num_words


def get_num_chars(content):
    all_chars = {}
    for char in content:
        lower_char = char.lower()
        if lower_char not in all_chars:
            all_chars[lower_char] = 1
        else:
            all_chars[lower_char] += 1
    return all_chars

def sort_on(all_chars):
    return all_chars["num"]

def sorted_list(all_chars):
    key_values = []
    for key, value in all_chars.items():
        key_values .append({"char": key, "num": value})
    key_values.sort(reverse=True, key=sort_on)
    return key_values
