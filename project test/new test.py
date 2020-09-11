import requests
import json
import pandas as pd

HEADERS = {
    'Content-Type': 'application/json',
    "Authorization": "Bearer BQBCvsWXy-CqqES9-8gOcoo_qP8dmR2XaqAGAXpgMeSik0xyktKaxMn8SofR7j_LNYS7MoNvW6Xej--ucL8808L2dOdBLJJ6ncAGvWWRSPhFvVz06CVdddjSZMsUjeSp2Ej50YdcMA_p2HoOAmsUaVTDBX39-M8" 
}

response = requests.get('https://api.spotify.com/v1/me/top/artists', headers=HEADERS)

data = response.json()

# Get dataframe info (artist name, genres, popularity, link to artist spotify page)
artists = [item['name'] for item in data['items']]
genres = [item['genres'] for item in data['items']]
popularity = [item['popularity'] for item in data['items']]
urls = [item['external_urls']['spotify'] for item in data['items']]

# create pandas dataframe of above data
df_data = {'Artists':artists, 'Genres':genres, 'Popularity':popularity, 'URLs':urls}
df = pd.DataFrame(df_data)
df.set_index('Artists', inplace=True)

print(df)