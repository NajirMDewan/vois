def list_unique_conversion(duplicate_list):
    '''
    Q5: Convert list with duplicates to set and
    back to list (to remove duplicates).
    '''
    print(f"\n5. Original List: {duplicate_list}")

    unique_set = set(duplicate_list)

    unique_list = list(unique_set)

    print(f"Set (Unique): {unique_set}")
    print(f"Final List: {unique_list}")


if __name__ == "__main__":
    dupe_list = [10, 20, 20, 30, 10, 40, 50, 50]

    list_unique_conversion(dupe_list)
