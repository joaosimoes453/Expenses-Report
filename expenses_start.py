import openpyxl
import mysql.connector

# Load the Excel workbook
workbook = openpyxl.load_workbook('expenses.xlsx')
sheet = workbook.active

# MySQL connection setup with connection timeout
db_config = {
    'host': 'localhost',
    'port': '3306',
    'user': 'root',
    'password': 'Simoes.453',
    'database': 'expenses_db',
    'connect_timeout': 300
}

# Connect to the MySQL database
connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

# Iterate through rows and insert data into MySQL
for row in sheet.iter_rows(min_row=2, values_only=True):
    date, category, amount, description = row
    print("Inserting row:", date, category, amount, description)  # Debugging output
    insert_query = "INSERT INTO expenses (date, category, amount, description) VALUES (%s, %s, %s, %s)"
    data = (date, category, amount, description)
    try:
        cursor.execute(insert_query, data)
        connection.commit()
    except mysql.connector.IntegrityError as e:
        print("Duplicate entry, skipping:", e)  # Debugging output

# Close the cursor and connection
cursor.close()
connection.close()

print("Data from Excel has been successfully inserted into MySQL.")
