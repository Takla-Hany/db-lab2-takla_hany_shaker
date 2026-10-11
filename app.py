import os
from flask import Flask, render_template, request, redirect, url_for, session
import bcrypt
import pymysql
from db import get_db_connection

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "fallback_dev_key")

@app.route('/register', methods=['GET', 'POST'])
def register():
    # recive the register form information
    if request.method == 'POST':
        name = request.form.get('name').strip()
        email = request.form.get('email').strip()
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        # Validation
        if not name:
            return render_template('register.html', error="Name is required")
        if not email:
            return render_template('register.html', error="Email is required")
        if not password:
            return render_template('register.html', error="Password is required")
        if not confirm_password:
            return render_template('register.html', error="Confirm password is required")
        if password != confirm_password:
            return render_template('register.html', error="Passwords do not match")

        # password Hashing
        hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        connection = get_db_connection()
        try:
            # add register info to database
            with connection.cursor() as cursor:
                sql = "INSERT INTO users (email, name, password_hash) VALUES (%s, %s, %s)"
                cursor.execute(sql, (email, name, hash.decode('utf-8')))
            connection.commit()

            # let user log-in
            with connection.cursor() as cursor:
                cursor.execute("SELECT user_id FROM users WHERE email = %s", (email))
                user = cursor.fetchone()
                session['user_id'] = user['user_id']
            
            return redirect(url_for('index'))

        except:
            return render_template('register.html', error="Email Already Exists")
        finally:
            connection.close()

    # Render register Page
    return render_template('register.html')

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return "not-completed"

@app.route('/login')
def login():
    return "not-completed"

if __name__ == '__main__':
    app.run(debug=True)