# Expense Tracking Web Application

## Project Overview
Welcome to the Expense Tracking Web Application project! In this project, I have developed a user-friendly web application that allows users to efficiently manage and track their expenses. By combining the power of Excel, Python, and MySQL, this application enables users to input, categorize, and search their expenses effortlessly.

## Key Features
- **Expense Entry:** Enter expenses with details like date, category, amount, and description.
- **Search:** Easily find expenses using keywords by specific categories.
- **Collaborative Effort:** Developed using Excel, Python, and MySQL technologies.

## Project Structure
- **app.py:** The main Flask application file for routing and rendering templates.
- **templates/:** Contains HTML templates for various pages, such as the home page and about page.
- **expenses.xlsx:** Sample Excel file with fictional expense data.
- **expenses_start.py:** Script to populate the MySQL database with data from `expenses.xlsx`.
- **requirements.txt:** List of required packages to run the application.

## Getting Started
1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run `expenses_start.py` to populate the MySQL database with sample expense data.
4. Run `app.py` to start the Flask application.
5. Open a web browser and navigate to `http://localhost:5000` to access the Expense Tracking Web Application.

## SQL Code for Enhancements
```sql
-- Select specific columns from expenses
SELECT date, category, amount, description FROM expenses;

-- Add index to the category column
ALTER TABLE expenses ADD INDEX idx_category (category);

-- Normalize categories by creating a separate categories table
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

-- Add unique constraint to categories
ALTER TABLE categories ADD CONSTRAINT uc_unique_category UNIQUE KEY (name);

-- Insert a category
INSERT INTO categories (name) VALUES ('Food');

-- Update the expenses table to reference the categories table
ALTER TABLE expenses ADD COLUMN category_id INT;
UPDATE expenses e
JOIN categories c ON e.category = c.name
SET e.category_id = c.id;

-- Add a foreign key constraint to ensure referential integrity
ALTER TABLE expenses ADD CONSTRAINT fk_expenses_category
    FOREIGN KEY (category_id) REFERENCES categories (id);
```

## Contributions and Feedback
This project showcases the fusion of Excel, Python, and MySQL to create a robust expense tracking application. Dive into the code, tailor it to your needs, and explore the realms of data management and visualization. Should you have questions, suggestions, or feedback, don't hesitate to get in touch. Your input aids in refining this project and enhancing skills for future endeavors.

Thank you for delving into the Expense Tracking Web Application project!

**Note:** This project is intended for educational purposes and does not handle real financial data.
