from stats import (get_word_count, get_character_count)

def main():
    message("books/frankenstein.txt")
    

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.split()
        for i in range(0, len(text)):
            text[i] = text[i].lower()
        return text
    

def message(book_file_name):
    book_text = get_book_text(book_file_name)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
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