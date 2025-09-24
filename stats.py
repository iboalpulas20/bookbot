def count_the_words(file_content):
    words = file_content.split()
    num_words = len(words)
    print(f"Found {num_words} total words")
    return num_words
def count_the_characters(file_content):
    lowered_content = file_content.lower()
    character_dict = {}
    for char in lowered_content:
        count = character_dict.get(char, 0) 
        character_dict[char] = count + 1
    return character_dict
def sort_on(character_dict):
    new_char_dict = []
    for char, num in character_dict.items():
        new_char_dict.append({"char": char, "num": num})
    new_char_dict.sort(key=by_num, reverse=True)
    return new_char_dict
def by_num(item):
    return item["num"]