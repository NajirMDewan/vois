def demonstrate_immutability():
    '''
    Q5: Demonstrate string immutability by handling the error.
    '''
    text = "Python"
    print(f"\n5. Demonstrating Immutability on string: '{text}'")
    print("   Attempting to change index 0 to 'J'...")

    try:
        # Strings are immutable, so this triggers a TypeError
        text[0] = 'J'
    except TypeError as e:
        print(f"   Error Caught: {e}")
        print("   Conclusion: Strings cannot be modified after creation.")


if __name__ == "__main__":
    demonstrate_immutability()
