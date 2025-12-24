def count_occurrence_manual(my_tuple, target):
    '''
    Q3: Count occurrence of an element without using
    built-in methods (like .count()).
    '''
    count = 0
    for item in my_tuple:
        if item == target:
            count += 1

    print(f"\n3. Searching for '{target}' in {my_tuple}")
    print(f"   Count: {count}")


if __name__ == "__main__":
    tuple_repeats = (1, 2, 3, 2, 2, 4, 5)

    count_occurrence_manual(tuple_repeats, 2)
