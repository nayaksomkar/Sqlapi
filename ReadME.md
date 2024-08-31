# Instructions for Marketplace Setup and Display

## 1. Database and Table Creation
**File Name: `sqldbcreate.py` and `mongodbcreate.py`**

- **Purpose:** Create the MySQL database and tables.
- **Steps:**
  - Connect to MySQL server.
  - Create the `marketplace` database if it doesn’t exist.
  - Create `customers`, `sellers`, and `items` tables if they don’t exist.

## 2. Data Population
**File Name: `datawrite.py`**

- **Purpose:** Insert data into MySQL and MongoDB if not already present.
- **Steps:**
  - Connect to MySQL and MongoDB.
  - Check for existing data and insert if missing.
  - Populate `customers`, `sellers`, `items`, and `deliveries` collections.

## 3. API Backend
**File Name: `mainapi.py`**

- **Purpose:** Provide APIs to fetch data from MySQL and MongoDB.
- **Steps:**
  - Connect to MySQL and MongoDB.
  - Define API endpoints to return data from `customers`, `sellers`, `items`, and `deliveries`.
  - Enable CORS to allow requests from all origins.

## 4. Frontend Display
**File Name: `main.html`**

- **Purpose:** Display data from the API in a web interface.
- **Steps:**
  - Fetch data from API endpoints for `customers`, `sellers`, `items`, and `deliveries`.
  - Populate HTML tables with the fetched data.
  - Handle errors and display them in the tables.

## Execution Sequence

1. **Run `sqldbcreate.py` and `mongodbcreate.py`** to create the database and tables.
2. **Run `datawrite.py`** to insert initial data into MySQL and MongoDB.
3. **Run `mainapi.py`** to start the Flask server and make API endpoints available.
4. **Open `main.html`** in a web browser to view the data fetched from the API.

This sequence ensures that the database and data are prepared before the server and frontend are used.