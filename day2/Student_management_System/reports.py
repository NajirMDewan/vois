from datetime import datetime


class ReportGenerator:
    def __init__(self, student_name, roll_no):
        self.name = student_name
        self.roll_no = roll_no
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def generate_card(self, avg_marks, attendance_pct, fee_status):
        report = f"""
        --- REPORT CARD ---
        Date: {self.date}
        Student: {self.name} (Roll: {self.roll_no})
        -------------------
        Average Marks: {avg_marks}
        Attendance:    {attendance_pct}%
        Fee Status:    {fee_status}
        -------------------
        """
        return report
