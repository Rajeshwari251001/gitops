from flask import Flask, render_template, request

app = Flask(_name_)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}! Thank you for submitting the form."

if _name_ == '_main_':
    app.run(host='0.0.0.0',debug=True)