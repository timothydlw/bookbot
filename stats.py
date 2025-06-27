def num_of_words_in_book(input):
    with open(input) as f:
        file_contents = f.read()
        words = file_contents.split()
        total_words = len(words)
    return total_words

def num_of_times_char_appear_in_book(input):
    character_totals = {}
    with open(input) as f:
        file_contents = f.read()
        lower_case_string = file_contents.lower()
        for character in lower_case_string:
            if character in character_totals:
                character_totals[character] += 1
            else:
                character_totals[character] = 1
        return character_totals