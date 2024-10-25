import sqlite3

# Connect to the new salary database
salary_db = sqlite3.connect("salary_management.db")
salary_cursor = salary_db.cursor()

# Create Salary Table
salary_cursor.execute('''
CREATE TABLE IF NOT EXISTS Salaries (
    Salary_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Employee_ID INTEGER NOT NULL,
    Total_Salary REAL NOT NULL,
    Bonus REAL DEFAULT 0,
    Deduction REAL DEFAULT 0,
    FOREIGN KEY (Employee_ID) REFERENCES Employees (Employee_ID)
)''')

def add_salary(employee_id, total_salary, bonus=0, deduction=0):
    """Insert a new salary record."""
    try:
        salary_cursor.execute("INSERT INTO Salaries (Employee_ID, Total_Salary, Bonus, Deduction) VALUES (?, ?, ?, ?)",
                              (employee_id, total_salary, bonus, deduction))
        salary_db.commit()
    except Exception as e:
        print(f"Error adding salary: {e}")

def close_db():
    """Close the database connection."""
    salary_db.close()
