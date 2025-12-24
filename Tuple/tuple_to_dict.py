def list_of_tuples_to_dict(tuple_list):
    '''
    Q2: Convert a list of tuples into a dictionary.
    '''
    result_dict = dict(tuple_list)

    print(f"\n2. List of Tuples: {tuple_list}")
    print(f"   Dictionary: {result_dict}")


if __name__ == "__main__":
    list_tups = [("Name", "Alice"), ("Age", 25), ("City", "New York")]

    list_of_tuples_to_dict(list_tups)
