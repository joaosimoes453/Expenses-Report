from flask import Flask, render_template, request
import mysql.connector
import expenses_start
import os
from dotenv import load_dotenv

app = Flask(__name__)

# MySQL connection setup
db_config = {
    'host': os.getenv('DB_HOST'),
    'port': os.getenv('DB_PORT'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME'),
    'connect_timeout': 300
}

def get_expenses_data(search_query='', category_filter=''):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    query = "SELECT * FROM expenses WHERE description LIKE %s AND category LIKE %s"
    query_params = (f'%{search_query}%', f'%{category_filter}%')
    cursor.execute(query, query_params)
    data = cursor.fetchall()

    cursor.close()
    connection.close()

    return data


@app.route('/', methods=['GET'])
def index():
    search_query = request.args.get('search', '')
    category_filter = request.args.get('category', '')
    expenses_data = get_expenses_data()

    # Apply search and filtering
    if search_query:
        expenses_data = [expense for expense in expenses_data if search_query.lower() in expense[2].lower()]
    if category_filter:
        expenses_data = [expense for expense in expenses_data if category_filter == '' or category_filter == expense[2]]

    return render_template('index.html', expenses_data=expenses_data)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)