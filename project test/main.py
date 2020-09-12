import requests
import json
import pandas as pd
import pkce  # used for code verification/challenge
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

client_id = 'eb9a37f93d5148e28e113134d65d6c08'
client_secret = '29d3cde540304c43b72e8b344c605f63'
redirect_uri = 'project-songbird-login://callback'

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(scope=scope, client_secret=client_secret, client_id=client_id, redirect_uri=redirect_uri))

# token = spotipy.oauth2.SpotifyAuthBase.get_access_token()
#
# HEADERS = {
#     'Content-Type': 'application/json',
#     "Authorization": "Bearer" + token
# }
#
# response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=HEADERS)
#
# data = response.json()

data = sp.current_user_top_tracks()


print(data)
# Get dataframe info (artist name, genres, popularity, link to artist spotify page)
artists = [item['name'] for item in data['items']]
genres = [item['genres'] for item in data['items']]
popularity = [item['popularity'] for item in data['items']]
urls = [item['external_urls']['spotify'] for item in data['items']]

# create pandas dataframe of above data
df_data = {'Artists': artists, 'Genres': genres, 'Popularity': popularity, 'URLs': urls}
df = pd.DataFrame(df_data)
df.set_index('Artists', inplace=True)

print(df)
