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

    # Feed url: feed://ezrss.it/search/index.php?simple&show_name=Big+Bang+Theory&mode=rss


    # tvdb information
    db = api.TVDB('BECF7AA2B2C2B4F4',actors=False,banners=True)
    result = db.search('Dexter', 'en')
    show = result[0]
    show.load_banners()

    seasons = [b for b in show.banner_objects if b.BannerType == "season" and b.BannerType2 == "seasonwide"]

    return render_template('tracker.html', navloc='tracker', banners=seasons)

@app.route('/search')
def search():
    return render_template('search.html', navloc='tracker')

@app.route('/result')
def result():

    return render_template('search.html', navloc='tracker', data=True)
if __name__ == '__main__':
    app.run()
