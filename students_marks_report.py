from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
students = []
marks = []
with open("marks.txt", "r") as file:
    for line in file:
        name, mark = line.strip().split(",")
        students.append(name)
        marks.append(int(mark))
total_students = len(students)
average_marks = sum(marks) / total_students
highest_marks = max(marks)
lowest_marks = min(marks)
pdf = canvas.Canvas("Student_Report.pdf", pagesize=A4)
width, height = A4
pdf.setFont("Helvetica-Bold", 16)
pdf.drawString(180, height - 50, "Student Marks Report")
pdf.setFont("Helvetica", 12)
pdf.drawString(50, height - 100, f"Total Students: {total_students}")
pdf.drawString(50, height - 130, f"Average Marks: {average_marks:.2f}")
pdf.drawString(50, height - 160, f"Highest Marks: {highest_marks}")
pdf.drawString(50, height - 190, f"Lowest Marks: {lowest_marks}")
pdf.drawString(50, height - 230, "Student Details:")
y = height - 260
for i in range(total_students):
    pdf.drawString(60, y, f"{students[i]} - {marks[i]}")
    y -= 25
pdf.save()
print("PDF Report Generated Successfully!")
