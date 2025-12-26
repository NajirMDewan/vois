import math


def process_marks(marks_list):
    if not marks_list:
        return 0, 0

    total = math.fsum(marks_list)
    average = total / len(marks_list)

    rounded_avg = math.ceil(average)

    return total, rounded_avg
