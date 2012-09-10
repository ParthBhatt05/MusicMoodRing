"""
Music Mood Ring
"""

import os

from flask import Flask
from flask import request
from flask import url_for, redirect
from flask import render_template

from lfmlibs import lfm_get_info

# from secrets import apikey, sign
# import urllib
# import json

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')

#@app.route('/lfm_playlist/<uname>')
#def get_lfm_list(uname):
#    my_tracks = lfm_get_info(uname, 20)
#    return str(my_tracks)

@app.route('/get/mood/<uname>')
def get_moods(uname):
    tracks, moods, themes = lfm_get_info(uname, 20)
    return render_template('moods.html', tracks=tracks, moods=moods,
                           themes=themes, user=uname)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
