def remove_common_elements(s1, s2):
    '''
    Q2: Remove common elements from two sets.
    '''
    print(f"\n2. Original Sets -> A: {s1}, B: {s2}")

    common = s1.intersection(s2)
    print(f"   Common Elements: {common}")

    s1.difference_update(common)
    s2.difference_update(common)

    print(f"   After Removing Common -> A: {s1}, B: {s2}")


if __name__ == "__main__":
    A = {1, 2, 3, 4, 5}
    B = {4, 5, 6, 7, 8}

    remove_common_elements(A.copy(), B.copy())
