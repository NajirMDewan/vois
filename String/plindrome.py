
def check_palindrome(text):
    '''
    q3: check if string is palindrome using indexing and slicing.
    '''
    clean_text = text.replace(" ", "").lower()

    if clean_text == clean_text[::-1]:
        print(f"\n3. '{text}' is a palindrome.")
    else:
        print(f"\n3. '{text}' is not a palindrome.")


if __name__ == "__main__":
    input_str_3 = "Madam"

    check_palindrome(input_str_3)
