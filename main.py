def get_book_text(filepath):
    try:
        with open(filepath,"r") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return "Error: File not found."

def main():
    content = get_book_text("books/frankenstein.txt")
    word_count(content)

def word_count(content):
    all_words = content .split()
    num_words = len(all_words)
    print(num_words, "words found in the document")

main()


