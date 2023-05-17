-- This SQL script creates a Postgres schema, tables, and columns

-- Create schema named accreditation
CREATE SCHEMA IF NOT EXISTS veeva;

-- Create project_under_test table
CREATE TABLE IF NOT EXISTS veeva.testtable(
	rtsm_url TEXT PRIMARY KEY, 
	username TEXT NOT NULL, 
	password TEXT NOT NULL, 
);
