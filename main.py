import sys

from stats import num_of_words_in_book

from stats import num_of_times_char_appear_in_book

from stats import character_sorter

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(input):
    with open(input) as f:
    # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text(sys.argv[1])
    total_words = num_of_words_in_book(sys.argv[1])
    character_totals = num_of_times_char_appear_in_book(sys.argv[1])
    print (file_contents)
    print(f"{total_words} words found in the document")
    print(character_totals)
    print(f"============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------\nFound {total_words} total words\n--------- Character Count -------")
    sorted_characters = character_sorter(character_totals)
    for character_dict in sorted_characters:
        print(f"{character_dict['char']}: {character_dict['num']}")
    print("============= END ===============")

main()