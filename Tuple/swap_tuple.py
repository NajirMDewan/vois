def swap_tuples(t1, t2):
    '''
    Q5: Write a program to swap two tuples.
    '''
    print(f"\n5. Before Swap -> t1: {t1}, t2: {t2}")

    t1, t2 = t2, t1

    print(f"   After Swap  -> t1: {t1}, t2: {t2}")


if __name__ == "__main__":
    tuple_a = (1, 2, 3)
    tuple_b = (9, 8, 7)

    swap_tuples(tuple_a, tuple_b)
