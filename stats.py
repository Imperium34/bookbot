def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        text = text.split()
        for word in text:
            word = word.lower()
        return text
    
def get_word_count(filepath):
    words = get_book_text(filepath)
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_character_count(filepath):
    words = get_book_text(filepath)
    words = words.lower()