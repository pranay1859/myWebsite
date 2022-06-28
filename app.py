import csv
from flask import Flask, redirect, render_template, request
import smtplib
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
        return name, email, subject, message

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            name, email, subject, message = write_to_csv(data)
            bot_message = "\n\n name:{}\n e-mail:{}\n subject {}\n message:{}".format(name, email, subject, message)
            new_message = 'Subject: {}\n\n{}\n\n this is bot generate {}'.format(subject, message, bot_message)
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login('pranay1859@gmail.com', 'czyrpjjlfnsizkvp')
            server.sendmail(email, 'pranay1859@gmail.com', new_message)
            return redirect('/thankyou.html')
    except Exception as e:
        print(e)
        return 'Please try again, something went wrong'

