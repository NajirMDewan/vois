import student_data
from marks import process_marks
import attendance as att
import fees
from reports import ReportGenerator
import utils


def main():
    utils.print_header("STUDENT MANAGEMENT SYSTEM")

    while True:
        print("\n1. Add Student")
        print("2. Add Marks & Process")
        print("3. Mark Attendance")
        print("4. Pay Fees")
        print("5. Generate Report")
        print("6. Show Module Properties")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter Name: ")
            roll = student_data.add_new_student(name)
            utils.print_success(f"Student Added! Roll No: {roll}")

        elif choice == '2':
            roll = int(input("Enter Roll No: "))
            if roll in student_data.students_db:
                m1 = float(input("Enter Marks 1: "))
                m2 = float(input("Enter Marks 2: "))
                stu = student_data.students_db[roll]
                stu['marks'] = [m1, m2]

                total, avg = process_marks([m1, m2])
                print(f"Marks Processed. Average: {avg}")
            else:
                print("Student not found.")

        elif choice == '3':
            roll = int(input("Enter Roll No: "))
            if roll in student_data.students_db:
                att.mark_present(student_data.students_db[roll])

        elif choice == '4':
            roll = int(input("Enter Roll No: "))
            if roll in student_data.students_db:
                msg = fees.pay_fee(student_data.students_db[roll])
                print(msg)

        elif choice == '5':
            roll = int(input("Enter Roll No: "))
            if roll in student_data.students_db:
                stu = student_data.students_db[roll]
                _, avg = process_marks(stu['marks'])
                att_pct = att.get_attendance_percentage(stu['attendance'])
                f_status = fees.check_status(stu)

                reporter = ReportGenerator(stu['name'], roll)
                print(reporter.generate_card(avg, att_pct, f_status))

        elif choice == '6':
            print("\n--- Module Properties for 'student_data' ---")
            print(f"1. __name__: {student_data.__name__}")
            print(f"2. __file__: {student_data.__file__}")
            print(f"3. __dict__: {list(student_data.__dict__.keys())}")

        elif choice == '7':
            print("Exiting...")
            break


if __name__ == "__main__":
    main()
