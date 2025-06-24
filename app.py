from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Renders the form

@app.route('/home1', methods=['POST'])  # Accepts POST request from the form
def home1():
    name = request.form['name']  # Gets name from form data
    return f"Welcome {name}"

if __name__ == '__main__':
    app.run(debug=True)
 