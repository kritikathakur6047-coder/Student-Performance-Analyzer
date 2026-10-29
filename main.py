import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np
import matplotlib.pyplot as plt

students = []
subjects = ["Python", "DBMS", "C", "Maths", "English"]


# Function to add student
def add_student():
    name = name_entry.get().strip()

    if name == "":
        messagebox.showerror("Error", "Enter student name")
        return

    try:
        marks = [int(entry.get()) for entry in mark_entries]
    except ValueError:
        messagebox.showerror("Error", "Enter marks in all subjects")
        return

    if any(mark < 0 or mark > 100 for mark in marks):
        messagebox.showerror("Error", "Marks must be between 0 and 100")
        return

    # Calculate total and percentage using NumPy
    total = int(np.sum(marks))
    percentage = float(np.mean(marks))

    # Calculate grade and result
    if any(mark < 33 for mark in marks):
        grade = "F"
        result = "Fail"
    elif percentage >= 90:
        grade = "A+"
        result = "Pass"
    elif percentage >= 80:
        grade = "A"
        result = "Pass"
    elif percentage >= 70:
        grade = "B"
        result = "Pass"
    elif percentage >= 60:
        grade = "C"
        result = "Pass"
    elif percentage >= 50:
        grade = "D"
        result = "Pass"
    else:
        grade = "E"
        result = "Pass"

    # Store student information in a dictionary
    student = {
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "result": result
    }

    students.append(student)

    # Display student in table
    table.insert(
        "",
        "end",
        values=(
            name,
            total,
            f"{percentage:.2f}%",
            grade,
            result
        )
    )

    messagebox.showinfo(
        "Student Result",
        f"Name: {name}\n"
        f"Total: {total}/500\n"
        f"Percentage: {percentage:.2f}%\n"
        f"Grade: {grade}\n"
        f"Result: {result}"
    )

    # Clear input fields
    name_entry.delete(0, tk.END)

    for entry in mark_entries:
        entry.delete(0, tk.END)


# Function to display chart
def show_chart():
    selected = table.selection()

    if not selected:
        messagebox.showwarning(
            "Warning", "Select a student from the table first"
        )
        return

    # Get the selected student's name
    selected_name = table.item(selected[0], "values")[0]

    for student in students:
        if student["name"] == selected_name:
            plt.figure(figsize=(8, 5))
            plt.bar(subjects, student["marks"])
            plt.title("Student Performance Analysis")
            plt.xlabel("Subjects")
            plt.ylabel("Marks")
            plt.ylim(0, 100)
            plt.tight_layout()
            plt.show()
            return


# Function to clear input fields
def clear_fields():
    name_entry.delete(0, tk.END)

    for entry in mark_entries:
        entry.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.title("Student Performance Analyzer")
root.geometry("800x650")
root.configure(bg="#f2f5f9")

# Heading
heading = tk.Label(
    root,
    text="Student Performance Analyzer",
    font=("Arial", 20, "bold"),
    bg="#f2f5f9"
)
heading.pack(pady=15)

# Input form
form = tk.Frame(root, bg="#f2f5f9")
form.pack()

# Student name
tk.Label(
    form,
    text="Student Name:",
    font=("Arial", 11),
    bg="#f2f5f9"
).grid(row=0, column=0, padx=10, pady=6, sticky="w")

name_entry = tk.Entry(form, font=("Arial", 11), width=22)
name_entry.grid(row=0, column=1, padx=10, pady=6)

# Subject mark input fields
mark_entries = []

for i, subject in enumerate(subjects):
    tk.Label(
        form,
        text=subject + " Marks:",
        font=("Arial", 11),
        bg="#f2f5f9"
    ).grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")

    entry = tk.Entry(form, font=("Arial", 11), width=22)
    entry.grid(row=i + 1, column=1, padx=10, pady=5)

    mark_entries.append(entry)

# Buttons
buttons = tk.Frame(root, bg="#f2f5f9")
buttons.pack(pady=12)

tk.Button(
    buttons,
    text="Add Student",
    command=add_student,
    font=("Arial", 11, "bold"),
    bg="#2878d0",
    fg="white",
    width=14
).grid(row=0, column=0, padx=5)

tk.Button(
    buttons,
    text="Show Chart",
    command=show_chart,
    font=("Arial", 11, "bold"),
    bg="#198754",
    fg="white",
    width=14
).grid(row=0, column=1, padx=5)

tk.Button(
    buttons,
    text="Clear Fields",
    command=clear_fields,
    font=("Arial", 11),
    width=14
).grid(row=0, column=2, padx=5)

# Student records table
columns = ("Name", "Total", "Percentage", "Grade", "Result")

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings",
    height=8
)

for column in columns:
    table.heading(column, text=column)
    table.column(column, width=140, anchor="center")

table.pack(fill="both", expand=True, padx=20, pady=15)

# Run application
root.mainloop()