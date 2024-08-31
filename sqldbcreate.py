import mysql.connector as con

def create_mysql_database():
    try:
        # Connect to MySQL server
        connection = con.connect(
            host='localhost',
            user='root',
            password='0000',  # Update your password
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS marketplace")
            print("MySQL Database created successfully")
   
    except Exception as error:
        print(f"Error: {error}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def create_mysql_tables():
    try:
        # Connect to 'marketplace' database
        connection = con.connect(
            host='localhost',
            user='root',
            password='0000',  # Update your password
            database='marketplace'
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create 'customers' table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS customers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    address VARCHAR(255)
                )
            """)

            # Create 'sellers' table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sellers (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    email VARCHAR(100) UNIQUE,
                    business_name VARCHAR(100)
                )
            """)

            # Create 'items' table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS items (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100),
                    description TEXT,
                    price DECIMAL(10, 2),
                    seller_id INT,
                    FOREIGN KEY (seller_id) REFERENCES sellers(id)
                )
            """)

            print("MySQL Tables created successfully")
            
    except Exception as error:
        print(f"Error: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_mysql_database()
    create_mysql_tables()
