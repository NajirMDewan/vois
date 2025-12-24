def remove_duplicates_no_set(input_list):
    '''
    Q1: Remove duplicate elements from a list without using set.
    '''
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)

    print(f"1. Original: {input_list}")
    print(f"   No Duplicates: {unique_list}")


if __name__ == "__main__":
    list_q1 = [1, 2, 2, 3, 4, 4, 5]

    remove_duplicates_no_set(list_q1)
