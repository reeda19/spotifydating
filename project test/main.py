import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = 'user-top-read' #how much we are allowed to see from user

# these should be delted and instead added to ENV VARs
client_id = 'eb9a37f93d5148e28e113134d65d6c08'
client_secret = '29d3cde540304c43b72e8b344c605f63'
redirect_uri = 'project-songbird-login://callback'

# authenticate use
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,client_id=client_id,client_secret=client_secret,redirect_uri=redirect_uri))

#Get dataframe info (artist name, genres, popularity, link to artist spotify page)
data = sp.current_user_top_artists()




artists = [item['name'] for item in data['items']]
genres = [item['genres'] for item in data['items']]
popularity = [item['popularity'] for item in data['items']]
urls = [item['external_urls']['spotify'] for item in data['items']]

# create pandas dataframe of above data
df_data = {'Artists': artists, 'Genres': genres, 'Popularity': popularity, 'URLs': urls}
df = pd.DataFrame(df_data)
df.set_index('Artists', inplace=True)

print(df)
