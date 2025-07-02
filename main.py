import sys

from stats import get_book_text, get_num_words, get_num_chars, sorted_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        current_book = sys.argv[1]
        print("Usage: python3 main.py <path_to_book>")
    content = get_book_text(current_book)
    full_count = get_num_words(content)
    char_counts = get_num_chars(content)
    full_list = sorted_list(char_counts)
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + current_book + "...")
    print("----------- Word Count ----------") 
    print(f"Found {full_count} total words")
    print("--------- Character Count -------")
    for dict in full_list:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")

main()