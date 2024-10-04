#!/Dev/laragon/bin/python/python-3.10/python.exe
from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="login_db"
    )

# Landing page - login
@app.route('/')
def index():
    return render_template('login.html')

# Login handler
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
    user = cursor.fetchone()
    
    if user:
        session['username'] = username
        return redirect(url_for('home'))
    else:
        return "Feil brukernavn eller passord."

# Home page after login
@app.route('/home')
def home():
    if 'username' in session:
        return render_template('home.html', username=session['username'])
    return redirect(url_for('index'))

# Logout handler
@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
