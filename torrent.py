from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from pytvdbapi import api

app = Flask(__name__)

app.config.update(dict(
    DEBUG=True
))

@app.route('/')
def welcome():
    return render_template('welcome.html', navloc='home')

@app.route('/tracker')
def tracker():
    db = api.TVDB('BECF7AA2B2C2B4F4',actors=False,banners=True)
    result = db.search('Dexter', 'en')
    show = result[0]
    show.load_banners()
    amount = len(show.banner_objects)
    bannerurl = show.banner_objects[0].banner_url
    return render_template('tracker.html', navloc='tracker', bannerpath=bannerurl)

if __name__ == '__main__':
    app.run()
