
from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def connect_db():
    return sqlite3.connect('technova_store.db')

@app.route('/products', methods=['GET'])
def get_products():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    rows = cursor.fetchall()
    conn.close()
    return jsonify([
        {
            "id": row[0],
            "name": row[1],
            "description": row[2],
            "price": row[3],
            "category": row[4],
            "image": row[5]
        }
        for row in rows
    ])

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM admin WHERE username=? AND password=?", (username, password))
    admin = cursor.fetchone()
    conn.close()

    if admin:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401

if __name__ == '__main__':
    app.run(debug=True)
