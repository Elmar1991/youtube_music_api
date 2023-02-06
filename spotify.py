import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
    client_id='721d6f670f074b1497e74fc59125a6f3', client_secret='efddc083fa974d39bc6369a892c07ced',))


def find_track_id(search_query):
    results = spotify.search(q='track:' + search_query, type='track')
    track_id = results['tracks']['items'][0]['id']
    return track_id



