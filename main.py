from stats import (get_word_count, get_character_count)
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_file_path = sys.argv[1]
    message(book_file_path)
    

def get_book_text(book_file_path):
    with open(book_file_path) as f:
        text = f.read()
        text = text.split()
        for i in range(0, len(text)):
            text[i] = text[i].lower()
        return text
    

def message(book_file_path):
    book_text = get_book_text(book_file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}...")
    print("----------- Word Count ----------")
    get_word_count(book_text)
    print("--------- Character Count -------")
    character_count = get_character_count(book_text)
    for i in range(0, len(character_count)):
        character = character_count[i]["char"]
        if str(character).isalpha() is True:
            print(f"{character_count[i]["char"]}: {character_count[i]["num"]}")
    print("============= END ===============")


main()