# Sales and Orchestra Data Analysis

This repository contains a Python script that performs various analyses on sales and orchestra data. The script utilizes libraries such as NumPy and Pandas to manipulate and analyze datasets.

## Features

### 1. Sales Managers and Total Sales:
Analyzes sales data to display the managers along with the grand total sales made by sales agents reporting to these managers.

### 2. Sales Agents and Profitable Sales:
Identifies sales agents who sold products at a profit and displays the respective sales agents and the count of such sales.

### 3. Sales Agents Losing Opportunities:
Lists sales agents who lost at least two opportunities, displaying the sales agent names and the count of lost opportunities.

### 4. Monthly Sales for a Specific Product (GTXBasic):
Analyzes sales for the product "GTXBasic" and displays the sales count for each month of the year.

### 5. Sales Agents Without Lost Deals:
Identifies sales agents who never lost a deal and displays the information as a dictionary with the sales agent name and the count of sales.

### 6. Instrument Played by a Specific Artist:
Utilizes a JSON file containing orchestra data to find and display the instrument played by the artist "Lehmann Caroline."

### 7. All Vocalists:
Extracts and displays the names of all vocalists from the orchestra data.

### 8. Orchestra Played Under a Specific Program ID:
Finds and displays the orchestra played under program ID 2561.

### 9. Locations for Events at Specific Time:
Parses an XML file to find and display locations used for events at the time 8:15 PM.

### 10. Total Number of Programs:
Counts and displays the total number of programs in the orchestra XML file.

## Datasets

The script operates on several CSV and JSON files, including:
- `accounts.csv`
- `clicks.csv`
- `products.csv`
- `sales_pipeline.csv`
- `sales_teams.csv`
- `Orchestra.json`
- `Orchestra.xml`

## Dependencies

- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
