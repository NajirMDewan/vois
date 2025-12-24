def set_operations(set1, set2):
    '''
    Q1: Find union, intersection, difference, and symmetric difference.
    '''
    print(f"1. Set A: {set1}, Set B: {set2}")

    u = set1.union(set2)
    print(f"   Union: {u}")

    i = set1.intersection(set2)
    print(f"   Intersection: {i}")

    d = set1.difference(set2)
    print(f"   Difference (A - B): {d}")

    sd = set1.symmetric_difference(set2)
    print(f"   Symmetric Difference: {sd}")


if __name__ == "__main__":
    # Test Data
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    set_operations(A, B)
