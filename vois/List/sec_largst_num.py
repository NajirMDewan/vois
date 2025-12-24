def find_second_largest(numbers):
    '''
    Q3: Find the second largest element in a list.
    '''
    distinct_nums = []
    for num in numbers:
        if num not in distinct_nums:
            distinct_nums.append(num)

    if len(distinct_nums) < 2:
        print("\n3. List must have at least two distinct numbers.")
        return

    distinct_nums.sort()

    second_max = distinct_nums[-2]

    print(f"\n3. List: {numbers}")
    print(f"   Second Largest Element: {second_max}")


if __name__ == "__main__":
    list_q3 = [50, 20, 10, 50, 40]  # Note the duplicate 50s

    find_second_largest(list_q3)
