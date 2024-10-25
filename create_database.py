import sqlite3

# Database Setup
db = sqlite3.connect("employees.db")
cursor = db.cursor()

# Create the Employees table if it does not exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS Employees (
    Employee_ID INTEGER PRIMARY KEY,
    Name TEXT,
    Age INTEGER,
    Role TEXT,
    Hourly_Wage REAL,
    Hours_Worked REAL,
    Bonus REAL DEFAULT 0,
    Deduction REAL DEFAULT 0,
    Total_Salary REAL DEFAULT 0
)
''')

db.commit()
