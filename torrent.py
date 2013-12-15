from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True
))

@app.route('/')
def welcome():
    return render_template('welcome.html', navloc='home')

@app.route('/tracker')
def tracker():
    return render_template('tracker.html', navloc='tracker')

if __name__ == '__main__':
    app.run()
