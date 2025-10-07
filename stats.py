def get_word_count(text):
    num_words = len(text)
    print(f"Found {num_words} total words")

def get_character_count(words):
    character_count = {}
    for word in words:
        letters = list(word)
        for letter in word:
            character_count[letter] = 0

    for word in words:
        letters = list(word)
        for letter in word:
            character_count[letter] += 1
    character_count = sort_on(character_count)
    return character_count

def sort_on(input_dict):
    temp_list = []
    for latter in input_dict:
        number = input_dict[latter]
        temp = {"char": latter, "num": number}
        temp_list.append(temp)
    final = sorted(temp_list, key=lambda x: x["num"], reverse=True)

    return final



