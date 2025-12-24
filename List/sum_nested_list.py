def sum_nested_lists(nested_list):
    '''
    Q4: Create a nested list and calculate the sum of each inner list.
    '''
    print(f"\n4. Nested List: {nested_list}")
    print("   Sums of inner lists:")

    for i, inner_list in enumerate(nested_list):
        total = sum(inner_list)
        print(f"   Inner list {i+1} {inner_list} Sum: {total}")


if __name__ == "__main__":
    list_q4 = [[1, 2, 3], [10, 20], [5, 5, 5, 5]]

    sum_nested_lists(list_q4)
