def check_subset(set_a, set_b):
    '''
    Q3: Check whether one set is a subset of another.
    '''
    is_sub = set_a.issubset(set_b)

    print(f"\n3. Is {set_a} a subset of {set_b}?")
    print(f"   Answer: {is_sub}")


if __name__ == "__main__":
    subset_test_1 = {1, 2}
    subset_test_2 = {1, 2, 3, 4, 5}

    check_subset(subset_test_1, subset_test_2)
