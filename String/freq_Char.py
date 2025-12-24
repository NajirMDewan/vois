def char_frequency(text):
    '''
    q4: find frequency of each character in a string.
    '''

    freq = {}
    for char in text:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    print(f"\n4. Character Frequency in '{text}':")
    for char, count in freq.items():
        print(f"   '{char}': {count}")


if __name__ == "__main__":
    char_frequency("banana")
