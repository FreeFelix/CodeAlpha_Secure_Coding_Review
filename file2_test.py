import pytest
from flask import Flask
from flask.testing import FlaskClient
import sqlite3
import os
import hashlib
import re

# Import the application
from your_flask_app import app

@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    app.config['DATABASE'] = 'test_users.db'
    
    with app.test_client() as client:
        yield client

    # Clean up after test
    if os.path.exists(app.config['DATABASE']):
        os.remove(app.config['DATABASE'])

def init_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT)")
    conn.commit()
    conn.close()

def test_add_user_valid(client):
    init_db()
    
    response = client.post('/add_user', data={
        'username': 'testuser',
        'password': 'securepassword'
    })
    
    assert response.status_code == 200
    assert response.json == {'message': 'User added successfully'}

    conn = sqlite3.connect(app.config['DATABASE'])
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=?", ('testuser',))
    user = cursor.fetchone()
    conn.close()
    
    assert user is not None
    assert hashlib.sha256(b'securepassword').hexdigest() == user[1]

def test_add_user_invalid_username(client):
    init_db()
    
    response = client.post('/add_user', data={
        'username': 'invalid_user!',
        'password': 'securepassword'
    })
    
    assert response.status_code == 400
    assert response.json == {'message': 'Invalid input'}

def test_add_user_invalid_password(client):
    init_db()
    
    response = client.post('/add_user', data={
        'username': 'validuser',
        'password': 'short'
    })
    
    assert response.status_code == 400
    assert response.json == {'message': 'Invalid input'}
