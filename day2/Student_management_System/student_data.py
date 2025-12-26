import random

students_db = {}


def add_new_student(name):
    roll_no = random.randint(1000, 9999)
    students_db[roll_no] = {
        "name": name,
        "marks": [],
        "attendance": 0,
        "fees_paid": False
    }
    return roll_no
