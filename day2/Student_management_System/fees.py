COURSE_FEE = 5000


def pay_fee(student_record):
    student_record['fees_paid'] = True
    return "Payment Successful"


def check_status(student_record):
    if student_record['fees_paid']:
        return "Paid"
    else:
        return f"Pending: ${COURSE_FEE}"
