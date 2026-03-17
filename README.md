# CSV Data Validation Pipeline

## Overview

This project is a Python-based automation script designed to clean and validate CSV datasets. It ensures data quality by validating structure, enforcing field-level rules, removing duplicates, and maintaining consistency across related files.

The pipeline processes multiple CSV files (e.g., customers and orders) and enforces relationships between them using in-memory data structures.

---

## Features

- Header (schema) validation  
- Row structure validation (column count check)  
- Field-level validation:
  - Numeric ID checks  
  - Email format check (@)  
  - Phone number validation (10 digits)  
  - Non-empty mandatory fields  
- Duplicate detection using sets  
- Data segregation:
  - Valid records  
  - Invalid records  
- Cross-file validation:
  - Ensures customer_id in orders exists in customers dataset  
- Clean output generation into new CSV files  

---

## How It Works

### Step 1: Process Customers Data

- Reads customers_2000.csv  
- Validates:
  - Header format  
  - Row length  
  - Field values (ID, name, phone, email, city)  
- Removes duplicates using a set (customer_ids)  
- Stores valid customer IDs in memory  

---

### Step 2: Process Orders Data

- Reads orders_5000.csv  
- Validates:
  - Header format  
  - Row structure  
  - Order ID uniqueness  
  - Product name presence  
  - Quantity and amount (positive integers)  
- Performs cross-file validation:
  - Ensures customer_id exists in the validated customer dataset  

---

### Step 3: Output

Generates four files:

- val1rec.csv → Valid customer records  
- inval1rec.csv → Invalid customer records  
- val2rec.csv → Valid order records  
- inval2rec.csv → Invalid order records  

---

## Key Concepts Demonstrated

- Data validation pipeline  
- Schema and field validation  
- Duplicate detection (uniqueness constraints)  
- Data cleaning and filtering  
- Cross-file validation  
- Referential integrity enforcement  
- In-memory data processing using sets  
- Defensive programming  

---

## Tech Stack

- Python  
- Built-in csv module  
- File handling  
- Data structures (list, set)  

---

## Example Use Case

This type of pipeline is commonly used in:

- Cleaning customer and transaction data  
- Preparing datasets before analysis  
- Validating business records before storage  
- Automating data quality checks in workflows  

---

## How to Run

1. Place input files:
   - customers_2000.csv  
   - orders_5000.csv  

2. Run the script:

python script.py

3. Check generated output files in the same directory.

---

## Future Improvements

- Add detailed error reporting (reason-wise counts)  
- Convert script into reusable functions  
- Add logging instead of print statements  
- Support JSON and Excel formats  
- Integrate with APIs for real-time validation  
