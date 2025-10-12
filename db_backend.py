import mysql.connector

def connect():
    return mysql.connector.connect(
        host="localhost",
        user="root",        # change to your MySQL username
        password="",  # change to your MySQL password
        database="employee_db"
    )

def insert_employee(name, age, gender, department):
    con = connect()
    cursor = con.cursor()
    cursor.execute("INSERT INTO employees (name, age, gender, department) VALUES (%s, %s, %s, %s)",
                   (name, age, gender, department))
    con.commit()
    con.close()

def fetch_all():
    con = connect()
    cursor = con.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    con.close()
    return rows

def update_employee(emp_id, name, age, gender, department):
    con = connect()
    cursor = con.cursor()
    cursor.execute(
        "UPDATE employees SET name=%s, age=%s, gender=%s, department=%s WHERE id=%s",
        (name, age, gender, department, emp_id)
    )
    con.commit()
    con.close()

def delete_employee(emp_id):
    con = connect()
    cursor = con.cursor()
    cursor.execute("DELETE FROM employees WHERE id=%s", (emp_id,))
    con.commit()
    con.close()
