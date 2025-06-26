def num_of_words_in_book(input):
    with open(input) as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = len(words)
    return total_words