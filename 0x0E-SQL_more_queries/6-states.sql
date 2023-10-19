-- a script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on my MySQL server

-- Create the database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- Use the database
USE hbtn_0d_usa;

-- Create the 'states' table with basic structure
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
	);

