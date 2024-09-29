from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Secret key for session management and flash messages

# Simulated user database (username: password)
users_db = {}

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Registration Page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db:
            flash('Username already exists. Try a different one.')
            return redirect(url_for('register'))
        users_db[username] = password
        flash('Registration successful! Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users_db and users_db[username] == password:
            return redirect(url_for('secured_page', username=username))
        else:
            flash('Invalid username or password.')
            return redirect(url_for('login'))
    return render_template('login.html')

# Secured Page
@app.route('/secured/<username>')
def secured_page(username):
    return render_template('secured.html', username=username)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
