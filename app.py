import sqlite3
import customtkinter
from tkinter import messagebox, END
from tkinter import ttk

# Initialize the application
app = customtkinter.CTk()
app.title("Employee Management System")
app.geometry("850x500")
app.resizable(True, True)  # Allow resizing

# Colors and Fonts
RED_BG = "#d62828"
BLACK_BG = "#1a1a1a"
FONT1 = ("Arial", 20, "bold")
FONT2 = ("Arial", 15, "bold")

# Configure grid layout for left panel taking more space
app.grid_columnconfigure(0, weight=2)  # Left panel takes more space
app.grid_columnconfigure(1, weight=1)  # Right panel takes less space
app.grid_rowconfigure(0, weight=1)  # Single row that stretches equally

# --- Left Panel: Input Fields and Buttons ---
left_frame = customtkinter.CTkFrame(app, fg_color=RED_BG, corner_radius=10)
left_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

left_frame.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7), weight=1, uniform="rows")  # Equal spacing for inputs and buttons

# Input Fields
id_label = customtkinter.CTkLabel(left_frame, text="ID:", font=FONT1, text_color="white")
id_label.grid(row=0, column=0, padx=15, pady=5, sticky="e")
id_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
id_entry.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

name_label = customtkinter.CTkLabel(left_frame, text="Name:", font=FONT1, text_color="white")
name_label.grid(row=1, column=0, padx=15, pady=5, sticky="e")
name_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
name_entry.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

age_label = customtkinter.CTkLabel(left_frame, text="Age:", font=FONT1, text_color="white")
age_label.grid(row=2, column=0, padx=15, pady=5, sticky="e")
age_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
age_entry.grid(row=2, column=1, padx=10, pady=5, sticky="ew")

role_label = customtkinter.CTkLabel(left_frame, text="Role:", font=FONT1, text_color="white")
role_label.grid(row=3, column=0, padx=15, pady=5, sticky="e")
role_combobox = customtkinter.CTkComboBox(left_frame, values=["Manager", "Developer", "Designer", "Analyst"], font=FONT2)
role_combobox.grid(row=3, column=1, padx=10, pady=5, sticky="ew")

# Hourly Wage Input Field
wage_label = customtkinter.CTkLabel(left_frame, text="Hourly Wage:", font=FONT1, text_color="white")
wage_label.grid(row=4, column=0, padx=15, pady=5, sticky="e")
wage_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
wage_entry.grid(row=4, column=1, padx=10, pady=5, sticky="ew")

# Hours Worked Input Field
hours_label = customtkinter.CTkLabel(left_frame, text="Hours Worked:", font=FONT1, text_color="white")
hours_label.grid(row=5, column=0, padx=15, pady=5, sticky="e")
hours_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
hours_entry.grid(row=5, column=1, padx=10, pady=5, sticky="ew")

# Bonus Input Field
bonus_label = customtkinter.CTkLabel(left_frame, text="Bonus:", font=FONT1, text_color="white")
bonus_label.grid(row=6, column=0, padx=15, pady=5, sticky="e")
bonus_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
bonus_entry.grid(row=6, column=1, padx=10, pady=5, sticky="ew")

# Deduction Input Field
deduction_label = customtkinter.CTkLabel(left_frame, text="Deduction:", font=FONT1, text_color="white")
deduction_label.grid(row=7, column=0, padx=15, pady=5, sticky="e")
deduction_entry = customtkinter.CTkEntry(left_frame, font=FONT2, width=200)
deduction_entry.grid(row=7, column=1, padx=10, pady=5, sticky="ew")

