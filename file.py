from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.form['username']
    password = request.form['password']
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (username, password) VALUES ('{username}', '{password}')")
    conn.commit()
    conn.close()
    
    return jsonify({'message': 'User added successfully'})

if __name__ == '__main__':
    app.run(debug=True)
