from flask import Flask, render_template, request, redirect, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="hotel_booking"
)
cursor = db.cursor(dictionary=True)

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            session['user_id'] = user['id']
            return "Login Successful! Redirect to dashboard or booking page."
        else:
            flash("Invalid credentials")
            return redirect('/login')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
