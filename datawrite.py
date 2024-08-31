import mysql.connector
from pymongo import MongoClient
from datetime import datetime

def mysql_data():
    connection = mysql.connector.connect(
        host="localhost", user="root", password="0000", database="marketplace"
    )
    cursor = connection.cursor()

    # Insert customer if not exists
    cursor.execute("SELECT * FROM customers WHERE email = 'john@example.com'")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO customers (name, email, address) VALUES
            ('John Doe', 'john@example.com', '123 Main St')
        """
        )

    cursor.execute("SELECT * FROM customers WHERE email = 'jane@example.com'")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO customers (name, email, address) VALUES
            ('Jane Smith', 'jane@example.com', '456 Elm St')
        """
        )

    # Insert seller if not exists
    cursor.execute("SELECT * FROM sellers WHERE email = 'bob@example.com'")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO sellers (name, email, business_name) VALUES
            ('Bob Johnson', 'bob@example.com', 'Bob''s Electronics')
        """
        )

    cursor.execute("SELECT * FROM sellers WHERE email = 'alice@example.com'")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO sellers (name, email, business_name) VALUES
            ('Alice Brown', 'alice@example.com', 'Alice''s Apparel')
        """
        )

    # Insert item if not exists
    cursor.execute("SELECT * FROM items WHERE name = 'Laptop' AND seller_id = 1")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO items (name, description, price, seller_id) VALUES
            ('Laptop', 'High-performance laptop', 999.99, 1)
        """
        )

    cursor.execute("SELECT * FROM items WHERE name = 'T-shirt' AND seller_id = 2")
    if cursor.fetchone() is None:
        cursor.execute(
            """
            INSERT INTO items (name, description, price, seller_id) VALUES
            ('T-shirt', 'Cotton t-shirt', 19.99, 2)
        """
        )

    connection.commit()
    cursor.close()
    connection.close()

def mongodb_data():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["marketplace"]
    deliveries = db.deliveries

    # Insert delivery if not exists
    if deliveries.count_documents({"order_id": 1}) == 0:
        deliveries.insert_one(
            {
                "order_id": 1,
                "status": "In Transit",
                "location": {"lat": 40.7128, "lon": -74.0060},
                "timestamp": datetime.now(),
            }
        )

    if deliveries.count_documents({"order_id": 2}) == 0:
        deliveries.insert_one(
            {
                "order_id": 2,
                "status": "Delivered",
                "location": {"lat": 34.0522, "lon": -118.2437},
                "timestamp": datetime.now(),
            }
        )

if __name__ == "__main__":
    mysql_data()
    mongodb_data()
    print("Data written successfully")