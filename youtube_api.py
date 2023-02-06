from ytmusicapi import YTMusic
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from pytube import YouTube
import json

# YTMusic.setup(filepath="headers_auth.json")
app = Flask(__name__)


ytmusic = YTMusic('headers_auth.json')
@app.route('/stream/<videoId>', methods=['GET'])
def stream(videoId):
    yt = YouTube('https://www.youtube.com/watch?v='+videoId)
    audio_streams = yt.streams.filter(only_audio=True)
    best_audio_stream = sorted(
        audio_streams, key=lambda stream: stream.abr, reverse=True)[0]
    best_audio_stream_url = best_audio_stream.url
    return best_audio_stream_url


@app.route('/', methods=['GET'])
def index():
    return "Youtube Music API convert to Restful API"


@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('q')
    filterq = request.args.get('filter')
    results = ytmusic.search(query, filter=filterq, limit=10)
    return jsonify(results)


@app.route('/home', methods=['GET'])
def home():
    home = ytmusic.get_home(limit=5)
    return jsonify(home)


@app.route('/artist/<artist_id>', methods=['GET'])
def artist(artist_id):
    artist = ytmusic.get_artist(artist_id)
    return jsonify(artist)


@app.route('/<artist_id>/<album_para>', methods=['GET'])
def artist_album(artist_id, album_para):
    album = ytmusic.get_artist_albums(artist_id, album_para)
    return jsonify(album)


@app.route('/album/<album_id>', methods=['GET'])
def album(album_id):
    album = ytmusic.get_album(album_id)
    return jsonify(album)


@app.route('/album/playlistid/<audioPlaylistId>', methods=['GET'])
def album_playlist(audioPlaylistId):
    album = ytmusic.get_album_browse_id(audioPlaylistId)
    return jsonify(album)


@app.route('/user/<channelId>', methods=['GET'])
def user(channelId):
    user = ytmusic.get_user(channelId)
    return jsonify(user)


@app.route('/user/playlists/<channelId>/<params>', methods=['GET'])
def user_playlist(channelId, params):
    user = ytmusic.get_user_playlists(channelId, params)
    return jsonify(user)


@app.route('/song/<videoId>', methods=['GET'])
def song(videoId):
    song = ytmusic.get_song(videoId, 1675530291)
    return jsonify(song)
# artistM = artist("UCFNiNEbbFWpKedIwNJ6UeNw")
# a = convert_to_json(artistM)
# print(a)
 # Playlists


@app.route('/playlist/<playlistId>', methods=['GET'])
def playlist(playlistId):
    playlist = ytmusic.get_playlist(playlistId)
    return jsonify(playlist)


if __name__ == '__main__':

    app.run(debug=True)
