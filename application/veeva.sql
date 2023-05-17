-- This SQL script creates a Postgres schema, tables, and columns

-- Create schema named veeva
CREATE SCHEMA IF NOT EXISTS veeva;

-- Create veevainfo table
CREATE TABLE IF NOT EXISTS veeva.veevainfo(
	rtsm_url TEXT PRIMARY KEY, 
	username TEXT NOT NULL, 
	password TEXT NOT NULL, 
);

-- Create subjectinfo table
CREATE TABLE IF NOT EXISTS veeva.subjectinfo(
	subject_id TEXT PRIMARY KEY,
	site_number TEXT NOT NULL, 
	date_of_birth DATE NOT NULL, 
	sex VARCHAR(10) NOT NULL, 
	rand_id INT,
	previous_treatment BOOLEAN,
	severity VARCHAR(25),
	cohort TEXT,
	randomized_status VARCHAR(25),
	status_date DATE,
	next_event VARCHAR(25)
);
