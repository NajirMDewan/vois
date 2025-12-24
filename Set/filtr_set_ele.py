def filter_set_elements(my_set, threshold):
    '''
    Q4: Iterate over a set and print only elements greater than a given number.
    '''
    print(f"\n4. Elements in {my_set} greater than {threshold}:")

    found = False
    for item in my_set:
        if item > threshold:
            print(f"   -> {item}")
            found = True

    if not found:
        print("   (None found)")


if __name__ == "__main__":
    nums_set = {10, 55, 23, 8, 90, 4}
    filter_set_elements(nums_set, 20)
