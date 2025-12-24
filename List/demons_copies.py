import copy


def demonstrate_copies():
    '''
    Q5: Demonstrate shallow copy and deep copy of a list with mutable elements.
    '''
    print("\n5. Shallow vs Deep Copy Demonstration:")

    original = [1, 2, [3, 4]]

    shallow = copy.copy(original)

    deep = copy.deepcopy(original)

    print(f"   Original before change: {original}")

    print("   --> Modifying inner list of Original: Changing 3 to 999")
    original[2][0] = 999

    print(f"   Original: {original}")
    print(f"   Shallow : {shallow}  (Reflects change - BAD if unwanted)")
    print(f"   Deep    : {deep}  (Unaffected - GOOD for isolation")


if __name__ == "__main__":
    demonstrate_copies()
