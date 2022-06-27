from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<username>')
def hello_world(username=None, post=None):
    return render_template('index.html' ,name=username, post_id=post)