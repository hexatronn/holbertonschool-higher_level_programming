-- Create DB hbtn_0d_usa and table cities

-- Create DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use DB
USE hbtn_0d_usa;

-- Create table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);
