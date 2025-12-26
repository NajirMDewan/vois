def mark_present(student_record):
    student_record['attendance'] += 1
    print(f"Attendance marked. Total days present: {student_record['attendance']}")


def get_attendance_percentage(days_present, total_working_days=100):
    return (days_present / total_working_days) * 100
