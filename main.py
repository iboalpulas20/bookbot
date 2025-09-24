from stats import count_the_words, count_the_characters, sort_on
import sys

if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(file_path):
    with open(file_path) as file:
        file_contents = file.read()
    return file_contents


def main():
    #count_the_words(get_book_text("books/frankenstein.txt"))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    result = count_the_characters(get_book_text(sys.argv[1]))
    print("----------- Word Count ----------")
    count_the_words(get_book_text(sys.argv[1]))
    result = sort_on(result)
    print("--------- Character Count -------")
    for item in result:
        ch=item["char"]
        if not ch.isalpha():
            continue
        print(f"{ch}: {item['num']}")
    print("============= END ===============")
    
main()