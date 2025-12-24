def find_max_min(my_tuple):
    '''
    Q1: Find the maximum and minimum elements in a tuple.
    '''
    maximum = max(my_tuple)
    minimum = min(my_tuple)

    print(f"1. Tuple: {my_tuple}")
    print(f"   Max: {maximum}, Min: {minimum}")


if __name__ == "__main__":
    tuple_nums = (10, 5, 8, 20, 3)

    find_max_min(tuple_nums)
