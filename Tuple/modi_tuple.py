def modify_mutable_in_tuple():
    ''''
    Q4: Create a tuple with mutable elements and
    modify the mutable data inside it.
    '''
    my_tuple = (10, 20, ["Python", "Java"])

    print(f"\n4. Original Tuple: {my_tuple}")
    print("   --> Appending 'C++' to the inner list...")

    my_tuple[2].append("C++")
    print(f"   Modified Tuple: {my_tuple}")


if __name__ == "__main__":
    modify_mutable_in_tuple()
