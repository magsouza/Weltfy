from app import app
from flask import render_template, redirect, request, session
import json

import utils.spotify_services as sp
from utils.date_handler import get_3weeks
from utils.csv_gen import generate_csv

'''
@app.route('/')
def index():
    return render_template('home.html')


@app.route('/auth/')
def auth():
    return redirect(sp.AUTH_URL)


@app.route('/redirect/')
def callback():
    auth_token = request.args['code']
    auth_header = sp.authorize(auth_token)
    session['auth_header'] = auth_header
    return redirect('/country')


@app.route('/country', methods=['GET', 'POST'])
def country():
    with open('spotify_countries.json') as s:
        countries = json.load(s)
    return render_template('country.html', countries=countries['countries'])
'''

@app.route('/playlist', methods=['GET', 'POST'])
def playlist():
    print(request.is_json)
    query = request.get_json()
    auth_header = {"Authorization": f"Bearer {query['token']}"}
    interval = get_3weeks()
    country = query['country']
    tracklist = generate_csv(interval, country)
    playlist_id = sp.create_playlist(auth_header, country)  # create the playlist
    sp.fill_playlist(tracklist, playlist_id, auth_header)  # fill the playlist
    url = f'http://open.spotify.com/playlist/{playlist_id}'
    return {'url': url}
