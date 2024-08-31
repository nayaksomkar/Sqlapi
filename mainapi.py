from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)  # Allow all origins by default

# MySQL connection
def get_mysql_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='0000',
        database='marketplace'
    )

# MongoDB connection
mongo_client = MongoClient('mongodb://localhost:27017/')
mongo_db = mongo_client['marketplace']

@app.route('/customers', methods=['GET'])
def get_customers():
    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(customers)

@app.route('/sellers', methods=['GET'])
def get_sellers():
    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM sellers")
    sellers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(sellers)

@app.route('/items', methods=['GET'])
def get_items():
    conn = get_mysql_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(items)

@app.route('/deliveries', methods=['GET'])
def get_deliveries():
    deliveries = list(mongo_db.deliveries.find({}, {'_id': 0}))
    return jsonify(deliveries)

if __name__ == '__main__':
    app.run(debug=True)
