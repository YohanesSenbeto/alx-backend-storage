-- Create a table named "users" if it doesn't already exist. This table should have three columns:
-- - id: an auto-incremented integer acting as the primary key
-- - email: a VARCHAR field of maximum length 255, not allowing NULL values, and must be unique
-- - name: a VARCHAR field of maximum length 255, allowing NULL values
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
