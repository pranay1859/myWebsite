import csv
from flask import Flask, redirect, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_pahe(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as target:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = csv.writer(target, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file.writerow([name, email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
    except:
        return 'Please try again, something went wrong'

