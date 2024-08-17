from flask import Flask, redirect, render_template, request, url_for
from controller.signin import signin_controller
from controller.login import login_controller

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        formData = {field: request.form[field] for field in request.form}
        response = login_controller(formData)
        if response == "Loggedin":
            return redirect(url_for('dashboard'))
        error = response
    return render_template('login.html', error=error)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None
    if request.method == 'POST':
        formData = {field: request.form[field] for field in request.form}
        response = signin_controller(formData)
        if response == 'inserted':
            return redirect(url_for('login'))
        error = response
    return render_template('signin.html', error=error)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
