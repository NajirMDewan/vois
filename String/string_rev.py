def reverse_words(text):
    '''
    q2: reverse each word individually without changing word order.
    '''
    words = text.split()
    reversed_words = [word[::-1] for word in words]
    result = " ".join(reversed_words)
    print(f"\nOriginal: '{text}' -> \nReversed words: '{result}'\n")


if __name__ == "__main__":
    input_str_2 = "Python Programming"

    reverse_words(input_str_2)
