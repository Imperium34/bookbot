def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.split()
        for i in range(0, len(text)):
            text[i] = text[i].lower()
        return text
    
def get_word_count(filepath):
    words = get_book_text(filepath)
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_character_count(filepath):
    words = get_book_text(filepath)
    character_count = {}
    for word in words:
        letters = list(word)
        for letter in word:
            character_count[letter] = 0

    for word in words:
        letters = list(word)
        for letter in word:
            character_count[letter] += 1
    print(character_count)