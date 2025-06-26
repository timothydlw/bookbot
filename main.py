from stats import num_of_words_in_book

def get_book_text(input):
    with open(input) as f:
    # do something with f (the file) here
        # f is a file object
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    total_words = num_of_words_in_book("books/frankenstein.txt")
    print (file_contents)
    print(f"{total_words} words found in the document")

main()