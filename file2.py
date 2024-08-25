from flask import Flask, request, jsonify
import sqlite3
import bcrypt
import os
import re

app = Flask(__name__)
app.config['DATABASE'] = os.getenv('DATABASE_URL', 'users.db')

def validate_input(username, password):
    if not re.match("^[a-zA-Z0-9_]+$", username):
        return False
    if len(password) < 8:
        return False
    return True

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    
    if not validate_input(username, password):
        return jsonify({'message': 'Invalid input'}), 400
    
    hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY, password TEXT)")
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    
    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
