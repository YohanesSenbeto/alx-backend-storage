-- Task: Create a table named 'users' with specific column definitions and comments for each colum
-- country: Stores the country of the user with predefined options (US, CO, TN) and defaults to 'US'

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);
