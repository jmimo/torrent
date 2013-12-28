from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from pytvdbapi import api
import feedparser

app = Flask(__name__)
tvdb = api.TVDB('BECF7AA2B2C2B4F4',actors=False,banners=True)

app.config.update(dict(
    DEBUG=True
))

@app.route('/')
def welcome():
    return render_template('welcome.html', navloc='home')

@app.route('/tracker')
def tracker():

    # Feed url: feed://ezrss.it/search/index.php?simple&show_name=Big+Bang+Theory&mode=rss
    return render_template('tracker.html', navloc='tracker')

@app.route('/search',methods=['POST'])
def search():
    searchValue = request.form['search.value']
    # TODO: input validation
    result = tvdb.search(searchValue, 'en')
    if len(result) == 1:
        return redirect(url_for('showdetails', showid=result[0].id))
    else:
        return render_template('search.html', navloc='home', shows=result)

@app.route('/showdetails/<showid>', methods=['GET'])
def showdetails(showid):
    tvdbshow = tvdb.get_series(showid,'en')
    tvdbshow.update()

    #feed = feedparser.parse('http://www.torrentreactor.net/rss.php?search=' + tvdbshow.SeriesName)
    #feed = feedparser.parse('http://www.ievsoftware.com/rss/tv.php?show=' + tvdbshow.SeriesName)
    feed = feedparser.parse('http://kat.ph/search/' + tvdbshow.SeriesName + '/?rss=1')

    filtered = [item for item in feed.entries if item.category == 'TV']

    return render_template('showdetails1.html', navloc='home', show=tvdbshow, feed=filtered)

if __name__ == '__main__':
    app.run()
