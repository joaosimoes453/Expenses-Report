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
