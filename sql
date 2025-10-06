CREATE DATABASE hotel_booking;

USE hotel_booking;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(100) NOT NULL
);

-- Add a sample user
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
