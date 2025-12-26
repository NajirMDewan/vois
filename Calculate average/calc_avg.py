# def calculate_grade(average):
#     if average >= 90:
#         return "A"
#     elif 75 <= average <= 89:
#         return "B"
#     elif 60 <= average <= 74:
#         return "C"
#     else:
#         return "Fail"


def main():
    students = {}

    print("--- Enter Details for 5 Students ---")
    for i in range(5):
        print(f"\nStudent {i+1}:")
        name = input("Enter Student Name: ")

        marks = []
        for j in range(1, 4):
            m = int(input(f"Enter marks for Subject {j}: "))
            marks.append(m)

        students[name] = marks

    top_scorer_name = ""
    top_scorer_avg = -1

    for name, marks in students.items():
        average_marks = sum(marks) / len(marks)

        if average_marks > top_scorer_avg:
            top_scorer_avg = average_marks
            top_scorer_name = name

    print("-" * 35)

    print(f"\nTop Scorer: {top_scorer_name}")
    print(f"Highest Average: {top_scorer_avg:.2f}")


if __name__ == "__main__":
    main()