# Database Setup
db = sqlite3.connect("employees.db")
cursor = db.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    Employee_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Role TEXT,
    Hourly_Wage REAL,
    Hours_Worked REAL,
    Bonus REAL DEFAULT 0,
    Deduction REAL DEFAULT 0
)
''')

def calculate_total_salary(hourly_wage, hours_worked, bonus, deduction):
    return (hourly_wage * hours_worked) + bonus - deduction

def insert():
    try:
        emp_id = int(id_entry.get())
        name = name_entry.get()
        age = int(age_entry.get())
        role = role_combobox.get()
        hourly_wage = float(wage_entry.get())
        hours_worked = float(hours_entry.get())
        bonus = float(bonus_entry.get() or 0)  # Default to 0 if empty
        deduction = float(deduction_entry.get() or 0)  # Default to 0 if empty

        total_salary = calculate_total_salary(hourly_wage, hours_worked, bonus, deduction)

        cursor.execute("INSERT INTO Employees VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                       (emp_id, name, age, role, hourly_wage, hours_worked, bonus, deduction, total_salary))
        db.commit()
        messagebox.showinfo("Success", "Employee saved successfully!")
        display_data()
        clear()
    except Exception as e:
        messagebox.showerror("Error", f"Error saving employee: {e}")

def update():
    try:
        emp_id = int(id_entry.get())
        name = name_entry.get()
        age = int(age_entry.get())
        role = role_combobox.get()
        hourly_wage = float(wage_entry.get())
        hours_worked = float(hours_entry.get())
        bonus = float(bonus_entry.get() or 0)
        deduction = float(deduction_entry.get() or 0)

        total_salary = calculate_total_salary(hourly_wage, hours_worked, bonus, deduction)

        cursor.execute("UPDATE Employees SET Name=?, Age=?, Role=?, Hourly_Wage=?, Hours_Worked=?, Bonus=?, Deduction=?, Total_Salary=? WHERE Employee_ID=?", 
                       (name, age, role, hourly_wage, hours_worked, bonus, deduction, total_salary, emp_id))
        db.commit()
        messagebox.showinfo("Success", "Employee updated successfully!")
        display_data()
        clear()
    except Exception as e:
        messagebox.showerror("Error", f"Error updating employee: {e}")

def delete():
    try:
        emp_id = int(id_entry.get())
        cursor.execute("DELETE FROM Employees WHERE Employee_ID=?", (emp_id,))
        db.commit()
        messagebox.showinfo("Success", "Employee deleted successfully!")
        display_data()
        clear()
    except Exception as e:
        messagebox.showerror("Error", f"Error deleting employee: {e}")

def clear():
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    age_entry.delete(0, END)
    role_combobox.set("")
    wage_entry.delete(0, END)
    hours_entry.delete(0, END)
    bonus_entry.delete(0, END)
    deduction_entry.delete(0, END)

# Buttons
button_frame = customtkinter.CTkFrame(left_frame, fg_color=RED_BG)  # Create a frame for buttons
button_frame.grid(row=8, column=0, columnspan=2, padx=15, pady=5, sticky="ew")

save_button = customtkinter.CTkButton(button_frame, text="Save", command=insert, fg_color="black", text_color="white", width=100)
save_button.grid(row=0, column=0, padx=5)

update_button = customtkinter.CTkButton(button_frame, text="Update", command=update, fg_color="black", text_color="white", width=100)
update_button.grid(row=0, column=1, padx=5)

clear_button = customtkinter.CTkButton(button_frame, text="Clear", command=clear, fg_color="black", text_color="white", width=100)
clear_button.grid(row=0, column=2, padx=5)

delete_button = customtkinter.CTkButton(button_frame, text="Delete", command=delete, fg_color="black", text_color="white", width=100)
delete_button.grid(row=0, column=3, padx=5)

# --- Right Panel: TreeView to Display Data ---
right_frame = customtkinter.CTkFrame(app, fg_color=BLACK_BG, corner_radius=10)
right_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

# TreeView for Database Display
tree_frame = customtkinter.CTkFrame(right_frame, fg_color=BLACK_BG)
tree_frame.pack(fill="both", expand=True)

columns = ("Employee ID", "Name", "Age", "Role", "Hourly Wage", "Hours Worked", "Bonus", "Deduction", "Total Salary")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings", selectmode="browse")
tree.pack(side="left", fill="both", expand=True)

# Set specific widths for columns
tree.column("Employee ID", width=80, anchor="center")
tree.column("Name", width=120, anchor="center")
tree.column("Age", width=50, anchor="center")
tree.column("Role", width=100, anchor="center")
tree.column("Hourly Wage", width=100, anchor="center")
tree.column("Hours Worked", width=100, anchor="center")
tree.column("Bonus", width=80, anchor="center")
tree.column("Deduction", width=80, anchor="center")
tree.column("Total Salary", width=100, anchor="center")  # Added Total Salary column

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

def display_data():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, anchor="center")

def display_data():
    for row in tree.get_children():
        tree.delete(row)
    cursor.execute("SELECT * FROM Employees")
    for row in cursor.fetchall():
        tree.insert("", "end", values=row)
        

# Initial Data Display
display_data()
def toggle_fullscreen(event=None):
    app.attributes('-fullscreen', not app.attributes('-fullscreen'))

app.bind('<Escape>', toggle_fullscreen)

# Run the application
app.mainloop()

# Close database connection on exit
db.close()
