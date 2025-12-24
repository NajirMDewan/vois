def count_char_types(text):
    '''
    Q1: Count vowels, consonants, digits, and special characters.
    '''
    vowels = 0
    consonants = 0
    digits = 0
    special = 0

    # Convert to lowercase to make vowel checking easier
    lower_text = text.lower()

    for i in range(len(text)):
        char = text[i]
        check_char = lower_text[i]

        if char.isdigit():
            digits += 1
        elif char.isalpha():
            if check_char in 'aeiou':
                vowels += 1
            else:
                consonants += 1
        else:
            # Spaces are technically special characters/whitespace
            if char != ' ':
                special += 1

    print(f"1. Counts for '{text}':")
    print(f'''Vowels: {vowels},\nConsonants: {consonants},
Digits: {digits}, \nSpecial: {special}''')


if __name__ == "__main__":
    input_str_1 = "Hello World! 123"

    count_char_types(input_str_1)
