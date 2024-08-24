from flask import Flask, request, jsonify
import sqlite3
import hashlib
import re

app = Flask(__name__)

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
    
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
