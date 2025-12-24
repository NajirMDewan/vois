def filter_even_numbers(numbers):
    '''
    Q2: Create a new list containing only even
    numbers using list comprehension.
    '''
    # List comprehension: [expression for item in list if condition]
    even_numbers = [num for num in numbers if num % 2 == 0]

    print(f"\n2. Original: {numbers}")
    print(f"   Even Numbers (List Comp): {even_numbers}")


if __name__ == "__main__":
    list_q2 = [10, 15, 20, 25, 30, 33]

    filter_even_numbers(list_q2)
