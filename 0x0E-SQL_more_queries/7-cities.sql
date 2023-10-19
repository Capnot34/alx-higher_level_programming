-- a script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on my MySQL server
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- Use the specified database
USE hbtn_0d_usa;


-- Assuming the states table structure, for reference:
CREATE TABLE IF NOT EXISTS states (
	id INT AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(255) NOT NULL
	);


-- creating the table 'cities'
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY(state_id) REFERENCES states(id)
	);

