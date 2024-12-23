import sqlite3
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

DB_PATH = '/data/db/database.sqlite'

@app.route('/users', methods=['GET'])
def get_users():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("SELECT id, name, email FROM users")
    rows = cursor.fetchall()

    conn.close()

    return jsonify([
        {"id": row[0], "name": row[1], "email": row[2]} for row in rows
    ])


@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or not data.get('name') or not data.get('email'):
        abort(400, "Bad Request: 'name' and 'email' are required.")

    name = data['name']
    email = data['email']

    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()

        new_user_id = cursor.lastrowid
        conn.close()

        return jsonify({"id": new_user_id, "name": name, "email": email}), 201  # HTTP 201 Created

    except sqlite3.IntegrityError as e:
        abort(400, f"Bad Request: {str(e)}")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
